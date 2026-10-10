// POST /.netlify/functions/create-order  { lang, lines:[{id,qty}], contact:{...} }  ->  { id }
const { json, validate, apiBase, accessToken, orderBody } = require('../lib/shared');

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') return json(405, { error: 'method' });
  let b;
  try { b = JSON.parse(event.body || '{}'); } catch { return json(400, { error: 'json' }); }
  const v = validate(b);
  if (v.error) return json(400, { error: v.error });
  try {
    const r = await fetch(apiBase() + '/v2/checkout/orders', {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + (await accessToken()), 'Content-Type': 'application/json', Prefer: 'return=minimal' },
      body: JSON.stringify(orderBody(v)),
    });
    const d = await r.json();
    if (!r.ok || !d.id) { console.error('create-order', r.status, JSON.stringify(d).slice(0, 800)); return json(502, { error: 'paypal' }); }
    return json(200, { id: d.id });
  } catch (e) {
    console.error('create-order', e.message);
    return json(502, { error: 'paypal' });
  }
};
