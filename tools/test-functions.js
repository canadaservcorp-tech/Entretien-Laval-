// Server tests for the PayPal checkout, PayPal API mocked. Run: node test-functions.js <repo path>
const path = require('path'); const R = process.argv[2];
process.env.PAYPAL_CLIENT_ID='id'; process.env.PAYPAL_CLIENT_SECRET='sec';
let sent=null, calls=[];
global.fetch = async (url, opt) => { calls.push(url);
  if (url.endsWith('/v1/oauth2/token')) return {ok:true, status:200, json:async()=>({access_token:'T'})};
  if (url.endsWith('/v2/checkout/orders')) { sent = JSON.parse(opt.body); return {ok:true,status:201,json:async()=>({id:'5O190127TN364715T'})}; }
  if (url.includes('/capture')) { if (url.includes('DECLINED1')) return {ok:false,status:422,json:async()=>({details:[{issue:'INSTRUMENT_DECLINED'}]})};
    return {ok:true,status:201,json:async()=>({id:'5O190127TN364715T',status:'COMPLETED',purchase_units:[{payments:{captures:[{id:'CAP1',status:'COMPLETED',amount:{value:'90.84'}}]}}]})}; }
};
const co = require(path.join(R,'netlify/functions/create-order.js')).handler;
const cap = require(path.join(R,'netlify/functions/capture-order.js')).handler;
const S = require(path.join(R,'netlify/lib/shared.js'));
// test values (independent of the real settings in tools/content_order.py)
Object.assign(S.CAT, {enabled: true, free: 10, max: 10, zones: [{id:'laval',name:'Laval',prefix:'H7',fee:15,min_bags:1},{id:'montreal',name:'Montréal',prefix:'H',fee:25,min_bags:2}]});
const contact = {nom:'Garage Test',entreprise:'Garage Test inc.',courriel:'a@b.ca',telephone:'4385551234',adresse:'100 boul. Test',ville:'Laval',code_postal:'h7n0g4'};
const ev = b => ({httpMethod:'POST', body:JSON.stringify(b)});
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m); if(!c) process.exitCode=1;};
(async()=>{
  let r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:2}],contact}));
  ok(r.statusCode===200 && JSON.parse(r.body).id==='5O190127TN364715T','create order 2 colour bags -> 200');
  const a = sent.purchase_units[0].amount, b=a.breakdown;
  // 2*32=64 + 15 delivery = 79 ; GST 3.95 ; QST 7.88 ; total 90.83
  console.log('   amount', a.value, 'items', b.item_total.value, 'ship', b.shipping.value, 'tax', b.tax_total.value);
  ok(a.value==='90.83' && b.item_total.value==='64.00' && b.shipping.value==='15.00' && b.tax_total.value==='11.83','totals 64 + 15 + GST 3.95 + QST 7.88 = 90.83');
  ok((+b.item_total.value + +b.shipping.value + +b.tax_total.value).toFixed(2)===a.value,'breakdown sums to total');
  ok(sent.purchase_units[0].shipping.address.postal_code==='H7N 0G4','postal normalised');
  ok(!JSON.stringify(sent).toLowerCase().includes('surcharge') && b.handling===undefined,'no payment-method fee in order');
  r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:6},{id:'ratine-blanc',qty:4}],contact})); const a2=sent.purchase_units[0].amount;
  ok(a2.breakdown.shipping.value==='0.00','10 bags -> free delivery'); console.log('   10 bags total', a2.value);
  for (const [label,b] of [['price tampering ignored (no price field accepted)',{lang:'fr',lines:[{id:'tshirt-couleur',qty:1,price:1}],contact}]]) { r=await co(ev(b)); ok(r.statusCode===200 && sent.purchase_units[0].items[0].unit_amount.value==='32.00',label); }
  const bad = [['qty 11 rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:11}],contact}],['0 bags rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:0}],contact}],
    ['fake product rejected',{lang:'fr',lines:[{id:'gold',qty:1}],contact}],['decimal qty rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:1.5}],contact}],
    ['negative qty rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:-3},{id:'ratine-blanc',qty:2}],contact}],
    ['duplicate line rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:9},{id:'tshirt-couleur',qty:9}],contact}],
    ['Rive-Sud postal J4K rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:1}],contact:{...contact,code_postal:'J4K 1A1'}}],
    ['bad email rejected',{lang:'fr',lines:[{id:'tshirt-couleur',qty:1}],contact:{...contact,courriel:'x'}}]];
  for (const [label,b] of bad) { r=await co(ev(b)); ok(r.statusCode===400,label+' ('+JSON.parse(r.body).error+')'); }
  const mtl = {...contact, ville:'Montréal', code_postal:'H2X 1Y4'};
  r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:2}],contact:mtl})); const a3=sent.purchase_units[0].amount;
  // 64 + 25 = 89 ; GST 4.45 ; QST 8.88 ; total 102.33
  ok(r.statusCode===200 && a3.breakdown.shipping.value==='25.00' && a3.value==='102.33','Montréal 2 bags -> 25 delivery, total 102.33');
  r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:1}],contact:mtl})); ok(r.statusCode===400 && JSON.parse(r.body).error==='min','Montréal 1 bag rejected (min 2)');
  r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:1}],contact})); ok(r.statusCode===200 && sent.purchase_units[0].amount.breakdown.shipping.value==='15.00','Laval 1 bag -> 15 delivery');
  r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:2}],contact:{...contact,ville:'Montréal'}})); ok(r.statusCode===400 && JSON.parse(r.body).error==='city','Montréal city + Laval postal rejected (city)');
  r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:2}],contact:{...mtl,ville:'Laval'}})); ok(r.statusCode===400 && JSON.parse(r.body).error==='city','Laval city + Montréal postal rejected (city)');
  r = await co({httpMethod:'GET'}); ok(r.statusCode===405,'GET rejected');
  r = await cap(ev({orderID:'5O190127TN364715T'})); const d=JSON.parse(r.body); ok(r.statusCode===200 && d.status==='COMPLETED' && d.capture_id==='CAP1','capture ok');
  r = await cap(ev({orderID:'DECLINED1XYZ'})); ok(r.statusCode===422 && JSON.parse(r.body).issue==='INSTRUMENT_DECLINED','declined card -> restart signal');
  r = await cap(ev({orderID:'../../evil'})); ok(r.statusCode===400,'bad order id rejected');
  delete process.env.PAYPAL_CLIENT_SECRET; r = await co(ev({lang:'fr',lines:[{id:'tshirt-couleur',qty:1}],contact})); ok(r.statusCode===502,'missing secret -> 502, no crash');
})();
