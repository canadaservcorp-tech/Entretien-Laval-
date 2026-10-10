"""Extra guides: terry vs T-shirt, storing/washing rags, Québec rag glossary, budget calculator."""
BAG, SHOP, TEXT = "sac-chiffons-t-shirt-couleur-25-lb.webp", "sac-de-chiffons-d-atelier-conditionnes-prets-a-l-u.webp", "textiles-de-coton-recuperes.webp"
P = {}

P["guide-ratine"] = {"kind": "guide", "img": BAG, "rel": ["couleur", "blancs", "garage"],
 "fr": {"path": "/guides/ratine-ou-t-shirt/", "short": "Ratine ou t-shirt : quel chiffon choisir",
  "title": "Chiffons ratine ou t-shirt : lequel choisir?",
  "desc": "Ratine (tissu éponge) ou jersey de t-shirt, blanc ou couleur : comparaison de l'absorption, de la douceur et des usages pour choisir le bon chiffon d'essuyage.",
  "eyebrow": "Guide · choisir", "h1": "Ratine ou t-shirt : quel chiffon d'essuyage choisir?",
  "lede": "Les deux sont en coton recyclé et coûtent le même prix en couleur. La différence : l'épaisseur et l'usage.",
  "card": "Absorption, douceur, usages : le comparatif pour bien choisir.", "alt": "Sac de chiffons t-shirt couleur",
  "body": """<h2>La ratine (tissu éponge)</h2>
<p>La ratine vient de serviettes et de draps de bain. Elle est épaisse, bouclée et retient beaucoup de liquide. C'est le choix pour l'huile, la graisse, l'eau et les gros dégâts.</p>
<h2>Le t-shirt (jersey)</h2>
<p>Le jersey vient de t-shirts et de vêtements en coton tricoté. Il est mince, doux et souple, et laisse peu de peluches. C'est le chiffon tout usage : mains, outils, surfaces, nettoyage courant.</p>
<h2>Comparatif</h2>
<table><thead><tr><th></th><th>Ratine</th><th>T-shirt</th></tr></thead><tbody>
<tr><td>Épaisseur</td><td>Épaisse</td><td>Mince</td></tr>
<tr><td>Absorption</td><td>Très élevée</td><td>Bonne</td></tr>
<tr><td>Douceur</td><td>Moyenne</td><td>Élevée</td></tr>
<tr><td>Idéal pour</td><td>Huile, graisse, eau, déversements</td><td>Mains, outils, surfaces, polissage</td></tr></tbody></table>
<h2>Blanc ou couleur?</h2>
<p>La <a href="{{couleur}}">couleur</a> (32 $ le [pack]) convient à presque tout. Le <a href="{{blancs}}">blanc</a> (42 $) ne laisse pas de teinture : prenez-le pour la peinture, la teinture du bois, le vernis et les surfaces pâles.</p>""",
  "faq": [("La ratine laisse-t-elle plus de peluches?", "Un peu plus que le t-shirt, à cause de ses boucles. Pour les surfaces délicates, choisissez le t-shirt blanc."),
          ("Peut-on mélanger ratine et t-shirt dans une commande?", "Oui. Chaque [pack] contient un seul produit, mais vous pouvez commander plusieurs produits ensemble.")]},
 "en": {"path": "/en/guides/terry-vs-t-shirt-rags/", "short": "Terry vs T-shirt: which rag to choose",
  "title": "Terry vs T-shirt rags: which should you choose?",
  "desc": "Terry (towel cloth) or T-shirt jersey, white or colored: absorbency, softness and best uses compared, to choose the right wiping rag.",
  "eyebrow": "Guide · choosing", "h1": "Terry vs T-shirt: which wiping rag should you choose?",
  "lede": "Both are recycled cotton and cost the same in colored. The difference is thickness and use.",
  "card": "Absorbency, softness, uses: the comparison to choose well.", "alt": "Bag of colored T-shirt rags",
  "body": """<h2>Terry (towel cloth)</h2>
<p>Terry comes from bath towels and sheets. It's thick, looped and holds a lot of liquid. It's the pick for oil, grease, water and big spills.</p>
<h2>T-shirt (jersey)</h2>
<p>Jersey comes from T-shirts and knitted cotton clothing. It's thin, soft and flexible, and low-lint. It's the all-purpose rag: hands, tools, surfaces, everyday cleaning.</p>
<h2>Comparison</h2>
<table><thead><tr><th></th><th>Terry</th><th>T-shirt</th></tr></thead><tbody>
<tr><td>Thickness</td><td>Thick</td><td>Thin</td></tr>
<tr><td>Absorbency</td><td>Very high</td><td>Good</td></tr>
<tr><td>Softness</td><td>Medium</td><td>High</td></tr>
<tr><td>Best for</td><td>Oil, grease, water, spills</td><td>Hands, tools, surfaces, polishing</td></tr></tbody></table>
<h2>White or colored?</h2>
<p><a href="{{couleur}}">Colored</a> ($32 per [pack]) handles almost everything. <a href="{{blancs}}">White</a> ($42) leaves no dye: use it for paint, wood stain, varnish and light-colored surfaces.</p>""",
  "faq": [("Does terry leave more lint?", "A little more than T-shirt, because of its loops. For delicate surfaces, choose white T-shirt rags."),
          ("Can I mix terry and T-shirt in one order?", "Yes. Each [pack] holds one product, but you can order several products together.")]}}

P["guide-ranger"] = {"kind": "guide", "img": SHOP, "rel": ["guide-huileux", "garage", "marine"],
 "fr": {"path": "/guides/ranger-laver-reutiliser-chiffons/", "short": "Ranger, laver et jeter ses chiffons",
  "title": "Comment ranger, laver, réutiliser et jeter ses chiffons",
  "desc": "Ranger les chiffons propres et souillés, les laver sans perdre leur absorption, savoir quand les jeter et où les apporter au Québec (écocentre, collecte).",
  "eyebrow": "Guide · entretien", "h1": "Ranger, laver, réutiliser et jeter ses chiffons",
  "lede": "Bien rangés et bien lavés, vos chiffons durent plus longtemps. Bien jetés, ils ne causent ni incendie ni pollution.",
  "card": "Rangement, lavage sans assouplissant, et où jeter les chiffons souillés.", "alt": "Chiffons d'atelier rangés",
  "body": """<h2>Ranger les chiffons propres</h2>
<p>Gardez-les dans leur sac fermé ou un bac à couvercle, au sec, loin de la poussière et des produits chimiques. Un bac par poste de travail évite le gaspillage.</p>
<h2>Ranger les chiffons souillés</h2>
<p>Les chiffons imbibés d'huile, de solvant, de teinture ou de carburant vont dans un <b>contenant métallique fermé</b>, jamais en tas. Videz-le chaque jour. Pourquoi : voir <a href="{{guide-huileux}}">chiffons huileux et risque d'incendie</a>.</p>
<h2>Laver et réutiliser</h2>
<ul><li>Lavez seulement les chiffons <b>légèrement sales</b> : eau, poussière, produits ménagers doux.</li>
<li>Lavez-les à part, à l'eau chaude.</li>
<li><b>Pas d'assouplissant</b> : il réduit l'absorption du coton.</li>
<li>Ne mettez jamais à la sécheuse un chiffon qui a contenu de l'huile ou du solvant.</li></ul>
<h2>Quand et où les jeter</h2>
<p>Un chiffon déchiré ou imbibé d'un produit dangereux doit être jeté. Les chiffons contaminés par de la peinture, des solvants ou des huiles sont des résidus dangereux : les particuliers les apportent à un écocentre, et les entreprises passent par une entreprise de collecte spécialisée. Vérifiez les règles de votre municipalité.</p>""",
  "faq": [("Pourquoi éviter l'assouplissant?", "Il dépose une couche sur les fibres qui empêche le coton d'absorber. Vos chiffons essuieraient moins bien."),
          ("Un chiffon de ménage peut-il aller à la poubelle?", "Oui, s'il n'a servi qu'avec de l'eau ou des produits ménagers doux. S'il contient un produit dangereux, suivez les consignes de votre municipalité.")]},
 "en": {"path": "/en/guides/store-wash-reuse-rags/", "short": "Storing, washing and disposing of rags",
  "title": "How to store, wash, reuse and dispose of rags",
  "desc": "Storing clean and dirty rags, washing them without losing absorbency, knowing when to toss them and where to take them in Québec (ecocentre, specialized pickup).",
  "eyebrow": "Guide · care", "h1": "Storing, washing, reusing and disposing of rags",
  "lede": "Stored and washed well, your rags last longer. Disposed of well, they cause neither fires nor pollution.",
  "card": "Storage, washing without softener, and where to dispose of dirty rags.", "alt": "Stored shop rags",
  "body": """<h2>Storing clean rags</h2>
<p>Keep them in their closed bag or a lidded bin, dry, away from dust and chemicals. One bin per workstation avoids waste.</p>
<h2>Storing dirty rags</h2>
<p>Rags soaked with oil, solvent, stain or fuel go in a <b>closed metal container</b>, never in a pile. Empty it daily. Why: see <a href="{{guide-huileux}}">oily rags and fire risk</a>.</p>
<h2>Washing and reusing</h2>
<ul><li>Only wash <b>lightly soiled</b> rags: water, dust, mild cleaning products.</li>
<li>Wash them separately, in hot water.</li>
<li><b>No fabric softener</b>: it reduces cotton's absorbency.</li>
<li>Never put a rag that held oil or solvent in a dryer.</li></ul>
<h2>When and where to dispose of them</h2>
<p>A torn rag, or one soaked with a hazardous product, should be thrown out. Rags contaminated with paint, solvents or oils are hazardous waste: households take them to an ecocentre, and businesses use a specialized waste pickup company. Check your municipality's rules.</p>""",
  "faq": [("Why avoid fabric softener?", "It coats the fibers and stops cotton from absorbing, so your rags wipe less well."),
          ("Can a cleaning rag go in the trash?", "Yes, if it was only used with water or mild cleaning products. If it holds a hazardous product, follow your municipality's rules.")]}}

P["glossaire"] = {"kind": "guide", "img": TEXT, "rel": ["guide-ratine", "couleur", "faq"],
 "fr": {"path": "/guides/guenille-chiffon-torchon-lexique/", "short": "Guenille, chiffon, linge : le lexique",
  "title": "Guenille, chiffon, linge, ratine : le lexique québécois",
  "desc": "Guenille, chiffon d'essuyage, linge, torchon, ratine, jersey : le vocabulaire québécois et anglais des chiffons, pour bien chercher et bien commander.",
  "eyebrow": "Guide · lexique", "h1": "Guenille, chiffon, linge, ratine : le lexique des chiffons",
  "lede": "Au Québec, on dit guenille, chiffon ou linge. En anglais, rag, wiper ou shop rag. Voici ce que chaque mot veut dire.",
  "card": "Le vocabulaire québécois et anglais des chiffons, mot par mot.", "alt": "Textiles de coton récupérés",
  "body": "<p>Les mots changent d'une région et d'un métier à l'autre. Ce lexique vous aide à comparer les offres et à commander le bon produit.</p>",
  "terms": [("Guenille", "Mot québécois pour un chiffon fait d'un vieux tissu, utilisé pour nettoyer ou essuyer. « Des guenilles » se vendent souvent au poids, en sac."),
            ("Chiffon d'essuyage", "Terme général pour un morceau de tissu servant à essuyer : huile, graisse, liquides, poussière. En anglais : wiping rag ou wiper."),
            ("Chiffon d'atelier", "Chiffon utilisé dans les garages et ateliers. En anglais : shop rag."),
            ("Linge", "Au Québec, « un linge » désigne aussi un chiffon ou une serviette de nettoyage, comme dans « linge à vaisselle »."),
            ("Torchon", "Mot plus courant en France qu'au Québec pour un chiffon de nettoyage ou un linge à vaisselle."),
            ("Ratine", "Au Québec, le tissu éponge bouclé des serviettes. Épais et très absorbant. En anglais : terry."),
            ("Jersey (t-shirt)", "Tissu de coton tricoté des t-shirts. Mince, doux et peu pelucheux."),
            ("Peu pelucheux", "Qui laisse peu de fibres sur la surface. En anglais : low-lint."),
            ("Sans transfert de couleur", "Chiffon blanc qui ne laisse pas de teinture sur la surface essuyée."),
            ("Textile post-consommation", "Vêtements et tissus usagés récupérés après usage, puis triés et transformés en chiffons."),
            ("Vendu au poids", "Les chiffons se vendent en livres (lb) plutôt qu'à la pièce, car la taille des morceaux varie."),
            ("Traitement anti-punaises", "Traitement des textiles contre les punaises de lit avant l'emballage.")]},
 "en": {"path": "/en/guides/rag-glossary-quebec/", "short": "Rag glossary: guenille, chiffon, terry",
  "title": "Rag glossary: guenille, chiffon, terry, shop rag",
  "desc": "Guenille, chiffon, linge, ratine, wiper, shop rag: the Québec French and English vocabulary of rags, to search and order with confidence.",
  "eyebrow": "Guide · glossary", "h1": "Rag glossary: Québec French and English terms",
  "lede": "In Québec, people say guenille, chiffon or linge. In English, rag, wiper or shop rag. Here's what each word means.",
  "card": "The Québec French and English rag vocabulary, word by word.", "alt": "Reclaimed cotton textiles",
  "body": "<p>Words change from one region and trade to the next. This glossary helps you compare offers and order the right product.</p>",
  "terms": [("Guenille", "Québec French for a rag made from old fabric, used for cleaning or wiping. Guenilles are often sold by weight, in bags."),
            ("Chiffon d'essuyage (wiping rag)", "General term for a piece of fabric used to wipe oil, grease, liquids or dust. Also called a wiper."),
            ("Shop rag (chiffon d'atelier)", "A rag used in garages and workshops."),
            ("Linge", "In Québec, \"un linge\" also means a cleaning cloth or towel, as in \"linge à vaisselle\" (dish towel)."),
            ("Torchon", "Word used more in France than in Québec for a cleaning rag or dish towel."),
            ("Terry (ratine)", "Looped towel fabric. Thick and highly absorbent. Québec French calls it ratine."),
            ("Jersey (T-shirt)", "Knitted cotton fabric from T-shirts. Thin, soft and low-lint."),
            ("Low-lint (peu pelucheux)", "Leaves few fibers on the surface."),
            ("No color transfer (sans transfert de couleur)", "White rag that leaves no dye on the wiped surface."),
            ("Post-consumer textile", "Used clothing and fabric collected after use, then sorted and turned into rags."),
            ("Sold by weight", "Rags are sold by the pound (lb) rather than by the piece, because piece sizes vary."),
            ("Bedbug treatment (traitement anti-punaises)", "Treating textiles against bedbugs before packing.")]}}

P["calculateur"] = {"kind": "tool", "img": None, "rel": ["gros", "livraison", "guide-ratine"],
 "fr": {"path": "/calculateur-chiffons/", "short": "Calculateur de budget",
  "title": "Calculateur : combien de sacs de chiffons par mois?",
  "desc": "Estimez vos sacs de chiffons de 25 lb par mois et votre budget avant et après taxes (TPS et TVQ), selon votre consommation et le produit choisi.",
  "eyebrow": "Outil · budget", "h1": "Calculateur : combien de sacs de chiffons vous faut-il?",
  "lede": "Entrez votre consommation, choisissez un produit : vous obtenez le nombre de sacs par mois et le budget avant et après taxes.",
  "card": "Nombre de sacs par mois et budget avec TPS et TVQ.",
  "body": """<h2>Comment estimer votre consommation</h2>
<p>Le plus simple : commandez quelques [packs] et notez combien de temps ils durent. Divisez ensuite 25 lb par le nombre de semaines pour obtenir vos livres par semaine.</p>
<h2>Hors Laval et Montréal</h2>
<p>Le minimum est de 1 000 lb par livraison (40 sacs, produits mélangés acceptés). Le calculateur indique combien de mois de consommation cela représente. Voir les <a href="{{livraison}}">conditions de livraison</a>.</p>
<p>Ce calcul est une estimation. Les frais de livraison ne sont pas inclus : ils dépendent de votre adresse et sont indiqués dans la soumission.</p>""",
  "tool": {"lbw": "Consommation (lb par semaine)", "prod": "Produit", "zone": "Livraison", "z1": "Laval ou Montréal", "z2": "Ailleurs au Québec",
           "bags": "Sacs de 25 lb par mois", "pre": "Budget mensuel avant taxes", "tax": "TPS (5 %) + TVQ (9,975 %)", "tot": "Total mensuel avec taxes",
           "min": "Le minimum de 1 000 lb correspond à environ {m} mois de consommation.", "cur": "fr"}},
 "en": {"path": "/en/rag-calculator/", "short": "Budget calculator",
  "title": "Calculator: how many bags of rags per month?",
  "desc": "Estimate your 25 lb bags of rags per month and your budget before and after tax (GST and QST), based on your usage and the product you choose.",
  "eyebrow": "Tool · budget", "h1": "Calculator: how many bags of rags do you need?",
  "lede": "Enter your usage and choose a product: you get the number of bags per month and the budget before and after tax.",
  "card": "Bags per month and budget with GST and QST.",
  "body": """<h2>How to estimate your usage</h2>
<p>The simplest way: order a few [packs] and note how long they last. Then divide 25 lb by the number of weeks to get your pounds per week.</p>
<h2>Outside Laval and Montréal</h2>
<p>The minimum is 1,000 lb per delivery (40 bags, mixed products welcome). The calculator shows how many months of usage that represents. See the <a href="{{livraison}}">delivery terms</a>.</p>
<p>This is an estimate. Delivery fees aren't included: they depend on your address and are shown in the quote.</p>""",
  "tool": {"lbw": "Usage (lb per week)", "prod": "Product", "zone": "Delivery", "z1": "Laval or Montréal", "z2": "Elsewhere in Québec",
           "bags": "25 lb bags per month", "pre": "Monthly budget before tax", "tax": "GST (5%) + QST (9.975%)", "tot": "Monthly total with tax",
           "min": "The 1,000 lb minimum equals about {m} months of usage.", "cur": "en"}}}

GUIDE2_PAGES = P
