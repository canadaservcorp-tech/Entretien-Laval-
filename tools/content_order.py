"""Online ordering (PayPal) for Laval + Montréal: settings and page text.

LEGAL NOTE: no PayPal/card fee is added to the customer's bill.
- PayPal's user agreement ("No surcharges") forbids charging a fee for paying with PayPal.
- Québec's Consumer Protection Act forbids card surcharges to consumers.
GST and QST are added (required). The delivery fee is the same whatever the payment method.
"""

CHECKOUT = {
    # ---- Hicham sets these ----
    # Delivery zones, matched by postal-code prefix (first match wins). Fee in CAD before tax.
    "zones": [
        {"id": "laval", "name": "Laval", "prefix": "H7", "fee": 15, "min_bags": 1},
        {"id": "montreal", "name": "Montréal", "prefix": "H", "fee": 25, "min_bags": 2},
    ],
    "free_delivery_from": None,  # number of bags from which delivery is free, or None for never
    "max_bags": 10,              # most bags per online order; bigger orders go through the quote form
    "paypal_client_id": "",      # PUBLIC Client ID from developer.paypal.com (sandbox one while testing). The SECRET never goes here.
    # ---- fixed ----
    "gst": 0.05,                 # TPS
    "qst": 0.09975,              # TVQ
    "postal_regex": r"^H\d[A-Z] ?\d[A-Z]\d$",  # H = Montréal island + Laval
}

def ready():
    return bool(CHECKOUT["zones"]) and bool(CHECKOUT["paypal_client_id"])

PAGE = {"kind": "order", "img": None, "rel": ["couleur", "blancs", "gros"],
 "fr": {"path": "/commander/", "short": "Commander en ligne",
  "title": "Commander des guenilles en ligne – Laval, Montréal | Chiffons ÉCO",
  "desc": "Commandez vos chiffons d'essuyage recyclés en ligne : sacs de 25 lb dès 32 $, TPS et TVQ incluses au paiement, livrés à Laval et Montréal.",
  "eyebrow": "Commande en ligne · Laval et Montréal", "h1": "Commander des chiffons en ligne",
  "lede": "Choisissez vos sacs, entrez votre adresse de livraison et payez par PayPal ou carte de crédit. Pour les autres régions ou les grosses commandes, demandez une soumission.",
  "card": "Payez en ligne par PayPal ou carte, livré à Laval et Montréal.",
  "body": """<h2>Comment ça fonctionne</h2>
<ol><li>Choisissez les produits et le nombre de [packs].</li><li>Entrez vos coordonnées et votre adresse à Laval ou Montréal (code postal commençant par H).</li><li>Payez par PayPal ou par carte de crédit ou débit, sans compte PayPal.</li><li>Nous vous contactons pour fixer la date de livraison.</li></ol>
<h2>Livraison</h2>
<p>[delivery]</p>
<h2>Prix et taxes</h2>
<p>Les prix sont affichés avant taxes. La TPS (5 %) et la TVQ (9,975 %) sont calculées sur les produits et la livraison, et affichées avant le paiement. Le prix est le même quel que soit le mode de paiement. Vous recevez une facture d'entreprise enregistrée.</p>
<h2>Autres régions, grosses commandes, virement Interac</h2>
<p>Hors Laval et Montréal, pour plus de [max] [packs], ou pour payer par virement Interac, <a href="{{home#devis}}">demandez une soumission</a> ou appelez le 438-831-3611.</p>""",
  "faq": [("Dois-je avoir un compte PayPal?", "Non. Le bouton carte permet de payer par carte de crédit ou de débit sans compte PayPal."),
          ("Quand suis-je livré?", "Nous vous contactons après le paiement pour fixer la date de livraison à votre adresse à Laval ou Montréal."),
          ("Combien coûte la livraison?", "[delivery]"),
          ("Y a-t-il des frais pour payer en ligne?", "Non. Vous payez le prix des produits, la livraison et les taxes, comme pour une commande par soumission.")]},
 "en": {"path": "/en/order/", "short": "Order online",
  "title": "Order wiping rags online – Laval, Montreal | ECO Rags",
  "desc": "Order recycled wiping rags online: 25 lb bags from $32, GST and QST shown at checkout, delivered in Laval and Montreal. Pay with PayPal or card.",
  "eyebrow": "Online order · Laval and Montreal", "h1": "Order rags online",
  "lede": "Pick your bags, enter your delivery address and pay with PayPal or a credit card. For other regions or large orders, request a quote.",
  "card": "Pay online with PayPal or card, delivered in Laval and Montreal.",
  "body": """<h2>How it works</h2>
<ol><li>Choose the products and the number of [packs].</li><li>Enter your contact details and your Laval or Montréal address (postal code starting with H).</li><li>Pay with PayPal, or with a credit or debit card without a PayPal account.</li><li>We contact you to set the delivery date.</li></ol>
<h2>Delivery</h2>
<p>[delivery]</p>
<h2>Prices and taxes</h2>
<p>Prices are shown before tax. GST (5%) and QST (9.975%) are calculated on the products and delivery and shown before you pay. The price is the same whatever the payment method. You get a registered business invoice.</p>
<h2>Other regions, large orders, Interac e-Transfer</h2>
<p>Outside Laval and Montréal, for more than [max] [packs], or to pay by Interac e-Transfer, <a href="{{home#devis}}">request a quote</a> or call 438-831-3611.</p>""",
  "faq": [("Do I need a PayPal account?", "No. The card button lets you pay with a credit or debit card without a PayPal account."),
          ("When is it delivered?", "We contact you after payment to set the delivery date at your Laval or Montréal address."),
          ("How much is delivery?", "[delivery]"),
          ("Is there a fee for paying online?", "No. You pay the product price, delivery and taxes, the same as an order by quote.")]}}

def _delivery(lang):
    out = []
    for i, z in enumerate(CHECKOUT["zones"]):
        fee = f"{z['fee']} $" if lang == "fr" else f"${z['fee']}"
        pc = (f"code postal {z['prefix']}" if lang == "fr" else f"postal code {z['prefix']}") if i == 0 else \
             ("autres codes postaux en H" if lang == "fr" else "other H postal codes")
        if lang == "fr":
            mn = "dès 1 sac" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} sacs"
            out.append(f"{z['name']} ({pc}) : {fee} par commande, {mn}")
        else:
            mn = "from 1 bag" if z["min_bags"] <= 1 else f"minimum {z['min_bags']} bags"
            out.append(f"{z['name']} ({pc}): {fee} per order, {mn}")
    return ". ".join(out) + (". Taxes en sus." if lang == "fr" else ". Plus tax.")

for _l in ("fr", "en"):
    PAGE[_l]["body"] = PAGE[_l]["body"].replace("[max]", str(CHECKOUT["max_bags"])).replace("[delivery]", _delivery(_l))
    PAGE[_l]["faq"] = [(q, a.replace("[delivery]", _delivery(_l))) for q, a in PAGE[_l]["faq"]]

UI = {
 "fr": {"qty": "Nombre de sacs", "contact_h": "Vos coordonnées et l'adresse de livraison", "name": "Nom", "company": "Entreprise", "email": "Courriel",
        "phone": "Téléphone", "address": "Adresse (numéro, rue, local)", "city": "Ville", "postal": "Code postal", "notes": "Instructions de livraison",
        "sum_h": "Votre commande", "goods": "Produits", "delivery": "Livraison", "free": "Gratuite", "gst": "TPS (5 %)", "qst": "TVQ (9,975 %)", "total": "Total",
        "e_bags": "Choisissez entre 1 et {max} sacs.", "e_fields": "Remplissez les champs obligatoires.", "e_min": "Minimum {min} sacs pour une livraison à {zone}.", "e_postal": "La commande en ligne est offerte à Laval et Montréal seulement (code postal commençant par H). Pour une autre région, demandez une soumission.",
        "e_pay": "Le paiement n'a pas pu être complété. Aucun montant n'a été prélevé. Réessayez ou appelez le 438-831-3611.",
        "e_after": "Paiement reçu, mais la confirmation n'a pas pu être envoyée. Notez ce numéro et appelez le 438-831-3611 : ",
        "note": "Prix avant taxes. TPS et TVQ ajoutées. Aucuns frais selon le mode de paiement.", "pay_h": "Paiement"},
 "en": {"qty": "Number of bags", "contact_h": "Your details and delivery address", "name": "Name", "company": "Company", "email": "Email",
        "phone": "Phone", "address": "Address (number, street, unit)", "city": "City", "postal": "Postal code", "notes": "Delivery instructions",
        "sum_h": "Your order", "goods": "Products", "delivery": "Delivery", "free": "Free", "gst": "GST (5%)", "qst": "QST (9.975%)", "total": "Total",
        "e_bags": "Choose between 1 and {max} bags.", "e_fields": "Please fill in the required fields.", "e_min": "Minimum {min} bags for delivery in {zone}.", "e_postal": "Online ordering is for Laval and Montréal only (postal code starting with H). For another region, request a quote.",
        "e_pay": "The payment could not be completed. Nothing was charged. Try again or call 438-831-3611.",
        "e_after": "Payment received, but the confirmation could not be sent. Note this number and call 438-831-3611: ",
        "note": "Prices before tax. GST and QST added. No fee based on payment method.", "pay_h": "Payment"},
}
