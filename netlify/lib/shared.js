// Shared server logic for the PayPal checkout (Netlify Functions).
// The browser never decides the price: totals are recomputed here from catalog.json,
// which tools/build.py generates from tools/content.py + tools/content_order.py.
// Secrets come from Netlify environment variables, never from the repo:
//   PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET, PAYPAL_ENV ("live" or "sandbox")
const CAT = require('./catalog.json');

const r2 = (n) => Math.round((n + Number.EPSILON) * 100) / 100;
const fx = (n) => r2(n).toFixed(2);
const json = (statusCode, obj) => ({
  statusCode,
  headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  body: JSON.stringify(obj),
});

function zoneFor(pc) {
  const p = String(pc || '').toUpperCase().replace(/\s+/g, '');
  return (CAT.zones || []).find((z) => p.startsWith(z.prefix)) || null;
}

function totals(lines, zone) {
  let goods = 0, bags = 0;
  for (const l of lines) { goods += CAT.products[l.id].price * l.qty; bags += l.qty; }
  const del = bags === 0 || !zone ? 0 : (CAT.free && bags >= CAT.free ? 0 : zone.fee);
  const sub = goods + del, gst = r2(sub * CAT.gst), qst = r2(sub * CAT.qst);
  return { bags, goods: r2(goods), del: r2(del), gst, qst, total: r2(goods + del + gst + qst) };
}

const str = (v, max) => (typeof v === 'string' ? v.trim().slice(0, max) : '');

function validate(b) {
  if (!CAT.enabled) return { error: 'disabled' };
  if (!b || typeof b !== 'object') return { error: 'body' };
  const lang = b.lang === 'en' ? 'en' : 'fr';
  if (!Array.isArray(b.lines) || b.lines.length > Object.keys(CAT.products).length) return { error: 'lines' };
  const seen = new Set(), lines = [];
  for (const l of b.lines) {
    if (!l || !CAT.products[l.id] || seen.has(l.id)) return { error: 'product' };
    const qty = Number(l.qty);
    if (!Number.isInteger(qty) || qty < 0 || qty > CAT.max) return { error: 'qty' };
    seen.add(l.id);
    if (qty > 0) lines.push({ id: l.id, qty });
  }
  const bags = lines.reduce((s, l) => s + l.qty, 0);
  if (bags < 1 || bags > CAT.max) return { error: 'qty' };
  const c = b.contact || {};
  const contact = {
    nom: str(c.nom, 100), entreprise: str(c.entreprise, 100), courriel: str(c.courriel, 254),
    telephone: str(c.telephone, 30), adresse: str(c.adresse, 200), ville: str(c.ville, 80),
    code_postal: str(c.code_postal, 7).toUpperCase(), instructions: str(c.instructions, 500),
  };
  const pc = contact.code_postal.replace(/\s+/g, '');
  contact.code_postal = pc.length === 6 ? pc.slice(0, 3) + ' ' + pc.slice(3) : pc;
  if (!contact.nom || !contact.adresse || !contact.ville || contact.telephone.length < 7) return { error: 'fields' };
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contact.courriel)) return { error: 'email' };
  if (!new RegExp(CAT.postal).test(contact.code_postal)) return { error: 'postal' };
  const zone = zoneFor(contact.code_postal);
  if (!zone) return { error: 'postal' };
  if (contact.ville !== zone.name) return { error: 'city' };
  if (bags < zone.min_bags) return { error: 'min' };
  return { lang, lines, contact, zone };
}

function apiBase() {
  return process.env.PAYPAL_ENV === 'live' ? 'https://api-m.paypal.com' : 'https://api-m.sandbox.paypal.com';
}

async function accessToken() {
  const id = process.env.PAYPAL_CLIENT_ID, secret = process.env.PAYPAL_CLIENT_SECRET;
  if (!id || !secret) throw new Error('PayPal credentials missing in Netlify environment variables');
  const r = await fetch(apiBase() + '/v1/oauth2/token', {
    method: 'POST',
    headers: { Authorization: 'Basic ' + Buffer.from(id + ':' + secret).toString('base64'), 'Content-Type': 'application/x-www-form-urlencoded' },
    body: 'grant_type=client_credentials',
  });
  if (!r.ok) throw new Error('PayPal token HTTP ' + r.status);
  return (await r.json()).access_token;
}

function orderBody(v) {
  const t = totals(v.lines, v.zone);
  const items = v.lines.map((l) => ({
    name: (CAT.products[l.id]['name_' + v.lang] + (v.lang === 'fr' ? ' – sac de 25 lb' : ' – 25 lb bag')).slice(0, 127),
    sku: l.id, quantity: String(l.qty), category: 'PHYSICAL_GOODS',
    unit_amount: { currency_code: 'CAD', value: fx(CAT.products[l.id].price) },
  }));
  return {
    intent: 'CAPTURE',
    purchase_units: [{
      reference_id: 'chiffons-eco',
      description: 'Chiffons ÉCO – Entretien Laval',
      custom_id: (v.contact.entreprise || v.contact.nom).slice(0, 127),
      items,
      amount: {
        currency_code: 'CAD', value: fx(t.total),
        breakdown: {
          item_total: { currency_code: 'CAD', value: fx(t.goods) },
          shipping: { currency_code: 'CAD', value: fx(t.del) },
          tax_total: { currency_code: 'CAD', value: fx(t.gst + t.qst) },
        },
      },
      shipping: {
        name: { full_name: v.contact.nom },
        address: { address_line_1: v.contact.adresse, admin_area_2: v.contact.ville, admin_area_1: 'QC', postal_code: v.contact.code_postal, country_code: 'CA' },
      },
    }],
    application_context: {
      brand_name: 'Chiffons ÉCO – Entretien Laval', locale: v.lang === 'fr' ? 'fr-CA' : 'en-CA',
      shipping_preference: 'SET_PROVIDED_ADDRESS', user_action: 'PAY_NOW',
    },
  };
}

module.exports = { CAT, r2, fx, json, zoneFor, totals, validate, apiBase, accessToken, orderBody };
