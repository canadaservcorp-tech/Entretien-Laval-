"""Additional industry pages (same structure as the sector pages in content.py)."""
BAG, BAGS, BALE, SHOP, TEXT = ("sac-chiffons-t-shirt-couleur-25-lb.webp", "sacs-chiffons-couleur-25-lb.webp",
    "balle-compressee-de-chiffons-eco-en-textiles-recyc.webp", "sac-de-chiffons-d-atelier-conditionnes-prets-a-l-u.webp", "textiles-de-coton-recuperes.webp")
P = {}

def S(key, img, rel, fr, en):
    P[key] = {"kind": "sector", "img": img, "rel": rel, "fr": fr, "en": en}

S("carrosserie", SHOP, ["peinture", "blancs", "garage"],
 {"path": "/chiffons-carrosserie-debosselage/", "short": "Carrosserie",
  "title": "Chiffons pour carrosserie et débosselage – sacs de 25 lb",
  "desc": "Chiffons recyclés pour ateliers de carrosserie : dégraissage, ponçage, nettoyage de pistolets et d'outils. Blanc ou couleur, dès 32 $ le sac de 25 lb.",
  "eyebrow": "Carrosserie · débosselage · peinture auto", "h1": "Chiffons pour ateliers de carrosserie",
  "lede": "Pour dégraisser, essuyer la poussière de ponçage et nettoyer pistolets et outils, en [packs].",
  "card": "Dégraissage, ponçage, pistolets : le blanc pour les surfaces, la couleur pour le reste.",
  "alt": "Chiffons d'atelier pour carrosserie",
  "body": """<h2>À quoi servent nos chiffons en carrosserie</h2>
<ul><li><b>Dégraissage</b> des panneaux avant l'apprêt, avec votre solvant habituel.</li>
<li><b>Poussière de ponçage</b> et nettoyage des surfaces entre les étapes.</li>
<li><b>Pistolets, godets et outils</b> : nettoyage après chaque couleur.</li>
<li><b>Mains, établis et planchers</b> de l'atelier.</li></ul>
<h2>Blanc ou couleur?</h2>
<p>Sur une surface prête à peindre, prenez le <a href="{{blancs}}">t-shirt blanc</a> (42 $ le [pack]) : il ne laisse pas de teinture sur le panneau. Pour les outils, les pistolets et le plancher, le <a href="{{couleur}}">chiffon couleur</a> à 32 $ suffit.</p>
<p>Juste avant la couche de peinture, la plupart des carrossiers utilisent un chiffon collant (tack cloth) spécialisé. Nos chiffons servent à toutes les autres étapes.</p>
<h2>Solvants et sécurité</h2>
<p>Les chiffons imbibés de diluant ou de solvant doivent aller dans un contenant métallique fermé. Voir le guide <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>""",
  "faq": [("Vos chiffons laissent-ils des peluches sur la peinture?", "Le t-shirt blanc trié est peu pelucheux et convient au dégraissage. Pour la dernière étape avant la peinture, un chiffon collant spécialisé reste préférable."),
          ("Quel format pour un atelier de carrosserie?", "Beaucoup d'ateliers gardent un mélange : quelques [packs] de blanc pour les surfaces et de la couleur pour les outils et le nettoyage.")]},
 {"path": "/en/auto-body-shop-rags/", "short": "Auto body",
  "title": "Rags for auto body and collision shops – 25 lb bags",
  "desc": "Recycled rags for auto body shops: degreasing, sanding dust, spray gun and tool cleaning. White or colored, from $32 per 25 lb bag.",
  "eyebrow": "Auto body · collision · refinishing", "h1": "Rags for auto body shops",
  "lede": "For degreasing panels, wiping sanding dust and cleaning spray guns and tools, in [packs].",
  "card": "Degreasing, sanding, spray guns: white for surfaces, colored for everything else.",
  "alt": "Shop rags for auto body work",
  "body": """<h2>What body shops use our rags for</h2>
<ul><li><b>Degreasing</b> panels before primer, with your usual solvent.</li>
<li><b>Sanding dust</b> and surface cleanup between steps.</li>
<li><b>Spray guns, cups and tools</b>: cleanup after each color.</li>
<li><b>Hands, benches and floors</b> in the shop.</li></ul>
<h2>White or colored?</h2>
<p>On a surface that's ready for paint, use <a href="{{blancs}}">white T-shirt rags</a> ($42 per [pack]): they leave no dye on the panel. For tools, guns and floors, <a href="{{couleur}}">colored rags</a> at $32 are enough.</p>
<p>Right before the paint coat, most painters use a dedicated tack cloth. Our rags cover every other step.</p>
<h2>Solvents and safety</h2>
<p>Rags soaked with thinner or solvent belong in a closed metal container. See the guide <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>""",
  "faq": [("Do your rags leave lint on paint?", "Sorted white T-shirt rags are low-lint and work well for degreasing. For the last wipe before paint, a dedicated tack cloth is still best."),
          ("What should a body shop order?", "Many shops keep a mix: a few [packs] of white for surfaces and colored rags for tools and cleanup.")]})

S("esthetique-auto", BAG, ["carrosserie", "blancs", "garage"],
 {"path": "/chiffons-esthetique-automobile-lave-auto/", "short": "Esthétique auto et lave-auto",
  "title": "Chiffons pour esthétique automobile et lave-auto",
  "desc": "Guenilles recyclées pour esthéticiens auto et lave-autos : jantes, pneus, moteur, cadres de portes. Dès 32 $ le sac de 25 lb, livrées au Québec.",
  "eyebrow": "Esthétique automobile · lave-auto", "h1": "Chiffons pour l'esthétique automobile et les lave-autos",
  "lede": "Pour les jantes, les pneus, le compartiment moteur et les cadres de portes, en [packs]. Vos microfibres restent pour la peinture.",
  "card": "Jantes, pneus, moteur, cadres de portes : gardez vos microfibres pour la peinture.",
  "alt": "Sac de chiffons recyclés pour esthétique automobile",
  "body": """<h2>Où un chiffon recyclé fait mieux qu'une microfibre</h2>
<p>Les microfibres coûtent cher et s'abîment vite sur les surfaces sales. Pour les tâches salissantes, un chiffon recyclé fait le travail et se jette sans regret :</p>
<ul><li>Jantes, pneus et passages de roues.</li>
<li>Compartiment moteur, graisse et huile.</li>
<li>Cadres de portes, seuils et coffre.</li>
<li>Nettoyage des seaux, des outils et de l'aire de lavage.</li></ul>
<h2>Et sur la peinture?</h2>
<p>Pour le séchage et le polissage de la peinture, la plupart des esthéticiens préfèrent la microfibre. Si vous utilisez du coton, prenez le <a href="{{blancs}}">t-shirt blanc</a>, sans transfert de couleur.</p>
<h2>Quel produit choisir</h2>
<p>La <a href="{{couleur}}">ratine couleur</a> (32 $ le [pack]) absorbe beaucoup d'eau et de saleté pour les jantes et le moteur. Le t-shirt couleur convient aux intérieurs et aux plastiques.</p>""",
  "faq": [("Les chiffons recyclés peuvent-ils rayer la peinture?", "Tout chiffon peut rayer s'il traîne de la saleté. Sur la peinture, utilisez un chiffon propre et doux comme le t-shirt blanc, ou une microfibre."),
          ("Peut-on laver les chiffons d'un lave-auto?", "Oui, s'ils ne sont pas imbibés de solvant. Lavez-les à part, sans assouplissant, qui réduit l'absorption.")]},
 {"path": "/en/car-detailing-car-wash-rags/", "short": "Car detailing and car wash",
  "title": "Rags for car detailing and car washes – 25 lb bags",
  "desc": "Recycled rags for detailers and car washes: wheels, tires, engine bays, door jambs. From $32 per 25 lb bag, delivered in Québec.",
  "eyebrow": "Car detailing · car wash", "h1": "Rags for car detailing and car washes",
  "lede": "For wheels, tires, engine bays and door jambs, in [packs]. Save your microfibers for the paint.",
  "card": "Wheels, tires, engine bays, door jambs: save your microfibers for the paint.",
  "alt": "Bag of recycled rags for car detailing",
  "body": """<h2>Where a recycled rag beats a microfiber</h2>
<p>Microfibers are expensive and get ruined quickly on dirty surfaces. For the messy jobs, a recycled rag does the work and you can toss it without regret:</p>
<ul><li>Wheels, tires and wheel wells.</li>
<li>Engine bays, grease and oil.</li>
<li>Door jambs, sills and trunks.</li>
<li>Cleaning buckets, tools and the wash bay.</li></ul>
<h2>What about the paint?</h2>
<p>For drying and polishing paint, most detailers prefer microfiber. If you use cotton, choose <a href="{{blancs}}">white T-shirt rags</a>, with no color transfer.</p>
<h2>Which product to choose</h2>
<p><a href="{{couleur}}">Colored terry</a> ($32 per [pack]) absorbs lots of water and grime for wheels and engines. Colored T-shirt rags suit interiors and plastics.</p>""",
  "faq": [("Can recycled rags scratch paint?", "Any cloth can scratch if it drags dirt. On paint, use a clean, soft rag like white T-shirt, or a microfiber."),
          ("Can car wash rags be laundered?", "Yes, if they aren't soaked with solvent. Wash them separately and skip fabric softener, which reduces absorbency.")]})

S("ebenisterie", SHOP, ["guide-huileux", "peinture", "blancs"],
 {"path": "/chiffons-ebenisterie-menuiserie/", "short": "Ébénisterie et menuiserie",
  "title": "Chiffons pour ébénisterie, teinture et huile de finition",
  "desc": "Chiffons de coton recyclé pour ébénistes et menuisiers : teinture, huile de lin, vernis, essuyage. T-shirt blanc sans transfert, dès 32 $ le sac de 25 lb.",
  "eyebrow": "Ébénisterie · menuiserie · finition du bois", "h1": "Chiffons pour l'ébénisterie et la finition du bois",
  "lede": "Pour appliquer et essuyer teintures, huiles et vernis, en [packs]. Le t-shirt blanc ne laisse pas de couleur sur le bois.",
  "card": "Teinture, huile de lin, vernis : le t-shirt blanc, sans transfert de couleur.",
  "alt": "Chiffons d'atelier pour la finition du bois",
  "body": """<h2>Le bon chiffon pour la finition</h2>
<p>Pour appliquer une teinture ou une huile, et pour essuyer l'excédent, il faut un coton doux qui ne déteint pas. Le <a href="{{blancs}}">t-shirt blanc</a> (42 $ le [pack]) est fait pour ça. Pour le nettoyage de l'atelier et des outils, le <a href="{{couleur}}">chiffon couleur</a> à 32 $ suffit.</p>
<h2>Attention : huile de lin et combustion spontanée</h2>
<p>Les chiffons imbibés d'huile de lin, d'huile de tung ou de teinture à l'huile peuvent <b>s'enflammer tout seuls</b> en séchant en tas. Étalez-les à plat pour sécher, à l'extérieur, ou mettez-les dans un contenant métallique fermé rempli d'eau. Tout est expliqué dans le guide <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>
<h2>Pour quels ateliers</h2>
<p>Ébénistes, fabricants d'armoires et de meubles, menuisiers, restaurateurs de meubles et entrepreneurs en planchers de bois.</p>""",
  "faq": [("Quel chiffon pour appliquer une teinture?", "Le t-shirt blanc : doux, absorbant, et sans transfert de couleur sur le bois."),
          ("Peut-on jeter un chiffon taché d'huile de lin à la poubelle?", "Pas tel quel : il peut s'enflammer. Faites-le sécher à plat à l'extérieur ou mettez-le dans un contenant métallique fermé avec de l'eau, puis suivez les consignes de votre municipalité.")]},
 {"path": "/en/woodworking-cabinetmaking-rags/", "short": "Woodworking and cabinetmaking",
  "title": "Rags for woodworking, staining and oil finishes",
  "desc": "Recycled cotton rags for woodworkers and cabinetmakers: stain, linseed oil, varnish, wiping. White T-shirt with no color transfer, from $32 per 25 lb bag.",
  "eyebrow": "Woodworking · cabinetmaking · wood finishing", "h1": "Rags for woodworking and wood finishing",
  "lede": "For applying and wiping stains, oils and varnishes, in [packs]. White T-shirt rags leave no color on the wood.",
  "card": "Stain, linseed oil, varnish: white T-shirt rags with no color transfer.",
  "alt": "Shop rags for wood finishing",
  "body": """<h2>The right rag for finishing</h2>
<p>To apply stain or oil and wipe off the excess, you need soft cotton that won't bleed. <a href="{{blancs}}">White T-shirt rags</a> ($42 per [pack]) are made for it. For shop and tool cleanup, <a href="{{couleur}}">colored rags</a> at $32 are enough.</p>
<h2>Warning: linseed oil and spontaneous combustion</h2>
<p>Rags soaked with linseed oil, tung oil or oil-based stain can <b>catch fire on their own</b> when they dry in a pile. Lay them flat to dry outdoors, or put them in a closed metal container filled with water. The full explanation is in the guide <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>
<h2>Which shops</h2>
<p>Cabinetmakers, furniture and kitchen cabinet makers, carpenters, furniture restorers and hardwood floor contractors.</p>""",
  "faq": [("Which rag should I use to apply stain?", "White T-shirt rags: soft, absorbent and no color transfer onto the wood."),
          ("Can I throw a linseed-oil rag in the trash?", "Not as is: it can ignite. Dry it flat outdoors or put it in a closed metal container with water, then follow your municipality's rules.")]})

S("plomberie-cvac", BALE, ["construction", "couleur", "usinage"],
 {"path": "/chiffons-plomberie-cvac/", "short": "Plomberie et CVAC",
  "title": "Chiffons pour plombiers et techniciens CVAC – 25 lb",
  "desc": "Guenilles recyclées pour plomberie, chauffage, ventilation et climatisation : joints, huile de filetage, purges, fuites. Dès 32 $ le sac de 25 lb.",
  "eyebrow": "Plomberie · chauffage · ventilation · climatisation", "h1": "Chiffons pour la plomberie et le CVAC",
  "lede": "Pour essuyer les joints, l'huile de filetage, les purges et les fuites, en [packs]. Un sac par camion, et on n'en manque plus.",
  "card": "Joints, huile de filetage, purges et fuites : un sac par camion.",
  "alt": "Chiffons recyclés compressés pour plombiers",
  "body": """<h2>Les usages au quotidien</h2>
<ul><li>Essuyer les tuyaux et raccords avant le collage ou la soudure.</li>
<li>Huile de coupe et de filetage.</li>
<li>Purges de radiateurs, de chauffe-eau et de systèmes de chauffage.</li>
<li>Petites fuites, condensat et protection des planchers chez le client.</li></ul>
<h2>Quel chiffon choisir</h2>
<p>La <a href="{{couleur}}">ratine couleur</a> (32 $ le [pack]) est épaisse et absorbe beaucoup d'eau : idéale pour les purges et les fuites. Le t-shirt couleur, plus souple, sert pour les mains et les raccords.</p>
<h2>Pour les flottes de camions</h2>
<p>Une entreprise avec plusieurs camions peut commander en volume et répartir les sacs. Voir les <a href="{{gros}}">prix en gros</a> et la <a href="{{livraison}}">livraison</a>.</p>""",
  "faq": [("Quel chiffon pour absorber l'eau d'une purge?", "La ratine (tissu éponge) : c'est la plus absorbante de nos options."),
          ("Livrez-vous à notre entrepôt pour toute la flotte?", "Oui, nous livrons à l'adresse de votre entreprise. Les frais dépendent de l'emplacement et de la quantité.")]},
 {"path": "/en/plumbing-hvac-rags/", "short": "Plumbing and HVAC",
  "title": "Rags for plumbers and HVAC technicians – 25 lb bags",
  "desc": "Recycled rags for plumbing, heating, ventilation and air conditioning: joints, threading oil, bleeding, leaks. From $32 per 25 lb bag.",
  "eyebrow": "Plumbing · heating · ventilation · A/C", "h1": "Rags for plumbing and HVAC",
  "lede": "For wiping joints, threading oil, bleeding systems and leaks, in [packs]. One bag per truck and you never run out.",
  "card": "Joints, threading oil, bleeding and leaks: one bag per truck.",
  "alt": "Compressed recycled rags for plumbers",
  "body": """<h2>Everyday uses</h2>
<ul><li>Wiping pipes and fittings before gluing or soldering.</li>
<li>Cutting and threading oil.</li>
<li>Bleeding radiators, water heaters and heating systems.</li>
<li>Small leaks, condensate and protecting customers' floors.</li></ul>
<h2>Which rag to choose</h2>
<p><a href="{{couleur}}">Colored terry</a> ($32 per [pack]) is thick and soaks up lots of water: ideal for bleeding and leaks. Softer colored T-shirt rags work for hands and fittings.</p>
<h2>For truck fleets</h2>
<p>A company with several trucks can order in volume and split the bags. See <a href="{{gros}}">wholesale pricing</a> and <a href="{{livraison}}">delivery</a>.</p>""",
  "faq": [("Which rag soaks up water from bleeding a system?", "Terry (towel cloth): it's our most absorbent option."),
          ("Do you deliver to our shop for the whole fleet?", "Yes, we deliver to your business address. Fees depend on location and quantity.")]})

S("marine", BAGS, ["garage", "couleur", "guide-ranger"],
 {"path": "/chiffons-marinas-bateaux/", "short": "Marinas et bateaux",
  "title": "Chiffons pour marinas, bateaux et mécanique marine",
  "desc": "Chiffons recyclés pour marinas et mécanique marine : moteurs hors-bord, huile, carburant, entretien de coques et de ponts. Dès 32 $ le sac de 25 lb.",
  "eyebrow": "Marinas · mécanique marine · plaisance", "h1": "Chiffons pour marinas et bateaux",
  "lede": "Pour l'entretien des moteurs, l'huile, le carburant et le nettoyage des coques et des ponts, en [packs].",
  "card": "Moteurs, huile, carburant, coques : pour la saison et l'hivernage.",
  "alt": "Sacs de chiffons recyclés pour marinas",
  "body": """<h2>De la mise à l'eau à l'hivernage</h2>
<p>Une marina utilise beaucoup de chiffons au printemps et à l'automne : vidanges d'huile, entretien des moteurs hors-bord et intérieurs, carburant renversé, nettoyage des coques, des ponts et des cales.</p>
<h2>Quel chiffon choisir</h2>
<p>La <a href="{{couleur}}">ratine couleur</a> (32 $ le [pack]) pour l'huile, le carburant et l'eau. Le <a href="{{blancs}}">t-shirt blanc</a> (42 $) pour le gelcoat, le vernis et les surfaces de finition.</p>
<h2>Protéger l'eau</h2>
<p>Ne jetez jamais un chiffon souillé à l'eau ni dans une poubelle ouverte au quai. Gardez les chiffons imbibés de carburant ou d'huile dans un contenant métallique fermé, puis apportez-les à un point de collecte approprié. Voir le guide <a href="{{guide-ranger}}">ranger, laver et jeter ses chiffons</a>.</p>""",
  "faq": [("Pouvez-vous livrer avant la saison?", "Oui. Commandez au moins une semaine d'avance : la commande est confirmée et payée une semaine avant la livraison."),
          ("Quel chiffon pour le gelcoat?", "Le t-shirt blanc, doux et sans transfert de couleur.")]},
 {"path": "/en/marina-boat-rags/", "short": "Marinas and boats",
  "title": "Rags for marinas, boats and marine mechanics",
  "desc": "Recycled rags for marinas and marine mechanics: outboard motors, oil, fuel, hull and deck cleaning. From $32 per 25 lb bag.",
  "eyebrow": "Marinas · marine mechanics · boating", "h1": "Rags for marinas and boats",
  "lede": "For engine maintenance, oil, fuel and hull and deck cleaning, in [packs].",
  "card": "Engines, oil, fuel, hulls: for launch season and winterizing.",
  "alt": "Bags of recycled rags for marinas",
  "body": """<h2>From launch to winterizing</h2>
<p>A marina goes through a lot of rags in spring and fall: oil changes, outboard and inboard motor maintenance, fuel spills, and cleaning hulls, decks and bilges.</p>
<h2>Which rag to choose</h2>
<p><a href="{{couleur}}">Colored terry</a> ($32 per [pack]) for oil, fuel and water. <a href="{{blancs}}">White T-shirt rags</a> ($42) for gelcoat, varnish and finish surfaces.</p>
<h2>Protect the water</h2>
<p>Never throw a dirty rag in the water or in an open bin on the dock. Keep fuel- or oil-soaked rags in a closed metal container, then take them to a proper collection point. See the guide <a href="{{guide-ranger}}">storing, washing and disposing of rags</a>.</p>""",
  "faq": [("Can you deliver before the season starts?", "Yes. Order at least a week ahead: orders are confirmed and paid one week before delivery."),
          ("Which rag for gelcoat?", "White T-shirt rags: soft, with no color transfer.")]})

S("agriculture", BALE, ["garage", "gros", "ville-rive-nord"],
 {"path": "/chiffons-fermes-machinerie-agricole/", "short": "Fermes et machinerie agricole",
  "title": "Chiffons pour fermes et machinerie agricole – en gros",
  "desc": "Guenilles recyclées pour fermes et concessionnaires de machinerie agricole : graissage, huile hydraulique, entretien des tracteurs. Dès 32 $ le sac de 25 lb.",
  "eyebrow": "Fermes · machinerie agricole", "h1": "Chiffons pour les fermes et la machinerie agricole",
  "lede": "Pour le graissage, l'huile hydraulique et l'entretien des tracteurs et de l'équipement, en [packs].",
  "card": "Graissage, huile hydraulique, tracteurs : en volume pour la saison.",
  "alt": "Chiffons compressés pour fermes",
  "body": """<h2>L'entretien de l'équipement</h2>
<p>Graissage des points de pivot, vidanges, huile hydraulique, nettoyage des filtres et des moteurs : la machinerie agricole demande beaucoup de chiffons, surtout avant les semences et les récoltes.</p>
<h2>Quel chiffon choisir</h2>
<p>La <a href="{{couleur}}">ratine couleur</a> (32 $ le [pack]) est la plus économique pour l'huile et la graisse. Commandez en volume avant la saison : voir les <a href="{{gros}}">prix en gros</a>.</p>
<h2>Livraison en région</h2>
<p>Nous livrons partout au Québec à partir de 1 000 lb (40 sacs). Les fermes voisines peuvent regrouper une commande à une même adresse. Voir les <a href="{{livraison}}">conditions de livraison</a>.</p>""",
  "faq": [("Livrez-vous à la ferme?", "Oui, à partir de 1 000 lb par livraison hors Laval et Montréal. Les frais dépendent de la distance."),
          ("Peut-on utiliser ces chiffons pour les animaux ou les aliments?", "Non. Nos chiffons sont faits pour l'essuyage de la machinerie, des outils et des surfaces.")]},
 {"path": "/en/farm-machinery-rags/", "short": "Farms and farm machinery",
  "title": "Rags for farms and farm machinery – bulk 25 lb bags",
  "desc": "Recycled rags for farms and farm equipment dealers: greasing, hydraulic oil, tractor maintenance. From $32 per 25 lb bag.",
  "eyebrow": "Farms · farm machinery", "h1": "Rags for farms and farm machinery",
  "lede": "For greasing, hydraulic oil and tractor and equipment maintenance, in [packs].",
  "card": "Greasing, hydraulic oil, tractors: in volume for the season.",
  "alt": "Compressed rags for farms",
  "body": """<h2>Equipment maintenance</h2>
<p>Greasing pivot points, oil changes, hydraulic oil, cleaning filters and engines: farm machinery uses a lot of rags, especially before planting and harvest.</p>
<h2>Which rag to choose</h2>
<p><a href="{{couleur}}">Colored terry</a> ($32 per [pack]) is the most economical for oil and grease. Order in volume before the season: see <a href="{{gros}}">wholesale pricing</a>.</p>
<h2>Delivery to rural areas</h2>
<p>We deliver anywhere in Québec from 1,000 lb (40 bags). Neighbouring farms can combine an order to a single address. See the <a href="{{livraison}}">delivery terms</a>.</p>""",
  "faq": [("Do you deliver to farms?", "Yes, from 1,000 lb per delivery outside Laval and Montréal. Fees depend on distance."),
          ("Can these rags be used for animals or food?", "No. Our rags are made for wiping machinery, tools and surfaces.")]})

S("usinage", BAG, ["industrie", "gros", "guide-ratine"],
 {"path": "/chiffons-usinage-atelier-machinerie/", "short": "Usinage et ateliers",
  "title": "Chiffons pour ateliers d'usinage et de fabrication",
  "desc": "Chiffons recyclés pour ateliers d'usinage, soudure et fabrication métallique : huile de coupe, refroidissement, entretien des machines. Dès 32 $ le sac.",
  "eyebrow": "Usinage · soudure · fabrication métallique", "h1": "Chiffons pour l'usinage et la fabrication",
  "lede": "Pour l'huile de coupe, le liquide de refroidissement et l'entretien des machines-outils, en [packs].",
  "card": "Huile de coupe, liquide de refroidissement, machines-outils.",
  "alt": "Sac de chiffons pour atelier d'usinage",
  "body": """<h2>Dans un atelier d'usinage</h2>
<ul><li>Essuyer les pièces après l'usinage, avant la mesure ou l'inspection.</li>
<li>Huile de coupe et liquide de refroidissement autour des tours et des centres d'usinage.</li>
<li>Entretien des glissières, des étaux et des outils.</li>
<li>Mains, établis et planchers.</li></ul>
<h2>Quel chiffon choisir</h2>
<p>La <a href="{{couleur}}">ratine couleur</a> retient le plus de liquide. Le t-shirt couleur est plus souple pour les pièces. Les deux coûtent 32 $ le [pack]. Pour comparer, voir le guide <a href="{{guide-ratine}}">ratine ou t-shirt</a>.</p>
<h2>Attention aux copeaux</h2>
<p>Un chiffon qui a servi près d'une machine peut contenir des copeaux de métal coupants. Ne l'utilisez pas ensuite sur les mains ou une surface délicate.</p>""",
  "faq": [("Combien de sacs par mois pour un atelier?", "Cela dépend du nombre de postes et du type de travail. Notre <a href=\"{{calculateur}}\">calculateur</a> vous aide à estimer votre budget à partir de votre consommation."),
          ("Livrez-vous les zones industrielles?", "Oui, à l'adresse de votre entreprise. Hors Laval et Montréal, le minimum est de 1 000 lb par livraison.")]},
 {"path": "/en/machine-shop-rags/", "short": "Machine shops and fabrication",
  "title": "Rags for machine shops and metal fabrication",
  "desc": "Recycled rags for machine shops, welding and metal fabrication: cutting oil, coolant, machine maintenance. From $32 per 25 lb bag.",
  "eyebrow": "Machining · welding · metal fabrication", "h1": "Rags for machine shops and fabrication",
  "lede": "For cutting oil, coolant and machine tool maintenance, in [packs].",
  "card": "Cutting oil, coolant, machine tools.",
  "alt": "Bag of rags for a machine shop",
  "body": """<h2>In a machine shop</h2>
<ul><li>Wiping parts after machining, before measuring or inspection.</li>
<li>Cutting oil and coolant around lathes and machining centers.</li>
<li>Maintaining ways, vises and tools.</li>
<li>Hands, benches and floors.</li></ul>
<h2>Which rag to choose</h2>
<p><a href="{{couleur}}">Colored terry</a> holds the most fluid. Colored T-shirt rags are softer for parts. Both cost $32 per [pack]. To compare, see the guide <a href="{{guide-ratine}}">terry vs T-shirt</a>.</p>
<h2>Watch out for chips</h2>
<p>A rag used near a machine can hold sharp metal chips. Don't reuse it on hands or a delicate surface.</p>""",
  "faq": [("How many bags per month for a shop?", "It depends on the number of stations and the type of work. Our <a href=\"{{calculateur}}\">calculator</a> helps you estimate your budget from your usage."),
          ("Do you deliver to industrial parks?", "Yes, to your business address. Outside Laval and Montréal, the minimum is 1,000 lb per delivery.")]})

S("municipal", BAGS, ["entretien", "garage", "gros"],
 {"path": "/chiffons-municipalites-ecoles/", "short": "Municipalités et écoles",
  "title": "Chiffons pour municipalités, écoles et travaux publics",
  "desc": "Chiffons recyclés pour garages municipaux, travaux publics, arénas, écoles et institutions. Facture avec TPS et TVQ, dès 32 $ le sac de 25 lb.",
  "eyebrow": "Municipalités · travaux publics · écoles · institutions", "h1": "Chiffons pour municipalités, écoles et institutions",
  "lede": "Pour les garages municipaux, les travaux publics, les arénas et l'entretien des écoles, en [packs].",
  "card": "Garages municipaux, arénas, conciergerie des écoles et institutions.",
  "alt": "Sacs de chiffons recyclés pour institutions",
  "body": """<h2>Où nos chiffons servent</h2>
<ul><li><b>Garages municipaux et travaux publics</b> : entretien des camions, de la machinerie et des équipements de déneigement.</li>
<li><b>Arénas et centres sportifs</b> : entretien des machines et des installations.</li>
<li><b>Écoles et institutions</b> : conciergerie et entretien des bâtiments.</li></ul>
<h2>Un choix qui réduit les déchets</h2>
<p>Nos chiffons sont faits de textiles récupérés qui auraient fini à l'enfouissement. Un argument concret pour vos objectifs de réduction des déchets. Voir aussi le guide <a href="{{guide-papier}}">chiffons recyclés ou papier</a>.</p>
<h2>Achat et facturation</h2>
<p>Nous fournissons une facture avec nos numéros de TPS et de TVQ. Les prix sont avant taxes. La commande est confirmée et payée une semaine avant la livraison. Demandez une <a href="{{home#devis}}">soumission</a> pour votre service.</p>""",
  "faq": [("Pouvez-vous fournir une soumission pour notre service d'achats?", "Oui. Demandez-la en ligne ou par courriel à info@entretienlaval.ca, avec la quantité et l'adresse de livraison."),
          ("Livrez-vous plusieurs bâtiments?", "Nous livrons à l'adresse indiquée dans la soumission. Pour plusieurs adresses, précisez-les dans votre demande.")]},
 {"path": "/en/municipal-school-maintenance-rags/", "short": "Municipalities and schools",
  "title": "Rags for municipalities, schools and public works",
  "desc": "Recycled rags for municipal garages, public works, arenas, schools and institutions. Invoice with GST and QST, from $32 per 25 lb bag.",
  "eyebrow": "Municipalities · public works · schools · institutions", "h1": "Rags for municipalities, schools and institutions",
  "lede": "For municipal garages, public works, arenas and school maintenance, in [packs].",
  "card": "Municipal garages, arenas, school and institutional custodial work.",
  "alt": "Bags of recycled rags for institutions",
  "body": """<h2>Where our rags are used</h2>
<ul><li><b>Municipal garages and public works</b>: trucks, machinery and snow-removal equipment.</li>
<li><b>Arenas and sports centers</b>: machine and facility maintenance.</li>
<li><b>Schools and institutions</b>: custodial and building maintenance.</li></ul>
<h2>A choice that cuts waste</h2>
<p>Our rags are made from reclaimed textiles that would otherwise go to landfill: a concrete point for your waste-reduction goals. See also the guide <a href="{{guide-papier}}">recycled rags vs paper</a>.</p>
<h2>Purchasing and invoicing</h2>
<p>We provide an invoice with our GST and QST numbers. Prices are before tax. Orders are confirmed and paid one week before delivery. Request a <a href="{{home#devis}}">quote</a> for your department.</p>""",
  "faq": [("Can you provide a quote for our purchasing department?", "Yes. Request it online or by email at info@entretienlaval.ca, with the quantity and delivery address."),
          ("Do you deliver to several buildings?", "We deliver to the address in the quote. For several addresses, list them in your request.")]})

SECTOR2_PAGES = P
SECTOR2_KEYS = list(P)
