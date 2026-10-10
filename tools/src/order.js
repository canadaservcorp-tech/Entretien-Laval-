/* Online order page: live totals + PayPal Buttons.
   Totals shown here are for display only; the server (netlify/lib/shared.js) recomputes them from its own catalog.
   No payment-method fee is ever added (PayPal user agreement + Québec Consumer Protection Act). */
document.addEventListener('DOMContentLoaded', function () {
  var C = window.ORDER_CFG, U = C.ui;
  var $ = function (id) { return document.getElementById(id); };
  var form = $('oform'), err = $('o-err');
  var r2 = function (n) { return Math.round((n + Number.EPSILON) * 100) / 100; };
  var PRICE = {}; C.products.forEach(function (p) { PRICE[p.id] = p; });

  function money(n) {
    var o = { minimumFractionDigits: 2, maximumFractionDigits: 2 };
    return C.lang === 'fr' ? n.toLocaleString('fr-CA', o) + ' $' : '$' + n.toLocaleString('en-CA', o);
  }
  function lines() {
    return [].map.call(document.querySelectorAll('.oqty'), function (i) {
      return { id: i.getAttribute('data-id'), qty: Math.max(0, Math.floor(Number(i.value) || 0)) };
    }).filter(function (l) { return l.qty > 0; });
  }
  function totals(ls) {
    var goods = 0, bags = 0;
    ls.forEach(function (l) { goods += PRICE[l.id].price * l.qty; bags += l.qty; });
    var del = bags === 0 ? 0 : ((C.free && bags >= C.free) ? 0 : C.fee);
    var sub = goods + del, gst = r2(sub * C.gst), qst = r2(sub * C.qst);
    return { bags: bags, goods: r2(goods), del: r2(del), gst: gst, qst: qst, total: r2(goods + del + gst + qst) };
  }
  function val(name) { var e = form.elements[name]; return e ? String(e.value).trim() : ''; }
  function postal() { var p = val('code_postal').toUpperCase().replace(/\s+/g, ''); return p.length === 6 ? p.slice(0, 3) + ' ' + p.slice(3) : p; }
  function contact() {
    return { nom: val('nom'), entreprise: val('entreprise'), courriel: val('courriel'), telephone: val('telephone'),
             adresse: val('adresse'), ville: val('ville'), code_postal: postal(), instructions: val('instructions') };
  }
  function problem() {
    var t = totals(lines()), c = contact();
    if (t.bags < 1 || t.bags > C.max) return U.e_bags.replace('{max}', C.max);
    if (!c.nom || !c.courriel || !c.telephone || !c.adresse || !c.ville || !c.code_postal || !form.checkValidity()) return U.e_fields;
    if (!new RegExp(C.postal).test(c.code_postal)) return U.e_postal;
    return '';
  }
  function show(msg) { err.textContent = msg; err.hidden = !msg; }
  function render() {
    var t = totals(lines());
    $('o-goods').textContent = money(t.goods);
    $('o-del').textContent = t.bags && t.del === 0 ? U.free : money(t.del);
    $('o-gst').textContent = money(t.gst);
    $('o-qst').textContent = money(t.qst);
    $('o-total').textContent = money(t.total);
  }
  function post(fn, body) {
    return fetch(C.fn + '/' + fn, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
      .then(function (r) { return r.json(); });
  }
  function record(d) {
    var t = totals(lines()), c = contact();
    var data = { 'form-name': 'commande', langue: C.lang, commande_paypal: d.id, capture: d.capture_id || '', statut: d.capture_status || d.status,
                 montant: d.amount || String(t.total),
                 details: lines().map(function (l) { return l.qty + ' x ' + PRICE[l.id].name; }).join(' | '),
                 totaux: 'Produits ' + t.goods + ' / Livraison ' + t.del + ' / TPS ' + t.gst + ' / TVQ ' + t.qst + ' / Total ' + t.total };
    Object.keys(c).forEach(function (k) { data[k] = c[k]; });
    return fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() })
      .then(function (r) { if (!r.ok) throw new Error('form'); });
  }

  form.addEventListener('input', function () { render(); if (!err.hidden && !problem()) show(''); });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  render();

  if (!window.paypal) { show(U.e_pay); return; }
  window.paypal.Buttons({
    style: { layout: 'vertical', label: 'pay' },
    onInit: function (data, actions) {
      var sync = function () { if (problem()) actions.disable(); else actions.enable(); };
      sync(); form.addEventListener('input', sync);
    },
    onClick: function () { show(problem()); },
    createOrder: function () {
      return post('create-order', { lang: C.lang, lines: lines(), contact: contact() }).then(function (d) {
        if (!d.id) { show(d.error === 'postal' ? U.e_postal : U.e_pay); throw new Error(d.error || 'create'); }
        return d.id;
      });
    },
    onApprove: function (data, actions) {
      return post('capture-order', { orderID: data.orderID }).then(function (d) {
        if (d.issue === 'INSTRUMENT_DECLINED') return actions.restart();
        if (d.status !== 'COMPLETED') { show(U.e_pay); return; }
        return record(d).then(function () { location.href = C.thanks + '?commande=' + encodeURIComponent(d.id); },
                              function () { show(U.e_after + d.id); });
      });
    },
    onError: function () { if (err.hidden) show(U.e_pay); }
  }).render('#paypal-buttons');
});
