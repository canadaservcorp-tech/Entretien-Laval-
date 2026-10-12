"""City / delivery-area pages. Each page has its own local details; the delivery terms come from the quote the user supplied."""
BAG, BAGS, BALE = "sac-chiffons-t-shirt-couleur-25-lb.webp", "sacs-chiffons-couleur-25-lb.webp", "balle-compressee-de-chiffons-eco-en-textiles-recyc.webp"

C = [
 dict(key="ville-laval", name="Laval", fr="/chiffons-guenilles-laval/", en="/en/rags-laval/", core=True, img=BAG,
  hoods=["Chomedey", "Laval-des-Rapides", "Pont-Viau", "Vimont", "Auteuil", "Sainte-Rose", "Fabreville", "Sainte-Dorothée", "Duvernay", "Saint-François", "Saint-Vincent-de-Paul", "Laval-Ouest"],
  intro_fr="Nos chiffons sont triés et emballés ici même, à Laval. C'est notre secteur principal : les garages, ateliers, chantiers et entreprises d'entretien de l'île Jésus sont nos voisins.",
  intro_en="Our rags are sorted and packed right here in Laval. It's our home area: garages, workshops, job sites and cleaning companies on Île Jésus are our neighbours.",
  ind_fr="garages et concessionnaires, ateliers de fabrication, entrepreneurs en construction, entreprises de ménage et gestionnaires d'immeubles",
  ind_en="garages and dealerships, fabrication shops, contractors, cleaning companies and property managers",
  rel=["garage", "entretien", "ville-montreal"]),
 dict(key="ville-montreal", name="Montréal", fr="/chiffons-guenilles-montreal/", en="/en/rags-montreal/", core=True, img=BAGS,
  hoods=["Saint-Laurent", "Ahuntsic-Cartierville", "Montréal-Nord", "Rivière-des-Prairies–Pointe-aux-Trembles", "Anjou", "Saint-Léonard", "Mercier–Hochelaga-Maisonneuve", "Rosemont–La Petite-Patrie", "Villeray–Saint-Michel–Parc-Extension", "Lachine", "LaSalle", "Le Sud-Ouest", "Montréal-Est", "Dorval et Pointe-Claire"],
  intro_fr="Montréal est à quelques minutes de Laval, où nous trions et emballons nos chiffons. Nous livrons partout sur l'île, des secteurs industriels de Saint-Laurent et d'Anjou jusqu'aux restaurants du centre.",
  intro_en="Montréal is minutes from Laval, where we sort and pack our rags. We deliver across the island, from the industrial areas of Saint-Laurent and Anjou to downtown restaurants.",
  ind_fr="garages, imprimeries, restaurants, ateliers de fabrication, entreprises de ménage commercial et distributeurs",
  ind_en="garages, print shops, restaurants, fabrication shops, commercial cleaning companies and distributors",
  rel=["restauration", "industrie", "ville-laval"]),
 dict(key="ville-longueuil", name="Longueuil", fr="/chiffons-guenilles-longueuil/", en="/en/rags-longueuil/", core=False, img=BALE,
  hoods=["Le Vieux-Longueuil", "Saint-Hubert", "Greenfield Park", "LeMoyne"],
  intro_fr="De l'autre côté du fleuve, Longueuil compte beaucoup de garages, d'ateliers et d'entreprises de services. Nous y livrons nos sacs de 25 lb à l'adresse de votre entreprise.",
  intro_en="Across the river, Longueuil has many garages, workshops and service businesses. We deliver our 25 lb bags to your business address.",
  ind_fr="garages, ateliers d'entretien de véhicules et d'équipement, entrepreneurs et entreprises d'entretien",
  ind_en="garages, vehicle and equipment maintenance shops, contractors and cleaning companies",
  rel=["ville-rive-sud", "garage", "gros"]),
 dict(key="ville-terrebonne", name="Terrebonne", fr="/chiffons-guenilles-terrebonne/", en="/en/rags-terrebonne/", core=False, img=BAG,
  hoods=["Terrebonne", "Lachenaie", "La Plaine", "Mascouche"],
  intro_fr="Terrebonne et le secteur Lachenaie sont à courte distance de Laval par l'autoroute 25. Nous y livrons les entreprises qui utilisent des chiffons chaque jour.",
  intro_en="Terrebonne and the Lachenaie area are a short drive from Laval along Highway 25. We deliver to businesses that go through rags every day.",
  ind_fr="garages, entrepreneurs en construction et en rénovation, ateliers et entreprises de transport",
  ind_en="garages, construction and renovation contractors, workshops and trucking companies",
  rel=["construction", "ville-rive-nord", "couleur"]),
 dict(key="ville-blainville", name="Blainville et Boisbriand", fr="/chiffons-guenilles-blainville-boisbriand/", en="/en/rags-blainville-boisbriand/", core=False, img=BAGS,
  hoods=["Blainville", "Boisbriand", "Sainte-Thérèse", "Rosemère", "Lorraine", "Bois-des-Filion"],
  intro_fr="Blainville, Boisbriand et Sainte-Thérèse sont juste au nord de Laval, de l'autre côté de la rivière des Mille Îles. Leurs zones industrielles et commerciales utilisent beaucoup de chiffons d'atelier.",
  intro_en="Blainville, Boisbriand and Sainte-Thérèse sit just north of Laval, across the Rivière des Mille Îles. Their industrial and commercial areas use a lot of shop rags.",
  ind_fr="usines et ateliers, garages, entreprises de peinture et de finition, et services d'entretien",
  ind_en="plants and workshops, garages, painting and finishing companies, and maintenance services",
  rel=["usinage", "peinture", "ville-rive-nord"]),
 dict(key="ville-rive-nord", name="la Rive-Nord", fr="/chiffons-guenilles-rive-nord/", en="/en/rags-north-shore/", core=False, img=BALE, name_en="the North Shore",
  hoods=["Saint-Eustache", "Deux-Montagnes", "Mirabel", "Saint-Jérôme", "Repentigny", "L'Assomption", "Mascouche"],
  intro_fr="De Saint-Eustache à Repentigny, en passant par Mirabel et Saint-Jérôme, nous livrons la couronne nord de Montréal.",
  intro_en="From Saint-Eustache to Repentigny, including Mirabel and Saint-Jérôme, we deliver across Montreal's North Shore.",
  ind_fr="garages, fermes et entreprises de machinerie, ateliers de fabrication et entrepreneurs",
  ind_en="garages, farms and equipment dealers, fabrication shops and contractors",
  rel=["agriculture", "ville-terrebonne", "ville-blainville"]),
 dict(key="ville-rive-sud", name="la Rive-Sud", fr="/chiffons-guenilles-rive-sud/", en="/en/rags-south-shore/", core=False, img=BAG, name_en="the South Shore",
  hoods=["Brossard", "Boucherville", "Saint-Lambert", "La Prairie", "Candiac", "Châteauguay", "Saint-Bruno-de-Montarville", "Varennes", "Sainte-Julie"],
  intro_fr="Brossard, Boucherville, La Prairie, Châteauguay : la Rive-Sud compte de grands parcs industriels, comme celui de Boucherville. Nous y livrons nos chiffons recyclés.",
  intro_en="Brossard, Boucherville, La Prairie, Châteauguay: the South Shore has large industrial parks, such as Boucherville's. We deliver our recycled rags there.",
  ind_fr="usines, entrepôts, garages, ateliers d'usinage et entreprises d'entretien",
  ind_en="plants, warehouses, garages, machine shops and cleaning companies",
  rel=["ville-longueuil", "industrie", "gros"]),
 dict(key="ville-quebec", name="Québec", fr="/chiffons-guenilles-quebec/", en="/en/rags-quebec-city/", core=False, img=BAGS, name_en="Québec City", far=True, dist=250,
  hoods=["Sainte-Foy", "Charlesbourg", "Beauport", "Limoilou", "Les Rivières", "L'Ancienne-Lorette", "Lévis"],
  intro_fr="Pour la région de Québec, à environ 250 km de Laval, nous livrons par commandes de 1 000 lb ou plus. C'est la formule idéale pour un garage, une entreprise d'entretien ou un distributeur qui veut faire des réserves.",
  intro_en="For the Québec City area, about 250 km from Laval, we deliver orders of 1,000 lb or more. It suits a garage, cleaning company or distributor that wants to stock up.",
  ind_fr="garages et concessionnaires, entreprises d'entretien, chantiers et distributeurs de produits d'entretien",
  ind_en="garages and dealerships, cleaning companies, job sites and janitorial supply distributors",
  rel=["gros", "ville-trois-rivieres", "livraison"]),
 dict(key="ville-sherbrooke", name="Sherbrooke", fr="/chiffons-guenilles-sherbrooke/", en="/en/rags-sherbrooke/", core=False, img=BALE, far=True, dist=160,
  hoods=["Sherbrooke", "Magog", "le reste de l'Estrie"],
  intro_fr="Sherbrooke et l'Estrie sont à environ 160 km de Laval. Nous y livrons à partir de 1 000 lb par livraison, en mélangeant les produits si vous le voulez.",
  intro_en="Sherbrooke and the Eastern Townships are about 160 km from Laval. We deliver there from 1,000 lb per delivery, with mixed products if you like.",
  ind_fr="ateliers de fabrication, garages, entreprises d'entretien et distributeurs régionaux",
  ind_en="fabrication shops, garages, cleaning companies and regional distributors",
  rel=["gros", "usinage", "livraison"]),
 dict(key="ville-trois-rivieres", name="Trois-Rivières", fr="/chiffons-guenilles-trois-rivieres/", en="/en/rags-trois-rivieres/", core=False, img=BAG, far=True, dist=130,
  hoods=["Trois-Rivières", "Cap-de-la-Madeleine", "Bécancour", "Shawinigan", "le reste de la Mauricie"],
  intro_fr="Trois-Rivières est à environ 130 km de Laval. Les zones industrielles de la Mauricie et de Bécancour utilisent de grandes quantités de chiffons : nous y livrons à partir de 1 000 lb.",
  intro_en="Trois-Rivières is about 130 km from Laval. Industrial areas in Mauricie and Bécancour use large volumes of rags: we deliver from 1,000 lb.",
  ind_fr="usines, ateliers d'usinage, garages et entrepreneurs industriels",
  ind_en="plants, machine shops, garages and industrial contractors",
  rel=["industrie", "usinage", "ville-quebec"]),
 dict(key="ville-gatineau", name="Gatineau", fr="/chiffons-guenilles-gatineau/", en="/en/rags-gatineau/", core=False, img=BAGS, far=True, dist=190,
  hoods=["Hull", "Aylmer", "Gatineau", "Buckingham", "Masson-Angers", "le reste de l'Outaouais"],
  intro_fr="Gatineau et l'Outaouais sont à environ 190 km de Laval. Nous y livrons par commandes de 1 000 lb ou plus, pour les entreprises et les distributeurs de la région.",
  intro_en="Gatineau and the Outaouais are about 190 km from Laval. We deliver orders of 1,000 lb or more to businesses and distributors in the region.",
  ind_fr="garages, entreprises d'entretien, entrepreneurs et distributeurs",
  ind_en="garages, cleaning companies, contractors and distributors",
  rel=["gros", "entretien", "livraison"]),
]

def _lst(xs, last): return ", ".join(xs[:-1]) + f" {last} " + xs[-1] if len(xs) > 1 else xs[0]

def _page(d):
    n = d["name"]; ne = d.get("name_en", n); core = d["core"]
    a_fr = "à " + n if not n.startswith("la ") else "sur " + n
    a_en = "in " + ne
    if core:
        terms_fr = f"Les frais et les conditions de livraison {a_fr} dépendent de votre adresse et de la quantité. Ils sont indiqués dans votre soumission."
        terms_en = f"Delivery fees and terms {a_en} depend on your address and quantity. They're shown in your quote."
    else:
        terms_fr = f"Livraison {a_fr} à partir de 1 000 lb (40 sacs de 25 lb), produits mélangés acceptés. Les frais dépendent de la distance et sont indiqués dans votre soumission."
        terms_en = f"Delivery {a_en} from 1,000 lb (40 bags of 25 lb), mixed products welcome. Fees depend on distance and are shown in your quote."
    hoods_fr, hoods_en = _lst(d["hoods"], "et"), _lst(d["hoods"], "and")
    body = lambda lang: (f"""<h2>Livraison {a_fr}</h2>
<p>{d['intro_fr']}</p>
<p>{terms_fr}</p>
<h2>Secteurs desservis</h2>
<p>Nous livrons {a_fr}, notamment à {hoods_fr}.</p>
<h2>Pour quelles entreprises</h2>
<p>Nos chiffons servent aux {d['ind_fr']}. Voir nos pages <a href="{{{{garage}}}}">garages</a>, <a href="{{{{entretien}}}}">entretien ménager</a>, <a href="{{{{construction}}}}">chantiers</a> et <a href="{{{{industrie}}}}">industrie</a>.</p>
<h2>Nos chiffons et nos prix</h2>
<ul><li><a href="{{{{couleur}}}}">T-shirt ou ratine couleur</a> : 32 $ le [pack], pour l'huile, la graisse et l'usage général.</li>
<li><a href="{{{{blancs}}}}">T-shirt ou ratine blanc</a> : 42 $ le [pack], sans transfert de couleur, pour la finition et la peinture.</li></ul>
<p>Prix avant taxes (TPS et TVQ en sus), quantité illimitée. Commande confirmée et payée une semaine avant la livraison.</p>
<h2>Commander</h2>
<p>Demandez une <a href="{{{{home#devis}}}}">soumission en ligne</a>, appelez le 438-831-3611 ou écrivez à info@entretienlaval.ca. Indiquez votre adresse {a_fr} et la quantité souhaitée.</p>""" if lang == "fr" else f"""<h2>Delivery {a_en}</h2>
<p>{d['intro_en']}</p>
<p>{terms_en}</p>
<h2>Areas we serve</h2>
<p>We deliver {a_en}, including {hoods_en}.</p>
<h2>Who uses our rags</h2>
<p>Our rags are used by {d['ind_en']}. See our pages for <a href="{{{{garage}}}}">garages</a>, <a href="{{{{entretien}}}}">janitorial</a>, <a href="{{{{construction}}}}">job sites</a> and <a href="{{{{industrie}}}}">industry</a>.</p>
<h2>Our rags and prices</h2>
<ul><li><a href="{{{{couleur}}}}">Colored T-shirt or terry</a>: $32 per [pack], for oil, grease and general use.</li>
<li><a href="{{{{blancs}}}}">White T-shirt or terry</a>: $42 per [pack], no color transfer, for finishing and painting.</li></ul>
<p>Prices before tax (GST and QST extra), no quantity limit. Orders are confirmed and paid one week before delivery.</p>
<h2>How to order</h2>
<p>Request a <a href="{{{{home#devis}}}}">quote online</a>, call 438-831-3611 or email info@entretienlaval.ca. Include your address {a_en} and the quantity you need.</p>""")
    lab_fr = "Guenilles et chiffons " + ("à " + n if not n.startswith("la ") else "sur " + n)
    return {"kind": "city", "img": d["img"], "rel": d["rel"], "city": n, "city_en": ne, "core": core,
     "fr": {"path": d["fr"], "short": n[0].upper() + n[1:],
      "title": (f"Chiffons d'essuyage et guenilles {a_fr} – livraison" if len(n) < 20 else f"Chiffons d'essuyage et guenilles {a_fr}"),
      "desc": f"Guenilles et chiffons d'essuyage recyclés livrés {a_fr} : t-shirt ou ratine, couleur ou blanc, dès 32 $ le sac de 25 lb." + ("" if core else " Minimum 1 000 lb."),
      "eyebrow": "Livraison · " + n, "h1": lab_fr,
      "lede": f"Chiffons de coton recyclé, lavés, triés et traités contre les punaises, livrés {a_fr} en [packs].",
      "card": ("Livraison selon votre adresse." if core else "Livraison à partir de 1 000 lb.") + " " + ", ".join(d["hoods"][:3]) + "…",
      "alt": f"Sac de chiffons recyclés de 25 lb livré {a_fr}", "body": body("fr"),
      "faq": [(f"Livrez-vous {a_fr}?", f"Oui. Nous livrons {a_fr}, notamment à {_lst(d['hoods'][:3], 'et')}. {terms_fr}"),
              (f"Combien coûte la livraison {a_fr}?", f"Les frais de livraison {a_fr} dépendent de l'adresse exacte et de la quantité. Ils sont indiqués dans la soumission, avant toute commande."),
              (f"Quel chiffon choisir pour une entreprise {a_fr}?", "Le t-shirt couleur (32 $ le [pack]) convient à la plupart des usages. La ratine retient plus d'huile et de liquide. Le blanc (42 $) évite le transfert de couleur pour la peinture et la finition.")]},
     "en": {"path": d["en"], "short": ne[0].upper() + ne[1:],
      "title": f"Wiping rags and shop rags {a_en} – delivery",
      "desc": f"Recycled wiping rags and shop rags delivered {a_en}: T-shirt or terry, colored or white, from $32 per 25 lb bag." + ("" if core else " 1,000 lb minimum."),
      "eyebrow": "Delivery · " + ne.replace("the ", "").title() if ne.startswith("the ") else "Delivery · " + ne, "h1": f"Rags and shop rags {a_en}",
      "lede": f"Recycled cotton rags, washed, sorted and bedbug-treated, delivered {a_en} in [packs].",
      "card": ("Delivery based on your address." if core else "Delivery from 1,000 lb.") + " " + ", ".join(d["hoods"][:3]) + "…",
      "alt": f"25 lb bag of recycled rags delivered {a_en}", "body": body("en"),
      "faq": [(f"Do you deliver {a_en}?", f"Yes. We deliver {a_en}, including {_lst(d['hoods'][:3], 'and')}. {terms_en}"),
              (f"How much is delivery {a_en}?", f"Delivery fees {a_en} depend on the exact address and quantity. They're shown in the quote, before you order."),
              (f"Which rag should a business {a_en} choose?", "Colored T-shirt rags ($32 per [pack]) suit most uses. Terry holds more oil and liquid. White rags ($42) avoid color transfer for painting and finishing.")]}}

CITY_PAGES = {d["key"]: _page(d) for d in C}
CITY_KEYS = list(CITY_PAGES)
