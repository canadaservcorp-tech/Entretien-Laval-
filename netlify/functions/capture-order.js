// POST /.netlify/functions/capture-order  { orderID }  ->  { id, status, capture_id, capture_status, amount }
const { json, apiBase, accessToken } = require('../lib/shared');

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') return json(405, { error: 'method' });
  let b;
  try { b = JSON.parse(event.body || '{}'); } catch { return json(400, { error: 'json' }); }
  const id = String(b.orderID || '');
  if (!/^[A-Z0-9]{8,40}$/.test(id)) return json(400, { error: 'order' });
  try {
    const r = await fetch(apiBase() + '/v2/checkout/orders/' + id + '/capture', {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + (await accessToken()), 'Content-Type': 'application/json', 'PayPal-Request-Id': 'capture-' + id },
    });
    const d = await r.json();
    if (!r.ok) {
      const issue = d.details && d.details[0] && d.details[0].issue;
      console.error('capture-order', r.status, issue || JSON.stringify(d).slice(0, 800));
      return json(r.status === 422 ? 422 : 502, { error: 'capture', issue });
    }
    const cap = (((d.purchase_units || [])[0] || {}).payments || {}).captures || [];
    return json(200, { id: d.id, status: d.status, capture_id: cap[0] && cap[0].id, capture_status: cap[0] && cap[0].status, amount: cap[0] && cap[0].amount && cap[0].amount.value });
  } catch (e) {
    console.error('capture-order', e.message);
    return json(502, { error: 'paypal' });
  }
};
