# Site content. Placeholders: {{page-key}} or {{page-key#anchor}} -> URL in the page's language,
# [pack] / [packs] -> packaging unit, [phone] -> phone number.
SITE = "https://entretienlaval.ca"
PHONE = "438-831-3611"
TEL = "tel:+14388313611"
EMAIL = "info@entretienlaval.ca"
PACK = {"fr": ("sac de 25 lb", "sacs de 25 lb"), "en": ("25 lb bag", "25 lb bags")}
GOOGLE_SITE_VERIFICATION = ""  # paste the token from Search Console > Settings > Ownership > HTML tag
INDEXNOW_KEY = "7c1e4b9a2d6f4e0b8a35c9d1f2e7b604"

PRODUCTS = [
    {"id": "tshirt-couleur", "price": 32, "page": "couleur",
     "fr": ("Chiffons t-shirt couleur", "T-SHIRT · COULEUR", "Notre plus populaire. Jersey de coton doux et très absorbant, pour l'usage général."),
     "en": ("Colored T-shirt rags", "T-SHIRT · COLORED", "Our most popular. Soft, very absorbent cotton jersey for general use.")},
    {"id": "ratine-couleur", "price": 32, "page": "couleur",
     "fr": ("Chiffons ratine couleur", "RATINE · COULEUR", "Tissu éponge épais et très résistant. Pour l'huile, la graisse et les gros dégâts."),
     "en": ("Colored terry rags", "TERRY · COLORED", "Thick, tough terry cloth. For oil, grease and big spills.")},
    {"id": "ratine-blanc", "price": 42, "page": "blancs",
     "fr": ("Chiffons ratine blanc", "RATINE · BLANC", "Ratine blanche de qualité supérieure, sans transfert de couleur."),
     "en": ("White terry rags", "TERRY · WHITE", "Premium white terry cloth, no color transfer.")},
    {"id": "tshirt-blanc", "price": 42, "page": "blancs",
     "fr": ("Chiffons t-shirt blanc", "T-SHIRT · BLANC", "Coton blanc sans transfert de couleur : finition, peinture et surfaces délicates."),
     "en": ("White T-shirt rags", "T-SHIRT · WHITE", "White cotton, no color transfer: finishing, painting and delicate surfaces.")},
]

CITIES = ["Laval", "Montréal", "Longueuil", "Terrebonne", "Blainville", "Boisbriand", "Rive-Nord", "Rive-Sud"]

TERMS = {
 "fr": [("Prix avant taxes", "TPS et TVQ en sus, facture d'entreprise enregistrée."),
        ("Livraison à votre adresse", "Frais selon votre emplacement, indiqués dans la soumission."),
        ("Hors Laval et Montréal", "Minimum de 1 000 lb (40 sacs) par livraison."),
        ("Quantité illimitée", "Commande confirmée et payée une semaine avant la livraison.")],
 "en": [("Prices before tax", "GST and QST extra, invoiced by a registered business."),
        ("Delivered to your address", "Fee depends on your location and is stated in the quote."),
        ("Outside Laval and Montréal", "1,000 lb minimum (40 bags) per delivery."),
        ("Unlimited quantity", "Order confirmed and paid one week before delivery.")],
}

UI = {
 "fr": {"home": "Accueil", "wa_fab": "Courriel", "skip": "Aller au contenu", "menu": "Menu", "call": "Nous écrire",
        "quote": "Demander une soumission", "call_btn": "Appeler", "sectors": "Secteurs", "products": "Produits",
        "guides": "Guides", "info": "Infos", "more": "En savoir plus →", "read": "Lire le guide →",
        "faq_h": "Questions fréquentes", "related": "À voir aussi", "prices_h": "Prix par [pack]",
        "prices_note": "Prix avant taxes. Livraison selon l'emplacement.", "see_all_faq": "Toutes les questions →",
        "cta_h": "Besoin de chiffons pour votre entreprise?", "cta_p": "Soumission rapide, échantillons sur demande, livraison à votre adresse.",
        "foot_tag": "Chiffons d'essuyage en textiles recyclés, triés et conditionnés à Laval, Québec.",
        "nav_label": "Navigation principale", "lang_name": "English", "crumbs": "Fil d'Ariane",
        "updated": "Mis à jour", "unit": "/ [pack]", "delivery_to": "Livraison :"},
 "en": {"home": "Home", "wa_fab": "Email", "skip": "Skip to content", "menu": "Menu", "call": "Email us",
        "quote": "Request a quote", "call_btn": "Call", "sectors": "Industries", "products": "Products",
        "guides": "Guides", "info": "Info", "more": "Learn more →", "read": "Read the guide →",
        "faq_h": "Frequently asked questions", "related": "See also", "prices_h": "Price per [pack]",
        "prices_note": "Prices before tax. Delivery depends on location.", "see_all_faq": "All questions →",
        "cta_h": "Need rags for your business?", "cta_p": "Fast quote, samples on request, delivered to your address.",
        "foot_tag": "Wiping rags made from recycled textiles, sorted and packed in Laval, Québec.",
        "nav_label": "Main navigation", "lang_name": "Français", "crumbs": "Breadcrumb",
        "updated": "Updated", "unit": "/ [pack]", "delivery_to": "Delivery:"},
}

NAV = {
 "fr": [("Produits", "home#produits"), ("Secteurs", "secteurs"), ("En gros", "gros"), ("Livraison", "livraison"), ("Guides", "guides"), ("FAQ", "faq")],
 "en": [("Products", "home#produits"), ("Industries", "secteurs"), ("Wholesale", "gros"), ("Delivery", "livraison"), ("Guides", "guides"), ("FAQ", "faq")],
}

SECTOR_KEYS = ["garage", "peinture", "entretien", "construction", "restauration", "industrie", "gros"]

# ---------------- FAQ (shared: /faq/ page, first 6 on homepage) ----------------
FAQ = {
 "fr": [
  ("Combien coûtent vos chiffons?", "32 $ le [pack] pour les chiffons couleur (t-shirt ou ratine) et 42 $ pour les blancs (t-shirt ou ratine), avant taxes. La livraison est en sus et dépend de votre emplacement. Voir <a href=\"{{home#produits}}\">les produits</a>."),
  ("Qu'y a-t-il dans un [pack]?", "25 lb de chiffons de coton recyclé d'un seul type : t-shirt ou ratine, blanc ou couleur. Les chiffons sont lavés, triés et traités contre les punaises de lit."),
  ("Quelle différence entre t-shirt et ratine?", "Le t-shirt (jersey) est mince, doux et souple : idéal pour l'usage général, les mains et les surfaces délicates. La ratine (tissu éponge) est épaisse et absorbe davantage : idéale pour l'huile, la graisse et les gros dégâts."),
  ("Blanc ou couleur?", "Le blanc ne transfère pas de couleur : pour la peinture, la finition, le vernis et les surfaces claires. La couleur coûte moins cher et convient à l'essuyage de tous les jours au garage, à l'atelier et sur les chantiers."),
  ("Livrez-vous? Où?", "Oui, à votre adresse : Laval, Montréal, Longueuil, Terrebonne, Blainville, Boisbriand et le reste du Grand Montréal. Ailleurs au Québec, nous livrons à partir de 1 000 lb par livraison. Les frais dépendent de l'emplacement. Voir <a href=\"{{livraison}}\">la livraison</a>."),
  ("Comment commander?", "Remplissez le <a href=\"{{home#devis}}\">formulaire de soumission</a> ou écrivez à info@entretienlaval.ca. La commande est confirmée et payée une semaine avant la livraison."),
  ("Y a-t-il un minimum de commande?", "Hors Laval et Montréal, le minimum est de 1 000 lb (40 sacs) par livraison. Pour le Grand Montréal, demandez-nous les conditions selon votre secteur."),
  ("Les chiffons sont-ils propres?", "Oui. Chaque lot est lavé et traité contre les punaises de lit avant d'être trié et emballé à Laval."),
  ("Offrez-vous des échantillons?", "Oui, sur demande, pour vérifier la qualité et le format avant une première commande."),
  ("Pouvez-vous fournir de grandes quantités?", "Oui, la quantité est illimitée. Nous approvisionnons aussi les distributeurs sanitaires et les fournisseurs industriels. Voir <a href=\"{{gros}}\">guenilles en gros</a>."),
  ("Recevrai-je une facture avec taxes?", "Oui. Entretien Laval est une entreprise enregistrée au Québec (NEQ 2280629637, TPS et TVQ). Les prix affichés sont avant taxes."),
  ("Peut-on utiliser les chiffons avec de l'huile ou des solvants?", "Oui, le coton absorbe l'huile, la graisse et les solvants. Après usage, rangez les chiffons imbibés dans un contenant métallique fermé : voir notre guide <a href=\"{{guide-huileux}}\">chiffons huileux et risque d'incendie</a>."),
  ("D'où viennent les textiles?", "De vêtements et textiles de coton récupérés qui seraient autrement envoyés à l'enfouissement. Ils sont triés par type et par couleur, coupés et emballés à Laval."),
 ],
 "en": [
  ("How much do your rags cost?", "$32 per [pack] for colored rags (T-shirt or terry) and $42 for white (T-shirt or terry), before tax. Delivery is extra and depends on your location. See <a href=\"{{home#produits}}\">products</a>."),
  ("What's in a [pack]?", "25 lb of recycled cotton rags of a single type: T-shirt or terry, white or colored. The rags are washed, sorted and treated against bedbugs."),
  ("What's the difference between T-shirt and terry?", "T-shirt (jersey) is thin, soft and flexible: ideal for general use, hands and delicate surfaces. Terry (towel cloth) is thick and absorbs more: ideal for oil, grease and big spills."),
  ("White or colored?", "White doesn't transfer color: for painting, finishing, varnish and light surfaces. Colored costs less and suits everyday wiping in garages, shops and job sites."),
  ("Do you deliver? Where?", "Yes, to your address: Laval, Montréal, Longueuil, Terrebonne, Blainville, Boisbriand and the rest of Greater Montreal. Elsewhere in Québec we deliver from 1,000 lb per delivery. The fee depends on the location. See <a href=\"{{livraison}}\">delivery</a>."),
  ("How do I order?", "Fill in the <a href=\"{{home#devis}}\">quote form</a> or email info@entretienlaval.ca. Orders are confirmed and paid one week before delivery."),
  ("Is there a minimum order?", "Outside Laval and Montréal, the minimum is 1,000 lb (40 bags) per delivery. For Greater Montreal, ask us about the terms for your area."),
  ("Are the rags clean?", "Yes. Every lot is washed and treated against bedbugs before being sorted and packed in Laval."),
  ("Do you offer samples?", "Yes, on request, so you can check quality and size before a first order."),
  ("Can you supply large volumes?", "Yes, quantity is unlimited. We also supply janitorial distributors and industrial suppliers. See <a href=\"{{gros}}\">wholesale rags</a>."),
  ("Will I get an invoice with taxes?", "Yes. Entretien Laval is a registered Québec business (NEQ 2280629637, GST and QST). Listed prices are before tax."),
  ("Can the rags be used with oil or solvents?", "Yes, cotton absorbs oil, grease and solvents. After use, store soaked rags in a closed metal container: see our guide <a href=\"{{guide-huileux}}\">oily rags and fire risk</a>."),
  ("Where do the textiles come from?", "From recovered cotton clothing and textiles that would otherwise go to landfill. They are sorted by type and color, cut and packed in Laval."),
 ],
}

HOME = {
 "fr": {"path": "/", "title": "Guenilles et chiffons d'essuyage recyclés à Laval | Chiffons ÉCO",
        "desc": "Guenilles et chiffons d'essuyage en coton recyclé, lavés et traités anti-punaises, dès 32 $ le sac de 25 lb. Triés à Laval, livrés partout au Québec.",
        "prod_eyebrow": "Nos chiffons · 4 produits", "prod_h2": "T-shirt ou ratine, blanc ou couleur.",
        "prod_p": "Tous lavés, triés et traités contre les punaises de lit, en [packs]. Échantillons sur demande.",
        "photo_alt": ["Sacs de 25 lb de chiffons recyclés couleur, scellés", "Sac de chiffons t-shirt couleur de 25 lb"],
        "sec_eyebrow": "Secteurs", "sec_h2": "Fait pour ceux qui salissent leurs mains.",
        "sec_p": "Choisissez votre secteur : quel chiffon prendre, comment l'utiliser et quoi faire après.",
        "del_eyebrow": "Livraison", "del_h2": "Livré à votre adresse.",
        "del_p": "Partout dans le Grand Montréal, et ailleurs au Québec à partir de 1 000 lb. Les frais dépendent de votre emplacement.",
        "del_link": "Zones et conditions de livraison →",
        "faq_eyebrow": "FAQ", "faq_h2": "Vos questions, nos réponses.",
        "devis_eyebrow": "Soumission", "devis_h2": "Prix, échantillons et commandes.",
        "form_h": "Demande de soumission", "form_sub": "Réponse rapide par courriel ou téléphone, avec le prix livré à votre adresse.",
        "f_name": "Nom", "f_company": "Entreprise", "f_email": "Courriel", "f_phone": "Téléphone", "f_city": "Ville de livraison",
        "f_product": "Produit", "f_any": "Je ne sais pas encore", "f_qty": "Quantité (nombre de sacs)", "f_msg": "Message",
        "f_send": "Envoyer la demande", "f_fine": "Vos coordonnées servent uniquement à répondre à votre demande.",
        "ready_h": "Vous préférez parler à quelqu'un?", "ready_p": "Appelez-nous ou écrivez-nous. Livraison dans le Grand Montréal et au Québec.",
        "c_email_btn": "Écrire un courriel", "c_wa_btn": "Écrire sur WhatsApp", "c_call_btn": "Nous écrire",
        "lbl": {"phone": "Téléphone", "mail": "Courriel", "wa": "WhatsApp", "ig": "Instagram", "pin": "Adresse", "biz": "Entreprise"},
        "hero_cta1": "Demander une soumission", "hero_cta2": "Voir les prix"},
 "en": {"path": "/en/", "title": "Recycled wiping rags in Laval – 25 lb bags | ECO Rags",
        "desc": "Recycled cotton wiping rags and shop rags, washed and bedbug-treated, from $32 per 25 lb bag. Sorted in Laval, delivered across Greater Montreal and Québec.",
        "prod_eyebrow": "Our rags · 4 products", "prod_h2": "T-shirt or terry, white or colored.",
        "prod_p": "All washed, sorted and treated against bedbugs, in [packs]. Samples on request.",
        "photo_alt": ["Sealed 25 lb bags of colored recycled rags", "25 lb bag of colored T-shirt rags"],
        "sec_eyebrow": "Industries", "sec_h2": "Made for people who get their hands dirty.",
        "sec_p": "Pick your industry: which rag to use, how to use it and what to do after.",
        "del_eyebrow": "Delivery", "del_h2": "Delivered to your address.",
        "del_p": "Anywhere in Greater Montreal, and elsewhere in Québec from 1,000 lb. The fee depends on your location.",
        "del_link": "Delivery areas and terms →",
        "faq_eyebrow": "FAQ", "faq_h2": "Your questions, answered.",
        "devis_eyebrow": "Quote", "devis_h2": "Prices, samples and orders.",
        "form_h": "Request a quote", "form_sub": "Fast reply by email or phone, with the delivered price to your address.",
        "f_name": "Name", "f_company": "Company", "f_email": "Email", "f_phone": "Phone", "f_city": "Delivery city",
        "f_product": "Product", "f_any": "Not sure yet", "f_qty": "Quantity (number of bags)", "f_msg": "Message",
        "f_send": "Send request", "f_fine": "Your details are only used to answer your request.",
        "ready_h": "Prefer to talk to someone?", "ready_p": "Call or email us. Delivery across Greater Montreal and Québec.",
        "c_email_btn": "Send an email", "c_wa_btn": "Message on WhatsApp", "c_call_btn": "Email us",
        "lbl": {"phone": "Phone", "mail": "Email", "wa": "WhatsApp", "ig": "Instagram", "pin": "Address", "biz": "Business"},
        "hero_cta1": "Request a quote", "hero_cta2": "See prices"},
}

IMG_BAG = "sac-chiffons-t-shirt-couleur-25-lb.webp"
IMG_BAGS = "sacs-chiffons-couleur-25-lb.webp"
IMG_BALE = "balle-compressee-de-chiffons-eco-en-textiles-recyc.webp"
IMG_TEXT = "textiles-de-coton-recuperes.webp"
IMG_SHOP = "sac-de-chiffons-d-atelier-conditionnes-prets-a-l-u.webp"
IMG_SYM = "symbole-de-recyclage-forme-de-textiles-colores.webp"
IMG_CLOTH = "vetements-colores-et-symbole-de-recyclage-mode-cir.webp"

PAGES = {}

PAGES["garage"] = {"kind": "sector", "img": IMG_BAG, "rel": ["couleur", "guide-huileux", "industrie"],
 "fr": {"path": "/chiffons-garage-mecanique/", "short": "Garages et mécanique",
  "title": "Chiffons de garage et guenilles d'atelier – Laval, Montréal",
  "desc": "Guenilles recyclées pour garages et mécanique : huile, graisse, liquides. Dès 32 $ le sac de 25 lb, livrées à Laval, Montréal et partout au Québec.",
  "eyebrow": "Garages · mécanique · carrosserie", "h1": "Chiffons de garage et guenilles pour la mécanique",
  "lede": "Des chiffons de coton recyclé qui absorbent l'huile, la graisse et les liquides, en [packs]. Pour garages, ateliers mécaniques, carrosseries et concessionnaires.",
  "card": "Huile, graisse, liquides, mains et outils : la ratine et le t-shirt couleur font le travail.",
  "alt": "Sac de 25 lb de chiffons recyclés pour garage",
  "body": """<h2>Pourquoi des chiffons recyclés au garage</h2>
<p>Au garage, on essuie sans arrêt : mains, outils, jauges, pièces, déversements. Le papier se déchire dès qu'il est imbibé d'huile. Un chiffon de coton absorbe davantage, reste solide et coûte moins cher à l'usage.</p>
<ul><li><b>Huile et graisse</b> : la ratine (tissu éponge) est épaisse et retient beaucoup de liquide.</li>
<li><b>Usage général</b> : le t-shirt couleur, doux et souple, pour les mains, les outils et le nettoyage courant.</li>
<li><b>Surfaces peintes</b> : le blanc, sans transfert de couleur, pour l'esthétique automobile et les retouches.</li></ul>
<h2>Quel chiffon choisir</h2>
<p>Pour la plupart des garages, le <a href="{{couleur}}">chiffon couleur</a> offre le meilleur rapport qualité-prix : 32 $ le [pack]. Prenez la ratine pour les gros dégâts d'huile, et gardez quelques sacs de <a href="{{blancs}}">chiffons blancs</a> pour la carrosserie et les finis délicats.</p>
<h2>Sécurité : les chiffons huileux</h2>
<p>Rangez les chiffons imbibés d'huile, de solvant ou d'essence dans un contenant métallique fermé, jamais en tas dans un coin. Voir le guide <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>
<h2>Livraison aux garages</h2>
<p>Nous livrons les garages de Laval, Montréal, Longueuil, Terrebonne, Blainville, Boisbriand et du reste du Grand Montréal. Ailleurs au Québec, voir les <a href="{{livraison}}">conditions de livraison</a>.</p>""",
  "faq": [("Combien de chiffons y a-t-il dans un [pack]?", "Nous vendons au poids, car la taille des morceaux varie. Demandez un échantillon pour juger du format avant de commander."),
          ("Les chiffons laissent-ils des peluches?", "Le coton recyclé trié est peu pelucheux. Pour les surfaces peintes ou vernies, choisissez le t-shirt blanc."),
          ("Peut-on laver et réutiliser les chiffons?", "Les chiffons légèrement sales peuvent être lavés. Ceux imbibés d'huile ou de solvant ne doivent pas aller dans une sécheuse domestique, à cause du risque d'incendie : faites-les traiter par un service spécialisé ou jetez-les de façon sécuritaire.")]},
 "en": {"path": "/en/shop-rags-garage-mechanics/", "short": "Garages and mechanics",
  "title": "Shop rags for garages and mechanics – Laval, Montreal",
  "desc": "Recycled shop rags for garages and auto repair: oil, grease, fluids. From $32 per 25 lb bag, delivered in Laval, Montreal and across Québec.",
  "eyebrow": "Garages · auto repair · body shops", "h1": "Shop rags for garages and mechanics",
  "lede": "Recycled cotton rags that soak up oil, grease and fluids, in [packs]. For garages, repair shops, body shops and dealerships.",
  "card": "Oil, grease, fluids, hands and tools: colored terry and T-shirt rags do the job.",
  "alt": "25 lb bag of recycled shop rags for garages",
  "body": """<h2>Why recycled rags in the shop</h2>
<p>In a garage you wipe all day: hands, tools, dipsticks, parts, spills. Paper tears as soon as it's soaked with oil. A cotton rag absorbs more, stays strong and costs less per use.</p>
<ul><li><b>Oil and grease</b>: terry (towel cloth) is thick and holds a lot of liquid.</li>
<li><b>General use</b>: soft, flexible colored T-shirt rags for hands, tools and everyday cleanup.</li>
<li><b>Painted surfaces</b>: white rags, with no color transfer, for detailing and touch-ups.</li></ul>
<h2>Which rag to choose</h2>
<p>For most garages, <a href="{{couleur}}">colored rags</a> give the best value: $32 per [pack]. Use terry for big oil spills, and keep a few bags of <a href="{{blancs}}">white rags</a> for bodywork and delicate finishes.</p>
<h2>Safety: oily rags</h2>
<p>Store rags soaked with oil, solvent or gasoline in a closed metal container, never in a pile in a corner. See the guide <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>
<h2>Delivery to garages</h2>
<p>We deliver to garages in Laval, Montréal, Longueuil, Terrebonne, Blainville, Boisbriand and the rest of Greater Montreal. Elsewhere in Québec, see the <a href="{{livraison}}">delivery terms</a>.</p>""",
  "faq": [("How many rags are in a [pack]?", "We sell by weight because piece sizes vary. Ask for a sample to judge the size before you order."),
          ("Do the rags leave lint?", "Sorted recycled cotton is low-lint. For painted or varnished surfaces, choose white T-shirt rags."),
          ("Can rags be washed and reused?", "Lightly soiled rags can be washed. Rags soaked with oil or solvent must not go in a home dryer because of the fire risk: use a specialized service or dispose of them safely.")]},
}

PAGES["peinture"] = {"kind": "sector", "img": IMG_SHOP, "rel": ["blancs", "guide-huileux", "construction"],
 "fr": {"path": "/chiffons-peinture-finition/", "short": "Peinture et finition",
  "title": "Chiffons blancs pour peintres, teinture et vernis – Québec",
  "desc": "Chiffons de coton blanc recyclé sans transfert de couleur pour peintres et ébénistes : teinture, vernis, huile. Sacs de 25 lb à 42 $, livrés au Québec.",
  "eyebrow": "Peintres · ébénistes · finition", "h1": "Chiffons pour la peinture, la teinture et la finition",
  "lede": "Du coton blanc trié, sans transfert de couleur, pour appliquer et essuyer la teinture, l'huile et le vernis sans marquer vos surfaces.",
  "card": "Teinture, vernis et retouches : le coton blanc ne transfère pas de couleur.",
  "alt": "Chiffons d'atelier conditionnés pour la finition",
  "body": """<h2>Le blanc pour la finition</h2>
<p>Pour appliquer une teinture, essuyer un surplus d'huile ou nettoyer un pinceau, il faut un chiffon qui ne déteint pas. Nos <a href="{{blancs}}">chiffons blancs</a> sont triés pour ne laisser aucune couleur sur le bois, le métal ou la peinture fraîche.</p>
<ul><li><b>T-shirt blanc</b> : mince et doux, pour la teinture, le vernis, le polissage et les surfaces délicates.</li>
<li><b>Ratine blanche</b> : plus épaisse, pour les dégâts, le nettoyage des outils et les gros surplus.</li>
<li><b>Couleur</b> : pour le ménage du chantier, les mains et les échelles, à moindre coût.</li></ul>
<h2>Pour qui</h2>
<p>Peintres en bâtiment, ébénistes, finisseurs de meubles et d'armoires, restaurateurs de meubles, carrossiers et ateliers de peinture industrielle.</p>
<h2>Attention aux chiffons de teinture et d'huile</h2>
<div class="note"><p>Les chiffons imbibés d'huile de lin, d'huile de tung ou de teinture à l'huile peuvent <b>s'enflammer d'eux-mêmes</b> en séchant. Ne les laissez jamais en boule ou en tas. Étendez-les à plat à l'extérieur pour sécher, ou mettez-les dans un contenant métallique fermé rempli d'eau. Détails dans le guide <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p></div>
<h2>Prix et livraison</h2>
<p>Blanc : 42 $ le [pack], avant taxes. Livraison à votre atelier ou à l'adresse de votre choix, selon les <a href="{{livraison}}">conditions de livraison</a>.</p>""",
  "faq": [("T-shirt ou ratine pour la teinture?", "Le t-shirt blanc pour appliquer et essuyer la teinture (fin et régulier), la ratine blanche pour les gros surplus et le nettoyage."),
          ("Les chiffons couleur peuvent-ils tacher le bois?", "Avec des solvants, un tissu teint peut déteindre. Pour la finition, prenez du blanc."),
          ("Comment jeter un chiffon de teinture à l'huile?", "Faites-le sécher à plat à l'extérieur ou mettez-le dans un contenant métallique fermé avec de l'eau, puis apportez-le à l'écocentre comme résidu domestique dangereux (RDD).")]},
 "en": {"path": "/en/painting-finishing-rags/", "short": "Painting and finishing",
  "title": "White rags for painters, stain and varnish – Québec",
  "desc": "Recycled white cotton rags with no color transfer for painters, woodworkers and finishing: stain, varnish, oil. 25 lb bags at $42, delivered across Québec.",
  "eyebrow": "Painters · woodworkers · finishing", "h1": "Rags for painting, staining and finishing",
  "lede": "Sorted white cotton with no color transfer, to apply and wipe stain, oil and varnish without marking your surfaces.",
  "card": "Stain, varnish and touch-ups: white cotton doesn't transfer color.",
  "alt": "Packed shop rags for finishing work",
  "body": """<h2>White for finishing</h2>
<p>To apply stain, wipe off excess oil or clean a brush, you need a rag that won't bleed. Our <a href="{{blancs}}">white rags</a> are sorted so they leave no color on wood, metal or fresh paint.</p>
<ul><li><b>White T-shirt</b>: thin and soft, for stain, varnish, polishing and delicate surfaces.</li>
<li><b>White terry</b>: thicker, for spills, tool cleaning and heavy excess.</li>
<li><b>Colored</b>: for job-site cleanup, hands and ladders, at a lower cost.</li></ul>
<h2>Who it's for</h2>
<p>House painters, woodworkers, furniture and cabinet finishers, furniture restorers, body shops and industrial paint shops.</p>
<h2>Careful with stain and oil rags</h2>
<div class="note"><p>Rags soaked with linseed oil, tung oil or oil-based stain can <b>catch fire on their own</b> as they dry. Never leave them balled up or in a pile. Lay them flat outdoors to dry, or put them in a closed metal container filled with water. Details in the guide <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p></div>
<h2>Price and delivery</h2>
<p>White: $42 per [pack], before tax. Delivered to your shop or any address you choose, under our <a href="{{livraison}}">delivery terms</a>.</p>""",
  "faq": [("T-shirt or terry for staining?", "White T-shirt to apply and wipe stain (thin and even), white terry for heavy excess and cleanup."),
          ("Can colored rags stain wood?", "With solvents, dyed fabric can bleed. For finishing, choose white."),
          ("How do I dispose of an oil-stain rag?", "Dry it flat outdoors or put it in a closed metal container with water, then take it to your local eco-centre as household hazardous waste.")]},
}

PAGES["entretien"] = {"kind": "sector", "img": IMG_BAGS, "rel": ["gros", "guide-papier", "restauration"],
 "fr": {"path": "/chiffons-entretien-menager-conciergerie/", "short": "Entretien et conciergerie",
  "title": "Chiffons de nettoyage pour entretien ménager et conciergerie",
  "desc": "Chiffons de nettoyage en coton recyclé pour entreprises d'entretien ménager, concierges et gestionnaires d'immeubles. Sacs de 25 lb dès 32 $, Grand Montréal.",
  "eyebrow": "Entretien ménager · conciergerie · immeubles", "h1": "Chiffons de nettoyage pour l'entretien ménager et la conciergerie",
  "lede": "Des chiffons de coton recyclé lavés et traités, pour les équipes d'entretien, les concierges et les gestionnaires d'immeubles qui en passent beaucoup.",
  "card": "Équipes d'entretien, concierges et immeubles : du coton absorbant, moins de papier.",
  "alt": "Sacs scellés de chiffons de nettoyage recyclés",
  "body": """<h2>Des chiffons pour les équipes d'entretien</h2>
<p>Pour l'époussetage, les déversements, les planchers, les salles mécaniques et le ménage après travaux, un chiffon de coton absorbe plus que le papier et sert plus longtemps. Il réduit aussi les sacs de papier à la poubelle.</p>
<ul><li><b>T-shirt couleur</b> : usage général, poussière, surfaces et équipement.</li>
<li><b>Ratine</b> : planchers, gros déversements, salles mécaniques, garages d'immeubles.</li>
<li><b>Blanc</b> : là où l'on veut voir la saleté et éviter tout transfert de couleur.</li></ul>
<h2>Propres et sûrs pour vos clients</h2>
<p>Chaque lot est lavé et traité contre les punaises de lit avant le tri et l'emballage à Laval. Vous pouvez les apporter chez vos clients en toute confiance.</p>
<h2>Pour les volumes réguliers</h2>
<p>Entreprises d'entretien commercial, concierges, syndicats de copropriété, gestionnaires d'immeubles et distributeurs sanitaires : nous fournissons les quantités dont vous avez besoin. Voir aussi <a href="{{gros}}">guenilles en gros</a> et notre comparaison <a href="{{guide-papier}}">chiffons recyclés ou essuie-tout</a>.</p>""",
  "faq": [("Les chiffons conviennent-ils aux vitres?", "Pour les vitres et l'inox, le t-shirt blanc, mince et peu pelucheux, est le meilleur choix parmi nos produits."),
          ("Sont-ils compatibles avec les produits nettoyants?", "Oui, le coton supporte les nettoyants courants. Suivez toujours les consignes du fabricant du produit."),
          ("Livrez-vous chaque mois?", "Oui, nous pouvons planifier des livraisons régulières selon vos besoins. Demandez une soumission.")]},
 "en": {"path": "/en/janitorial-cleaning-rags/", "short": "Janitorial and cleaning",
  "title": "Cleaning rags for janitorial and building maintenance",
  "desc": "Recycled cotton cleaning rags for janitorial companies, custodians and property managers. 25 lb bags from $32, Laval and Greater Montreal.",
  "eyebrow": "Janitorial · custodial · buildings", "h1": "Cleaning rags for janitorial and building maintenance",
  "lede": "Washed and treated recycled cotton rags for cleaning crews, custodians and property managers who go through a lot of them.",
  "card": "Cleaning crews, custodians and buildings: absorbent cotton, less paper.",
  "alt": "Sealed bags of recycled cleaning rags",
  "body": """<h2>Rags for cleaning crews</h2>
<p>For dusting, spills, floors, mechanical rooms and post-renovation cleanup, a cotton rag absorbs more than paper and lasts longer. It also cuts down the bags of paper going in the trash.</p>
<ul><li><b>Colored T-shirt</b>: general use, dust, surfaces and equipment.</li>
<li><b>Terry</b>: floors, big spills, mechanical rooms, building garages.</li>
<li><b>White</b>: where you want to see the dirt and avoid any color transfer.</li></ul>
<h2>Clean and safe for your clients</h2>
<p>Every lot is washed and treated against bedbugs before sorting and packing in Laval, so you can bring them into your clients' buildings with confidence.</p>
<h2>For regular volumes</h2>
<p>Commercial cleaning companies, custodians, condo boards, property managers and janitorial distributors: we supply the quantities you need. See also <a href="{{gros}}">wholesale rags</a> and our comparison <a href="{{guide-papier}}">recycled rags vs paper towels</a>.</p>""",
  "faq": [("Are the rags good for windows?", "For glass and stainless steel, thin, low-lint white T-shirt rags are the best choice among our products."),
          ("Can I use them with cleaning products?", "Yes, cotton handles common cleaners. Always follow the product manufacturer's instructions."),
          ("Do you deliver monthly?", "Yes, we can schedule regular deliveries based on your needs. Ask for a quote.")]},
}

PAGES["construction"] = {"kind": "sector", "img": IMG_BALE, "rel": ["couleur", "gros", "peinture"],
 "fr": {"path": "/chiffons-construction-chantier/", "short": "Construction et chantiers",
  "title": "Guenilles pour chantiers de construction – livraison au Québec",
  "desc": "Guenilles recyclées pour entrepreneurs, plombiers, électriciens et chantiers : outils, colle, calfeutrage. Sacs de 25 lb dès 32 $, livrés sur place.",
  "eyebrow": "Entrepreneurs · plomberie · électricité", "h1": "Guenilles pour la construction et les chantiers",
  "lede": "Des chiffons solides et bon marché pour les outils, la colle, le calfeutrage, la plomberie et le ménage de fin de chantier, livrés en [packs].",
  "card": "Outils, colle, calfeutrage et ménage de fin de chantier, en gros volumes.",
  "alt": "Balle compressée de chiffons recyclés pour chantiers",
  "body": """<h2>Sur le chantier, on en use beaucoup</h2>
<p>Essuyer les outils, la colle et le scellant, nettoyer un joint de plomberie, protéger une surface, ramasser un déversement : un chantier passe vite à travers des sacs de guenilles. Les chiffons couleur sont le choix économique.</p>
<ul><li><b>T-shirt couleur</b> : calfeutrage, colle, outils, mains.</li>
<li><b>Ratine couleur</b> : huile, graisse, gros déversements, équipement lourd.</li>
<li><b>Blanc</b> : finition, peinture et surfaces visibles.</li></ul>
<h2>Pour qui</h2>
<p>Entrepreneurs généraux et spécialisés, plombiers, électriciens, frigoristes, couvreurs, poseurs de plancher et équipes de ménage après construction.</p>
<h2>Livraison au chantier</h2>
<p>Nous livrons à l'adresse de votre choix, au bureau, à l'entrepôt ou au chantier. Hors Laval et Montréal, minimum de 1 000 lb par livraison. Voir les <a href="{{livraison}}">conditions</a> ou demandez une <a href="{{home#devis}}">soumission</a>.</p>""",
  "faq": [("Pouvez-vous livrer directement au chantier?", "Oui, à l'adresse de votre choix, selon nos conditions de livraison."),
          ("Quel chiffon pour le silicone et le calfeutrage?", "Le t-shirt couleur : mince, souple et économique."),
          ("Facturez-vous les entrepreneurs?", "Oui, avec TPS et TVQ, sur facture d'entreprise enregistrée.")]},
 "en": {"path": "/en/construction-site-rags/", "short": "Construction sites",
  "title": "Rags for construction sites – delivered across Québec",
  "desc": "Recycled rags for contractors, plumbers, electricians and job sites: tools, glue, caulking, cleanup. 25 lb bags from $32, delivered to your address.",
  "eyebrow": "Contractors · plumbing · electrical", "h1": "Rags for construction and job sites",
  "lede": "Strong, low-cost rags for tools, glue, caulking, plumbing and end-of-job cleanup, delivered in [packs].",
  "card": "Tools, glue, caulking and end-of-job cleanup, in large volumes.",
  "alt": "Compressed bale of recycled rags for job sites",
  "body": """<h2>Job sites use a lot of them</h2>
<p>Wiping tools, glue and sealant, cleaning a plumbing joint, protecting a surface, catching a spill: a job site goes through bags of rags fast. Colored rags are the budget choice.</p>
<ul><li><b>Colored T-shirt</b>: caulking, glue, tools, hands.</li>
<li><b>Colored terry</b>: oil, grease, big spills, heavy equipment.</li>
<li><b>White</b>: finishing, painting and visible surfaces.</li></ul>
<h2>Who it's for</h2>
<p>General and specialty contractors, plumbers, electricians, HVAC technicians, roofers, flooring installers and post-construction cleaning crews.</p>
<h2>Delivery to the site</h2>
<p>We deliver to any address you choose: office, warehouse or job site. Outside Laval and Montréal, 1,000 lb minimum per delivery. See the <a href="{{livraison}}">terms</a> or request a <a href="{{home#devis}}">quote</a>.</p>""",
  "faq": [("Can you deliver straight to the job site?", "Yes, to any address you choose, under our delivery terms."),
          ("Which rag for silicone and caulking?", "Colored T-shirt: thin, flexible and economical."),
          ("Do you invoice contractors?", "Yes, with GST and QST, on a registered business invoice.")]},
}

PAGES["restauration"] = {"kind": "sector", "img": IMG_TEXT, "rel": ["entretien", "blancs", "guide-papier"],
 "fr": {"path": "/chiffons-restauration-cuisine/", "short": "Restaurants et cuisines",
  "title": "Chiffons pour restaurants et cuisines commerciales – Montréal",
  "desc": "Chiffons de coton recyclé pour l'entretien des restaurants : graisse, hottes, planchers, équipement. Lavés et traités, sacs de 25 lb, Laval et Grand Montréal.",
  "eyebrow": "Restaurants · traiteurs · cuisines", "h1": "Chiffons pour restaurants et cuisines commerciales",
  "lede": "Pour la graisse, les hottes, les planchers, l'équipement et les déversements : des chiffons de coton absorbants, lavés et traités.",
  "card": "Graisse, hottes, planchers et équipement : l'entretien de la cuisine, à moindre coût.",
  "alt": "Textiles de coton récupérés et triés",
  "body": """<h2>L'entretien de la cuisine</h2>
<p>Dans une cuisine commerciale, on essuie la graisse des hottes et des friteuses, l'équipement, les planchers et les déversements toute la journée. Le coton absorbe la graisse mieux que le papier.</p>
<ul><li><b>Ratine</b> : graisse, friteuses, hottes, planchers.</li>
<li><b>T-shirt blanc</b> : inox et surfaces où l'on veut voir la saleté.</li>
<li><b>T-shirt couleur</b> : ménage général, arrière-cuisine, entrepôt.</li></ul>
<h2>Hygiène</h2>
<p>Nos chiffons sont lavés et traités contre les punaises de lit. Ce sont des chiffons d'entretien : pour les surfaces en contact avec les aliments, suivez les règles du MAPAQ et votre procédure de nettoyage et d'assainissement.</p>
<h2>Graisse et risque d'incendie</h2>
<p>Les chiffons imbibés d'huile de cuisson ne doivent pas rester en tas, ni sortir chauds de la sécheuse. Voir le guide <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>""",
  "faq": [("Peut-on utiliser ces chiffons sur les comptoirs?", "Pour les surfaces en contact avec les aliments, utilisez des linges réservés à cet usage selon les règles du MAPAQ. Nos chiffons servent à l'entretien : graisse, planchers, équipement."),
          ("Quel chiffon pour la graisse?", "La ratine, épaisse et très absorbante."),
          ("Livrez-vous les restaurants de Montréal?", "Oui, à Montréal, Laval et dans le Grand Montréal.")]},
 "en": {"path": "/en/restaurant-kitchen-rags/", "short": "Restaurants and kitchens",
  "title": "Rags for restaurants and commercial kitchens – Montreal",
  "desc": "Recycled cotton rags for restaurant cleaning: grease, hoods, floors, equipment. Washed and treated, 25 lb bags, Laval and Greater Montreal.",
  "eyebrow": "Restaurants · caterers · kitchens", "h1": "Rags for restaurants and commercial kitchens",
  "lede": "For grease, hoods, floors, equipment and spills: absorbent cotton rags, washed and treated.",
  "card": "Grease, hoods, floors and equipment: kitchen cleaning at a lower cost.",
  "alt": "Recovered and sorted cotton textiles",
  "body": """<h2>Kitchen cleaning</h2>
<p>In a commercial kitchen you wipe grease from hoods and fryers, equipment, floors and spills all day. Cotton soaks up grease better than paper.</p>
<ul><li><b>Terry</b>: grease, fryers, hoods, floors.</li>
<li><b>White T-shirt</b>: stainless steel and surfaces where you want to see the dirt.</li>
<li><b>Colored T-shirt</b>: general cleaning, back of house, storage.</li></ul>
<h2>Hygiene</h2>
<p>Our rags are washed and treated against bedbugs. They are cleaning rags: for food-contact surfaces, follow MAPAQ rules and your cleaning and sanitizing procedure.</p>
<h2>Grease and fire risk</h2>
<p>Rags soaked with cooking oil must not stay in a pile or come out of the dryer hot. See the guide <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>""",
  "faq": [("Can these rags be used on counters?", "For food-contact surfaces, use dedicated cloths under MAPAQ rules. Our rags are for cleaning: grease, floors, equipment."),
          ("Which rag for grease?", "Terry, thick and very absorbent."),
          ("Do you deliver to Montreal restaurants?", "Yes, in Montréal, Laval and across Greater Montreal.")]},
}

PAGES["industrie"] = {"kind": "sector", "img": IMG_BALE, "rel": ["gros", "blancs", "guide-huileux"],
 "fr": {"path": "/chiffons-industriels-imprimerie/", "short": "Industrie et imprimerie",
  "title": "Chiffons industriels et chiffons d'imprimerie – Québec",
  "desc": "Chiffons industriels en coton recyclé pour usines, imprimeries et maintenance : encre, huile, solvants. Quantité illimitée, livraison partout au Québec.",
  "eyebrow": "Usines · imprimeries · maintenance", "h1": "Chiffons industriels et chiffons d'imprimerie",
  "lede": "Pour l'encre, l'huile de coupe, les solvants et l'entretien des machines : du coton recyclé en [packs], en quantité illimitée.",
  "card": "Encre, huile de coupe, solvants et entretien des machines, en quantité illimitée.",
  "alt": "Balle de chiffons industriels en textiles recyclés",
  "body": """<h2>Pour l'usine et l'atelier</h2>
<p>Ateliers d'usinage, usines, imprimeries, entrepôts et équipes de maintenance utilisent des chiffons pour l'huile de coupe, l'encre, les solvants, la graisse des machines et les déversements.</p>
<ul><li><b>Imprimerie</b> : t-shirt blanc pour nettoyer les presses et les rouleaux sans transfert de couleur.</li>
<li><b>Usinage et maintenance</b> : ratine couleur pour l'huile et la graisse.</li>
<li><b>Usage général</b> : t-shirt couleur, le plus économique.</li></ul>
<h2>Volumes et approvisionnement</h2>
<p>La quantité est illimitée. Hors Laval et Montréal, nous livrons à partir de 1 000 lb par livraison, avec un prix livré indiqué dans la soumission. Voir <a href="{{gros}}">guenilles en gros</a>.</p>
<h2>Solvants et chiffons usagés</h2>
<p>Les chiffons imbibés de solvants ou d'huile doivent être gardés dans des contenants métalliques fermés et éliminés selon vos règles de gestion des matières dangereuses. Voir le guide <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>""",
  "faq": [("Quel chiffon pour nettoyer une presse d'imprimerie?", "Le t-shirt blanc : il ne déteint pas avec les solvants de nettoyage."),
          ("Pouvez-vous livrer chaque semaine?", "Oui, nous planifions les livraisons régulières selon votre consommation."),
          ("Livrez-vous hors du Grand Montréal?", "Oui, ailleurs au Québec à partir de 1 000 lb par livraison.")]},
 "en": {"path": "/en/industrial-printing-rags/", "short": "Industry and printing",
  "title": "Industrial wiping rags and print shop rags – Québec",
  "desc": "Recycled cotton industrial rags for plants, print shops, machining and maintenance: ink, oil, solvents. Unlimited quantity, delivery across Québec.",
  "eyebrow": "Plants · print shops · maintenance", "h1": "Industrial wiping rags and print shop rags",
  "lede": "For ink, cutting oil, solvents and machine maintenance: recycled cotton in [packs], in unlimited quantity.",
  "card": "Ink, cutting oil, solvents and machine maintenance, in unlimited quantity.",
  "alt": "Bale of industrial rags made from recycled textiles",
  "body": """<h2>For the plant and the shop floor</h2>
<p>Machine shops, plants, print shops, warehouses and maintenance teams use rags for cutting oil, ink, solvents, machine grease and spills.</p>
<ul><li><b>Printing</b>: white T-shirt to clean presses and rollers with no color transfer.</li>
<li><b>Machining and maintenance</b>: colored terry for oil and grease.</li>
<li><b>General use</b>: colored T-shirt, the most economical.</li></ul>
<h2>Volumes and supply</h2>
<p>Quantity is unlimited. Outside Laval and Montréal we deliver from 1,000 lb per delivery, with a delivered price stated in the quote. See <a href="{{gros}}">wholesale rags</a>.</p>
<h2>Solvents and used rags</h2>
<p>Rags soaked with solvent or oil should be kept in closed metal containers and disposed of under your hazardous materials rules. See the guide <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>""",
  "faq": [("Which rag for cleaning a printing press?", "White T-shirt: it won't bleed with cleaning solvents."),
          ("Can you deliver every week?", "Yes, we schedule regular deliveries based on your usage."),
          ("Do you deliver outside Greater Montreal?", "Yes, elsewhere in Québec from 1,000 lb per delivery.")]},
}

PAGES["gros"] = {"kind": "sector", "img": IMG_BAGS, "rel": ["livraison", "industrie", "entretien"],
 "fr": {"path": "/guenilles-en-gros/", "short": "Guenilles en gros",
  "title": "Guenilles en gros et chiffons recyclés pour distributeurs",
  "desc": "Guenilles en gros et chiffons d'essuyage recyclés pour distributeurs sanitaires, quincailleries et fournisseurs. Quantité illimitée, livraison au Québec.",
  "eyebrow": "Distributeurs · revendeurs · gros volumes", "h1": "Guenilles en gros et chiffons recyclés pour distributeurs",
  "lede": "Un fournisseur québécois de chiffons d'essuyage recyclés : 4 produits, quantité illimitée, prix clairs et livraison partout au Québec.",
  "card": "Distributeurs sanitaires, quincailleries, fournisseurs : quantité illimitée.",
  "alt": "Sacs de guenilles recyclées prêts pour la livraison en gros",
  "body": """<h2>Un approvisionnement fiable</h2>
<p>Distributeurs de produits sanitaires, quincailleries, fournisseurs industriels, centres de location et grandes entreprises : nous fournissons des chiffons d'essuyage recyclés triés, emballés en [packs] et prêts à revendre ou à utiliser.</p>
<ul><li><b>4 produits</b> : t-shirt ou ratine, blanc ou couleur.</li>
<li><b>Quantité illimitée</b>, livraisons planifiées selon vos besoins.</li>
<li><b>Lavés, triés et traités</b> contre les punaises de lit, emballés à Laval.</li></ul>
<h2>Conditions</h2>
<p>Prix par [pack] : 32 $ couleur, 42 $ blanc, avant taxes. Hors Laval et Montréal, minimum de 1 000 lb (40 sacs) par livraison, frais de livraison selon votre emplacement. Commande confirmée et payée une semaine avant la livraison.</p>
<h2>Demander une soumission</h2>
<p>Indiquez le produit, la quantité et la ville de livraison dans le <a href="{{home#devis}}">formulaire</a> : nous vous répondons avec un prix livré.</p>""",
  "faq": [("Offrez-vous des prix de volume?", "Demandez une soumission avec vos quantités prévues : nous vous répondons avec un prix livré."),
          ("Puis-je mélanger les produits dans une livraison?", "Oui, le minimum de 1 000 lb s'applique au total de la livraison."),
          ("Livrez-vous en région?", "Oui, partout au Québec à partir de 1 000 lb, avec des frais selon la distance.")]},
 "en": {"path": "/en/wholesale-rags/", "short": "Wholesale rags",
  "title": "Wholesale rags and recycled wiping cloths for distributors",
  "desc": "Recycled wiping rags in bulk for janitorial distributors, hardware stores and industrial suppliers. Unlimited quantity, delivery across Québec.",
  "eyebrow": "Distributors · resellers · bulk", "h1": "Wholesale rags and recycled wiping cloths for distributors",
  "lede": "A Québec supplier of recycled wiping rags: 4 products, unlimited quantity, clear prices and delivery across Québec.",
  "card": "Janitorial distributors, hardware stores, suppliers: unlimited quantity.",
  "alt": "Bags of recycled rags ready for bulk delivery",
  "body": """<h2>Reliable supply</h2>
<p>Janitorial supply distributors, hardware stores, industrial suppliers, rental centres and large companies: we supply sorted recycled wiping rags, packed in [packs] and ready to resell or use.</p>
<ul><li><b>4 products</b>: T-shirt or terry, white or colored.</li>
<li><b>Unlimited quantity</b>, deliveries scheduled to your needs.</li>
<li><b>Washed, sorted and treated</b> against bedbugs, packed in Laval.</li></ul>
<h2>Terms</h2>
<p>Price per [pack]: $32 colored, $42 white, before tax. Outside Laval and Montréal, 1,000 lb minimum (40 bags) per delivery, delivery fee based on your location. Orders confirmed and paid one week before delivery.</p>
<h2>Request a quote</h2>
<p>Tell us the product, quantity and delivery city in the <a href="{{home#devis}}">form</a> and we'll reply with a delivered price.</p>""",
  "faq": [("Do you offer volume pricing?", "Request a quote with your expected quantities and we'll reply with a delivered price."),
          ("Can I mix products in one delivery?", "Yes, the 1,000 lb minimum applies to the delivery total."),
          ("Do you deliver to the regions?", "Yes, anywhere in Québec from 1,000 lb, with a fee based on distance.")]},
}

PAGES["blancs"] = {"kind": "product", "img": IMG_SHOP, "products": ["tshirt-blanc", "ratine-blanc"], "rel": ["peinture", "couleur", "industrie"],
 "fr": {"path": "/chiffons-blancs-recycles/", "short": "Chiffons blancs",
  "title": "Chiffons blancs recyclés, t-shirt et ratine 25 lb | Chiffons ÉCO",
  "desc": "Chiffons d'essuyage blancs en coton recyclé, t-shirt ou ratine, sans transfert de couleur. 42 $ le sac de 25 lb avant taxes. Laval, Montréal, Québec.",
  "eyebrow": "Produit · blanc", "h1": "Chiffons blancs recyclés : t-shirt et ratine",
  "lede": "Coton blanc trié, sans transfert de couleur, pour la peinture, la finition, l'imprimerie et les surfaces délicates. 42 $ le [pack].",
  "card": "T-shirt ou ratine blanc, sans transfert de couleur. 42 $ le [pack].",
  "alt": "Chiffons blancs conditionnés",
  "body": """<h2>Deux textures</h2>
<h3>T-shirt blanc</h3>
<p>Jersey de coton mince et doux. Pour appliquer et essuyer la teinture et le vernis, polir, nettoyer les presses d'imprimerie, l'inox et les surfaces délicates.</p>
<h3>Ratine blanche</h3>
<p>Tissu éponge épais de qualité supérieure. Très absorbant, pour les gros surplus, les déversements et le nettoyage d'outils, là où l'on ne veut aucune couleur.</p>
<h2>Pourquoi le blanc</h2>
<p>Un chiffon teint peut déteindre avec les solvants, la teinture ou l'humidité. Le blanc élimine ce risque et permet de voir la saleté. Pour l'essuyage courant, les <a href="{{couleur}}">chiffons couleur</a> coûtent moins cher.</p>
<h2>Qualité</h2>
<p>Coton recyclé lavé, trié et traité contre les punaises de lit, emballé en [packs] à Laval.</p>""",
  "faq": [("Les chiffons blancs sont-ils 100 % blancs?", "Ils sont triés pour ne garder que des textiles blancs ou très pâles, sans transfert de couleur."),
          ("Puis-je avoir un échantillon?", "Oui, sur demande.")]},
 "en": {"path": "/en/white-recycled-rags/", "short": "White rags",
  "title": "White recycled rags – T-shirt and terry, 25 lb | ECO Rags",
  "desc": "White recycled cotton wiping rags, T-shirt or terry, with no color transfer. $42 per 25 lb bag before tax. Laval, Montreal, Québec.",
  "eyebrow": "Product · white", "h1": "White recycled rags: T-shirt and terry",
  "lede": "Sorted white cotton with no color transfer, for painting, finishing, printing and delicate surfaces. $42 per [pack].",
  "card": "White T-shirt or terry, no color transfer. $42 per [pack].",
  "alt": "Packed white rags",
  "body": """<h2>Two textures</h2>
<h3>White T-shirt</h3>
<p>Thin, soft cotton jersey. To apply and wipe stain and varnish, polish, clean printing presses, stainless steel and delicate surfaces.</p>
<h3>White terry</h3>
<p>Premium thick towel cloth. Very absorbent, for heavy excess, spills and tool cleaning where you want no color at all.</p>
<h2>Why white</h2>
<p>Dyed rags can bleed with solvents, stain or moisture. White removes that risk and shows the dirt. For everyday wiping, <a href="{{couleur}}">colored rags</a> cost less.</p>
<h2>Quality</h2>
<p>Recycled cotton, washed, sorted and treated against bedbugs, packed in [packs] in Laval.</p>""",
  "faq": [("Are the white rags 100% white?", "They are sorted to keep only white or very pale textiles, with no color transfer."),
          ("Can I get a sample?", "Yes, on request.")]},
}

PAGES["couleur"] = {"kind": "product", "img": IMG_BAG, "products": ["tshirt-couleur", "ratine-couleur"], "rel": ["garage", "construction", "blancs"],
 "fr": {"path": "/chiffons-couleur-recycles/", "short": "Chiffons couleur",
  "title": "Chiffons couleur recyclés, t-shirt et ratine 25 lb | Chiffons ÉCO",
  "desc": "Chiffons d'essuyage couleur en coton recyclé, t-shirt ou ratine, pour garages, ateliers et chantiers. 32 $ le sac de 25 lb avant taxes. Livraison au Québec.",
  "eyebrow": "Produit · couleur", "h1": "Chiffons couleur recyclés : t-shirt et ratine",
  "lede": "Le choix économique pour l'essuyage de tous les jours : garages, ateliers, chantiers, entretien. 32 $ le [pack].",
  "card": "T-shirt ou ratine couleur, l'essuyage de tous les jours. 32 $ le [pack].",
  "alt": "Sac de 25 lb de chiffons t-shirt couleur",
  "body": """<h2>Deux textures</h2>
<h3>T-shirt couleur</h3>
<p>Notre produit le plus populaire. Jersey de coton doux et très absorbant, pour les mains, les outils, les surfaces et le ménage courant.</p>
<h3>Ratine couleur</h3>
<p>Tissu éponge épais et très résistant. Pour l'huile, la graisse, les gros déversements et l'équipement lourd.</p>
<h2>Pour qui</h2>
<p><a href="{{garage}}">Garages et mécanique</a>, <a href="{{construction}}">chantiers</a>, <a href="{{entretien}}">entretien ménager</a>, <a href="{{industrie}}">usines et ateliers</a>. Pour la peinture et la finition, prenez plutôt les <a href="{{blancs}}">chiffons blancs</a>.</p>
<h2>Qualité</h2>
<p>Coton recyclé lavé, trié et traité contre les punaises de lit, emballé en [packs] à Laval.</p>""",
  "faq": [("Les couleurs peuvent-elles déteindre?", "Avec des solvants ou de la teinture, un tissu teint peut déteindre. Pour ces usages, choisissez le blanc."),
          ("T-shirt ou ratine?", "T-shirt pour l'usage général, ratine pour l'huile, la graisse et les gros dégâts.")]},
 "en": {"path": "/en/colored-recycled-rags/", "short": "Colored rags",
  "title": "Colored recycled rags – T-shirt and terry, 25 lb | ECO Rags",
  "desc": "Colored recycled cotton wiping rags, T-shirt or terry, for garages, shops and job sites. $32 per 25 lb bag before tax. Delivery across Québec.",
  "eyebrow": "Product · colored", "h1": "Colored recycled rags: T-shirt and terry",
  "lede": "The budget choice for everyday wiping: garages, shops, job sites, cleaning. $32 per [pack].",
  "card": "Colored T-shirt or terry, for everyday wiping. $32 per [pack].",
  "alt": "25 lb bag of colored T-shirt rags",
  "body": """<h2>Two textures</h2>
<h3>Colored T-shirt</h3>
<p>Our most popular product. Soft, very absorbent cotton jersey for hands, tools, surfaces and everyday cleaning.</p>
<h3>Colored terry</h3>
<p>Thick, very tough towel cloth. For oil, grease, big spills and heavy equipment.</p>
<h2>Who it's for</h2>
<p><a href="{{garage}}">Garages and mechanics</a>, <a href="{{construction}}">job sites</a>, <a href="{{entretien}}">janitorial</a>, <a href="{{industrie}}">plants and shops</a>. For painting and finishing, choose <a href="{{blancs}}">white rags</a> instead.</p>
<h2>Quality</h2>
<p>Recycled cotton, washed, sorted and treated against bedbugs, packed in [packs] in Laval.</p>""",
  "faq": [("Can the colors bleed?", "With solvents or stain, dyed fabric can bleed. For those jobs, choose white."),
          ("T-shirt or terry?", "T-shirt for general use, terry for oil, grease and big spills.")]},
}

PAGES["livraison"] = {"kind": "info", "img": IMG_BAGS, "rel": ["gros", "faq", "couleur"],
 "fr": {"path": "/livraison-grand-montreal/", "short": "Livraison",
  "title": "Livraison de chiffons à Laval, Montréal, Rive-Nord et au Québec",
  "desc": "Livraison de chiffons d'essuyage recyclés à votre adresse : Laval, Montréal, Longueuil, Rive-Nord, Rive-Sud et partout au Québec à partir de 1 000 lb.",
  "eyebrow": "Livraison", "h1": "Livraison à Laval, Montréal et partout au Québec",
  "lede": "Vos chiffons livrés à votre adresse. Les frais dépendent de votre emplacement et sont indiqués dans votre soumission.",
  "card": "Grand Montréal, et partout au Québec à partir de 1 000 lb.",
  "alt": "Sacs de chiffons prêts pour la livraison",
  "body": """<h2>Grand Montréal</h2>
<p>Nous trions et emballons à Laval, et nous livrons dans tout le Grand Montréal :</p>
<ul><li><b>Laval</b> : Chomedey, Laval-des-Rapides, Pont-Viau, Vimont, Auteuil, Sainte-Rose, Fabreville, Sainte-Dorothée, Duvernay, Saint-François, Saint-Vincent-de-Paul.</li>
<li><b>Montréal</b> et l'île de Montréal.</li>
<li><b>Rive-Nord</b> : Terrebonne, Blainville, Boisbriand, Mirabel, Saint-Eustache, Repentigny.</li>
<li><b>Rive-Sud</b> : Longueuil, Brossard, Boucherville.</li></ul>
<p>Demandez-nous les conditions pour votre secteur.</p>
<h2>Ailleurs au Québec</h2>
<p>Nous livrons aussi en région, à partir de <b>1 000 lb par livraison</b> (40 sacs, produits mélangés acceptés). Les frais de livraison dépendent de la distance et sont indiqués dans la soumission.</p>
<h2>Comment ça fonctionne</h2>
<ol><li>Envoyez votre demande : produit, quantité et ville de livraison.</li>
<li>Nous vous envoyons une soumission avec le prix livré à votre adresse.</li>
<li>La commande est confirmée et payée une semaine avant la livraison.</li>
<li>Nous livrons à l'adresse convenue : bureau, entrepôt, atelier ou chantier.</li></ol>""",
  "faq": [("Combien coûte la livraison?", "Cela dépend de votre emplacement. Le montant exact est indiqué dans votre soumission."),
          ("Quel est le minimum hors Grand Montréal?", "1 000 lb par livraison, soit 40 sacs de 25 lb."),
          ("Quand dois-je payer?", "La commande est confirmée et payée une semaine avant la livraison.")]},
 "en": {"path": "/en/delivery-greater-montreal/", "short": "Delivery",
  "title": "Rag delivery in Laval, Montreal, North Shore and across Québec",
  "desc": "Recycled wiping rags delivered to your address: Laval, Montreal, Longueuil, North Shore, South Shore and anywhere in Québec from 1,000 lb.",
  "eyebrow": "Delivery", "h1": "Delivery in Laval, Montreal and across Québec",
  "lede": "Your rags delivered to your address. The fee depends on your location and is stated in your quote.",
  "card": "Greater Montreal, and anywhere in Québec from 1,000 lb.",
  "alt": "Bags of rags ready for delivery",
  "body": """<h2>Greater Montreal</h2>
<p>We sort and pack in Laval and deliver across Greater Montreal:</p>
<ul><li><b>Laval</b>: Chomedey, Laval-des-Rapides, Pont-Viau, Vimont, Auteuil, Sainte-Rose, Fabreville, Sainte-Dorothée, Duvernay, Saint-François, Saint-Vincent-de-Paul.</li>
<li><b>Montréal</b> and the island of Montreal.</li>
<li><b>North Shore</b>: Terrebonne, Blainville, Boisbriand, Mirabel, Saint-Eustache, Repentigny.</li>
<li><b>South Shore</b>: Longueuil, Brossard, Boucherville.</li></ul>
<p>Ask us about the terms for your area.</p>
<h2>Elsewhere in Québec</h2>
<p>We also deliver to the regions, from <b>1,000 lb per delivery</b> (40 bags, mixed products accepted). The delivery fee depends on distance and is stated in the quote.</p>
<h2>How it works</h2>
<ol><li>Send your request: product, quantity and delivery city.</li>
<li>We send a quote with the price delivered to your address.</li>
<li>The order is confirmed and paid one week before delivery.</li>
<li>We deliver to the agreed address: office, warehouse, shop or job site.</li></ol>""",
  "faq": [("How much is delivery?", "It depends on your location. The exact amount is stated in your quote."),
          ("What's the minimum outside Greater Montreal?", "1,000 lb per delivery, i.e. 40 bags of 25 lb."),
          ("When do I pay?", "The order is confirmed and paid one week before delivery.")]},
}

PAGES["faq"] = {"kind": "faq", "img": None, "rel": ["livraison", "gros", "guides"],
 "fr": {"path": "/faq/", "short": "FAQ", "title": "FAQ chiffons d'essuyage recyclés : prix, livraison | Chiffons ÉCO",
  "desc": "Prix, produits, livraison, minimum de commande, échantillons et sécurité : toutes les réponses sur nos chiffons d'essuyage recyclés de Laval.",
  "eyebrow": "FAQ", "h1": "Questions fréquentes sur nos chiffons", "lede": "Prix, produits, livraison et commandes.",
  "card": "Prix, livraison, minimum, échantillons, sécurité.", "body": ""},
 "en": {"path": "/en/faq/", "short": "FAQ", "title": "FAQ – recycled wiping rags, prices and delivery | ECO Rags",
  "desc": "Prices, products, delivery, minimum order, samples and safety: all the answers about our recycled wiping rags from Laval.",
  "eyebrow": "FAQ", "h1": "Frequently asked questions about our rags", "lede": "Prices, products, delivery and orders.",
  "card": "Prices, delivery, minimum, samples, safety.", "body": ""},
}

PAGES["guides"] = {"kind": "guides", "img": None, "rel": [],
 "fr": {"path": "/guides/", "short": "Guides", "title": "Guides pratiques sur les chiffons d'essuyage | Chiffons ÉCO",
  "desc": "Guides pratiques : chiffons huileux et risque d'incendie, chiffons recyclés ou essuie-tout en papier. Conseils pour garages, ateliers et entretien.",
  "eyebrow": "Guides", "h1": "Guides pratiques", "lede": "Des conseils concrets pour choisir, utiliser et jeter vos chiffons.",
  "card": "Conseils pour choisir, utiliser et jeter vos chiffons.", "body": ""},
 "en": {"path": "/en/guides/", "short": "Guides", "title": "Practical guides about wiping rags | ECO Rags",
  "desc": "Practical guides: oily rags and fire risk, recycled rags vs paper towels. Tips for garages, shops and cleaning crews.",
  "eyebrow": "Guides", "h1": "Practical guides", "lede": "Concrete tips to choose, use and dispose of your rags.",
  "card": "Tips to choose, use and dispose of your rags.", "body": ""},
}

PAGES["guide-huileux"] = {"kind": "guide", "img": IMG_SHOP, "rel": ["garage", "peinture", "industrie"],
 "fr": {"path": "/guides/chiffons-huileux-risque-incendie/", "short": "Chiffons huileux et risque d'incendie",
  "title": "Chiffons huileux : risque d'incendie et comment les jeter",
  "desc": "Pourquoi les chiffons imbibés d'huile, de teinture ou de solvant peuvent prendre feu seuls, et comment les ranger et les jeter de façon sécuritaire au Québec.",
  "eyebrow": "Guide · sécurité", "h1": "Chiffons huileux : le risque d'incendie et comment les jeter",
  "lede": "Un tas de chiffons imbibés d'huile de lin ou de teinture peut s'enflammer tout seul. Voici comment l'éviter.",
  "card": "Pourquoi un tas de chiffons imbibés peut prendre feu seul, et quoi faire.",
  "alt": "Chiffons d'atelier",
  "body": """<h2>Pourquoi un chiffon peut prendre feu tout seul</h2>
<p>Certaines huiles, comme l'huile de lin, l'huile de tung et beaucoup de teintures et vernis à l'huile, durcissent en réagissant avec l'oxygène de l'air. Cette réaction dégage de la chaleur. Dans un tas ou une boule de chiffons, la chaleur ne s'échappe pas : la température monte jusqu'à l'inflammation, parfois plusieurs heures plus tard. C'est la <b>combustion spontanée</b>.</p>
<p>Les chiffons imbibés d'essence, de diluant ou de solvants ne s'enflamment pas seuls de la même façon, mais leurs vapeurs sont très inflammables près d'une flamme ou d'une étincelle.</p>
<h2>Les bons gestes</h2>
<ol><li><b>Ne laissez jamais les chiffons en tas</b>, ni dans une poubelle ouverte, ni dans un coin de l'atelier.</li>
<li><b>Faites-les sécher à plat</b>, à l'extérieur, loin des bâtiments et à l'abri des enfants et des animaux, avant de les jeter.</li>
<li><b>Ou mettez-les dans un contenant métallique</b> avec un couvercle étanche, rempli d'eau, en attendant de vous en débarrasser.</li>
<li><b>Au travail, utilisez une poubelle métallique à fermeture automatique</b> prévue pour les chiffons huileux, et videz-la chaque jour.</li>
<li><b>Ne mettez pas de chiffons imbibés d'huile dans une sécheuse</b>, même après lavage : des incendies de sécheuse sont causés ainsi.</li></ol>
<h2>Où les jeter au Québec</h2>
<p>Pour les particuliers, les chiffons imbibés d'huile ou de solvant sont des résidus domestiques dangereux (RDD) : apportez-les à l'écocentre de votre ville dans un contenant fermé. Les entreprises doivent les éliminer selon leurs règles de gestion des matières dangereuses, souvent avec un fournisseur spécialisé.</p>
<div class="note"><p>En cas de doute, informez-vous auprès du service de sécurité incendie de votre municipalité.</p></div>
<h2>Choisir le bon chiffon</h2>
<p>Pour la teinture et le vernis, le <a href="{{blancs}}">t-shirt blanc</a> ne déteint pas. Pour l'huile et la graisse au garage, la <a href="{{couleur}}">ratine couleur</a> absorbe le plus.</p>""",
  "faq": [("Combien de temps avant qu'un chiffon prenne feu?", "Cela peut prendre de quelques heures à plus d'une journée, selon l'huile, la quantité et la température. C'est pourquoi il ne faut jamais laisser un tas sans surveillance."),
          ("Un chiffon à l'essence peut-il s'enflammer seul?", "Pas de la même façon que l'huile de lin, mais ses vapeurs s'enflamment facilement. Faites-le sécher à l'extérieur, loin de toute source d'ignition.")]},
 "en": {"path": "/en/guides/oily-rags-fire-risk/", "short": "Oily rags and fire risk",
  "title": "Oily rags: fire risk and how to dispose of them safely",
  "desc": "Why rags soaked with oil, stain or solvent can catch fire on their own, and how to store and dispose of them safely in Québec.",
  "eyebrow": "Guide · safety", "h1": "Oily rags: the fire risk and how to dispose of them",
  "lede": "A pile of rags soaked with linseed oil or stain can catch fire on its own. Here's how to prevent it.",
  "card": "Why a pile of soaked rags can catch fire on its own, and what to do.",
  "alt": "Shop rags",
  "body": """<h2>Why a rag can catch fire on its own</h2>
<p>Some oils, such as linseed oil, tung oil and many oil-based stains and varnishes, harden by reacting with oxygen in the air. That reaction gives off heat. In a pile or a ball of rags the heat can't escape, so the temperature climbs until it ignites, sometimes hours later. This is <b>spontaneous combustion</b>.</p>
<p>Rags soaked with gasoline, thinner or solvents don't self-ignite the same way, but their vapours are highly flammable near a flame or spark.</p>
<h2>What to do</h2>
<ol><li><b>Never leave rags in a pile</b>, in an open trash can or in a corner of the shop.</li>
<li><b>Dry them flat</b>, outdoors, away from buildings, children and pets, before throwing them out.</li>
<li><b>Or put them in a metal container</b> with a tight lid, filled with water, until you can get rid of them.</li>
<li><b>At work, use a self-closing metal oily-waste can</b> and empty it every day.</li>
<li><b>Don't put oil-soaked rags in a dryer</b>, even after washing: dryer fires start this way.</li></ol>
<h2>Where to dispose of them in Québec</h2>
<p>For households, rags soaked with oil or solvent are household hazardous waste: take them to your city's eco-centre in a closed container. Businesses must dispose of them under their hazardous materials rules, often through a specialized provider.</p>
<div class="note"><p>If in doubt, check with your municipality's fire department.</p></div>
<h2>Choosing the right rag</h2>
<p>For stain and varnish, <a href="{{blancs}}">white T-shirt</a> rags won't bleed. For oil and grease in the garage, <a href="{{couleur}}">colored terry</a> absorbs the most.</p>""",
  "faq": [("How long before a rag catches fire?", "Anywhere from a few hours to more than a day, depending on the oil, the amount and the temperature. That's why a pile should never be left unattended."),
          ("Can a gasoline rag ignite on its own?", "Not the same way as linseed oil, but its vapours ignite easily. Dry it outdoors, away from any ignition source.")]},
}

PAGES["guide-papier"] = {"kind": "guide", "img": IMG_SYM, "rel": ["entretien", "garage", "gros"],
 "fr": {"path": "/guides/chiffons-recycles-ou-papier/", "short": "Chiffons recyclés ou essuie-tout",
  "title": "Chiffons recyclés ou essuie-tout en papier : lequel choisir?",
  "desc": "Chiffons d'essuyage en coton recyclé ou essuie-tout en papier : absorption, coût, déchets et quand le papier reste préférable. Comparaison honnête.",
  "eyebrow": "Guide · comparaison", "h1": "Chiffons recyclés ou essuie-tout en papier : lequel choisir?",
  "lede": "Les deux ont leur place. Voici quand le chiffon de coton recyclé est le meilleur choix, et quand le papier reste préférable.",
  "card": "Absorption, coût, déchets : quand choisir le chiffon et quand garder le papier.",
  "alt": "Symbole de recyclage en textiles colorés",
  "body": """<h2>Absorption et solidité</h2>
<p>Le coton absorbe l'eau, l'huile, la graisse et les solvants, et il ne se déchire pas quand il est mouillé. Pour un gros dégât ou une pièce graisseuse, un chiffon remplace souvent plusieurs feuilles de papier.</p>
<h2>Coût</h2>
<p>Les chiffons recyclés se vendent au poids. Un chiffon sert plus longtemps qu'une feuille et, quand il n'est pas souillé de produits dangereux, il peut être lavé et réutilisé. Pour l'essuyage d'atelier, le coût à l'usage est généralement plus bas.</p>
<h2>Déchets</h2>
<p>Les essuie-tout vont à la poubelle après un seul usage. Nos chiffons sont faits de vêtements et textiles qui seraient autrement envoyés à l'enfouissement : vous leur donnez une deuxième vie avant qu'ils soient jetés.</p>
<h2>Quand le papier reste préférable</h2>
<ul><li>Le séchage des mains dans les toilettes publiques.</li>
<li>Les surfaces en contact avec les aliments, quand votre procédure exige un essuie-tout à usage unique.</li>
<li>Les liquides biologiques et les situations où l'on veut tout jeter immédiatement.</li></ul>
<h2>En résumé</h2>
<p>Pour l'atelier, le garage, le chantier, l'usine et l'entretien des bâtiments, les <a href="{{couleur}}">chiffons recyclés</a> font mieux pour moins cher. Gardez le papier pour l'hygiène des mains et les usages à jeter immédiatement.</p>""",
  "faq": [("Peut-on laver les chiffons recyclés?", "Oui, s'ils ne sont pas imbibés d'huile ou de solvant. Ceux-là ne doivent pas aller dans une sécheuse domestique."),
          ("Les chiffons recyclés sont-ils hygiéniques?", "Les nôtres sont lavés et traités contre les punaises de lit. Pour le contact alimentaire, suivez les règles du MAPAQ.")]},
 "en": {"path": "/en/guides/recycled-rags-vs-paper-towels/", "short": "Recycled rags vs paper towels",
  "title": "Recycled rags vs paper towels: which should you use?",
  "desc": "Recycled cotton wiping rags or paper towels: absorbency, cost, waste and when paper is still the better choice. An honest comparison.",
  "eyebrow": "Guide · comparison", "h1": "Recycled rags vs paper towels: which should you use?",
  "lede": "Both have their place. Here's when a recycled cotton rag is the better choice, and when paper still wins.",
  "card": "Absorbency, cost, waste: when to choose rags and when to keep paper.",
  "alt": "Recycling symbol made of colored textiles",
  "body": """<h2>Absorbency and strength</h2>
<p>Cotton absorbs water, oil, grease and solvents, and doesn't tear when wet. For a big spill or a greasy part, one rag often replaces several paper sheets.</p>
<h2>Cost</h2>
<p>Recycled rags are sold by weight. A rag lasts longer than a sheet and, when it isn't soaked with hazardous products, it can be washed and reused. For shop wiping, the cost per use is generally lower.</p>
<h2>Waste</h2>
<p>Paper towels go in the trash after one use. Our rags are made from clothing and textiles that would otherwise go to landfill, so you give them a second life before they're thrown out.</p>
<h2>When paper is still better</h2>
<ul><li>Drying hands in public washrooms.</li>
<li>Food-contact surfaces, when your procedure requires single-use paper.</li>
<li>Bodily fluids and situations where you want to throw everything out immediately.</li></ul>
<h2>Bottom line</h2>
<p>For shops, garages, job sites, plants and building maintenance, <a href="{{couleur}}">recycled rags</a> do better for less. Keep paper for hand hygiene and throw-away uses.</p>""",
  "faq": [("Can recycled rags be washed?", "Yes, if they aren't soaked with oil or solvent. Those must not go in a home dryer."),
          ("Are recycled rags hygienic?", "Ours are washed and treated against bedbugs. For food contact, follow MAPAQ rules.")]},
}

PAGES["merci"] = {"kind": "thanks", "img": None, "rel": [],
 "fr": {"path": "/merci/", "short": "Merci", "title": "Merci – demande reçue | Chiffons ÉCO", "desc": "Votre demande de soumission a bien été reçue.",
  "eyebrow": "Demande reçue", "h1": "Merci! Votre demande est envoyée.", "lede": "Nous vous répondons rapidement par courriel ou par téléphone. Pour une urgence, écrivez à info@entretienlaval.ca.", "card": "", "body": ""},
 "en": {"path": "/en/thanks/", "short": "Thanks", "title": "Thank you – request received | ECO Rags", "desc": "Your quote request was received.",
  "eyebrow": "Request received", "h1": "Thank you! Your request was sent.", "lede": "We'll get back to you quickly by email or phone. For anything urgent, email info@entretienlaval.ca.", "card": "", "body": ""},
}

# ---------------- expansion modules ----------------
from content_sectors2 import SECTOR2_PAGES, SECTOR2_KEYS
from content_guides2 import GUIDE2_PAGES
from content_cities import CITY_PAGES, CITY_KEYS
_merci = PAGES.pop("merci")
PAGES.update(SECTOR2_PAGES); PAGES.update(GUIDE2_PAGES); PAGES.update(CITY_PAGES)
PAGES["merci"] = _merci
SECTOR_KEYS = SECTOR_KEYS + SECTOR2_KEYS
GUIDE_KEYS = [k for k, p in PAGES.items() if p["kind"] in ("guide", "tool")]

PAGES["apropos"] = {"kind": "info", "img": IMG_BAGS, "rel": ["gros", "livraison", "faq"],
 "fr": {"path": "/a-propos/", "short": "À propos", "title": "À propos d'Entretien Laval – Chiffons ÉCO, guenilles en gros",
  "desc": "Entretien Laval (Chiffons ÉCO) vend des chiffons d'essuyage recyclés en sacs de 25 lb, dès 32 $, livrés au Grand Montréal et partout au Québec.",
  "eyebrow": "À propos", "h1": "Entretien Laval – Chiffons ÉCO", "lede": "Une entreprise de Laval qui transforme des textiles récupérés en chiffons d'essuyage pour les entreprises du Québec.",
  "card": "Qui nous sommes, ce que nous vendons, où nous livrons.", "alt": "Sacs de chiffons recyclés Chiffons ÉCO",
  "body": """<h2>En bref</h2>
<ul><li><b>Entreprise</b> : Entretien Laval, marque Chiffons ÉCO (ECO Rags). NEQ 2280629637.</li>
<li><b>Adresse</b> : 309-1355 boul. Le Corbusier, Laval (Québec) H7N 0G4.</li>
<li><b>Produits</b> : chiffons d'essuyage (guenilles) en coton recyclé, lavés, triés et traités contre les punaises de lit, en sacs de 25 lb.</li>
<li><b>Prix</b> : t-shirt ou ratine couleur 32 $ le sac; t-shirt ou ratine blanc 42 $ le sac. Avant taxes, quantité illimitée.</li>
<li><b>Livraison</b> : Laval, Montréal et le Grand Montréal; partout au Québec à partir de 1 000 lb. Frais selon l'emplacement.</li>
<li><b>Clients</b> : garages, ateliers, entreprises de ménage, chantiers, restaurants, industries, distributeurs.</li>
<li><b>Contact</b> : info@entretienlaval.ca.</li></ul>
<h2>Où acheter des guenilles en gros à Laval ou à Montréal?</h2>
<p>Entretien Laval vend des <a href="{{gros}}">guenilles en gros</a> en sacs de 25 lb, livrées à <a href="{{ville-laval}}">Laval</a>, à <a href="{{ville-montreal}}">Montréal</a> et dans le Grand Montréal. Demandez une <a href="{{home#devis}}">soumission</a>.</p>
<h2>Pourquoi des chiffons recyclés?</h2>
<p>Ils absorbent mieux que le papier et réduisent les déchets : les textiles récupérés auraient sinon fini à l'enfouissement. Voir le guide <a href="{{guide-papier}}">chiffons recyclés ou papier</a>.</p>""",
  "faq": [("Où acheter des chiffons d'essuyage en gros au Québec?", "Chez Entretien Laval (Chiffons ÉCO), à Laval : sacs de 25 lb dès 32 $, livrés au Grand Montréal et partout au Québec à partir de 1 000 lb."),
          ("Qui vend des guenilles de garage à Laval?", "Entretien Laval vend des guenilles de coton recyclé pour garages, en t-shirt ou en ratine.")]},
 "en": {"path": "/en/about/", "short": "About", "title": "About Entretien Laval – ECO Rags, wholesale wiping rags",
  "desc": "Entretien Laval (ECO Rags) sells recycled wiping rags in 25 lb bags from $32, delivered across Greater Montreal and anywhere in Québec.",
  "eyebrow": "About", "h1": "Entretien Laval – ECO Rags", "lede": "A Laval company that turns reclaimed textiles into wiping rags for Québec businesses.",
  "card": "Who we are, what we sell, where we deliver.", "alt": "Bags of ECO Rags recycled rags",
  "body": """<h2>At a glance</h2>
<ul><li><b>Business</b>: Entretien Laval, Chiffons ÉCO (ECO Rags) brand. NEQ 2280629637.</li>
<li><b>Address</b>: 309-1355 boul. Le Corbusier, Laval, Québec H7N 0G4.</li>
<li><b>Products</b>: recycled cotton wiping rags (shop rags), washed, sorted and treated against bedbugs, in 25 lb bags.</li>
<li><b>Prices</b>: colored T-shirt or terry $32 per bag; white T-shirt or terry $42 per bag. Before tax, no quantity limit.</li>
<li><b>Delivery</b>: Laval, Montréal and Greater Montreal; anywhere in Québec from 1,000 lb. Fees depend on location.</li>
<li><b>Customers</b>: garages, workshops, cleaning companies, job sites, restaurants, industry, distributors.</li>
<li><b>Contact</b>: info@entretienlaval.ca.</li></ul>
<h2>Where to buy rags in bulk in Laval or Montreal?</h2>
<p>Entretien Laval sells <a href="{{gros}}">wholesale rags</a> in 25 lb bags, delivered in <a href="{{ville-laval}}">Laval</a>, <a href="{{ville-montreal}}">Montréal</a> and Greater Montreal. Request a <a href="{{home#devis}}">quote</a>.</p>
<h2>Why recycled rags?</h2>
<p>They absorb better than paper and cut waste: the reclaimed textiles would otherwise go to landfill. See the guide <a href="{{guide-papier}}">recycled rags vs paper</a>.</p>""",
  "faq": [("Where can I buy wiping rags in bulk in Québec?", "From Entretien Laval (ECO Rags) in Laval: 25 lb bags from $32, delivered across Greater Montreal and anywhere in Québec from 1,000 lb."),
          ("Who sells shop rags in Laval?", "Entretien Laval sells recycled cotton shop rags for garages, T-shirt or terry.")]}}
_m = PAGES.pop("merci"); PAGES["merci"] = _m

# ---------------- audit follow-ups ----------------
import content_audit as A
PAGES["secteurs"] = A.HUB
for _l in ("fr", "en"):
    PAGES["guides"][_l]["body"] = A.GUIDES_BODY[_l]
    PAGES["gros"][_l]["body"] += A.GROS_EXTRA[_l]
    PAGES["calculateur"][_l]["body"] += A.CALC_EXTRA[_l]
for _k, _x in A.EN_SECTOR_EXTRA.items():
    PAGES[_k]["en"]["body"] += _x
for _k in CITY_KEYS:
    _fr, _en = A.city_extra(_k, PAGES[_k])
    PAGES[_k]["fr"]["body"] += _fr; PAGES[_k]["en"]["body"] += _en

# ---------------- online ordering (PayPal) ----------------
import content_order as O
if O.ready():
    PAGES["commander"] = O.PAGE
_m = PAGES.pop("merci"); PAGES["merci"] = _m
