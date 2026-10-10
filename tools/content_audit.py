"""Audit follow-ups: sectors hub, longer EN sector pages, wholesale/calculator/guides text, city local details."""
HUB = {"kind": "hub", "img": None, "rel": [],
 "fr": {"path": "/secteurs/", "short": "Tous les secteurs", "title": "Chiffons d'essuyage par secteur : garages, ateliers, ménage",
  "desc": "Guenilles et chiffons recyclés pour 14 secteurs : garages, carrosserie, peinture, ménage, chantiers, restaurants, usinage, fermes, marinas, municipalités.",
  "eyebrow": "Secteurs", "h1": "Chiffons d'essuyage pour chaque secteur", "lede": "Le même chiffon ne sert pas partout. Trouvez les conseils et le produit adaptés à votre métier.",
  "card": "Les 14 secteurs que nous servons, avec le bon chiffon pour chacun.",
  "body": """<p>Nos quatre produits (t-shirt ou ratine, couleur ou blanc) couvrent la plupart des besoins d'essuyage. La couleur à 32 $ le [pack] convient à l'huile, à la graisse et au nettoyage courant. Le blanc à 42 $ évite le transfert de couleur pour la peinture, la teinture et la finition. Chaque page ci-dessous explique les usages et le produit conseillé pour un secteur.</p>"""},
 "en": {"path": "/en/industries/", "short": "All industries", "title": "Wiping rags by industry: garages, shops, cleaning",
  "desc": "Recycled rags for 14 industries: garages, auto body, painting, janitorial, job sites, restaurants, machine shops, farms, marinas, municipalities.",
  "eyebrow": "Industries", "h1": "Wiping rags for every industry", "lede": "The same rag doesn't fit every job. Find the advice and product for your trade.",
  "card": "The 14 industries we serve, with the right rag for each.",
  "body": """<p>Our four products (T-shirt or terry, colored or white) cover most wiping needs. Colored at $32 per [pack] handles oil, grease and everyday cleaning. White at $42 avoids color transfer for painting, staining and finishing. Each page below explains the uses and the recommended product for one industry.</p>"""}}

GUIDES_BODY = {
 "fr": """<p>Nos guides répondent aux questions qu'on nous pose le plus : quel chiffon choisir entre la ratine et le t-shirt, comment éviter qu'un chiffon huileux prenne feu, comment ranger, laver et jeter ses chiffons, et s'il vaut mieux utiliser des chiffons recyclés ou du papier. Le lexique explique les mots québécois (guenille, linge, ratine) et leurs équivalents anglais. Le calculateur estime votre nombre de sacs par mois et votre budget avec taxes.</p>
<h2>Par où commencer</h2>
<p>Vous équipez un garage ou un atelier? Commencez par le guide sur les chiffons huileux : c'est une question de sécurité incendie. Vous hésitez entre deux produits? Le comparatif ratine ou t-shirt vous aide à choisir. Vous préparez une commande? Le calculateur vous donne le nombre de sacs et le budget avant de demander une soumission.</p>""",
 "en": """<p>Our guides answer the questions we hear most: terry or T-shirt, how to keep oily rags from catching fire, how to store, wash and dispose of rags, and whether recycled rags beat paper. The glossary explains Québec French terms (guenille, linge, ratine) and their English equivalents. The calculator estimates your bags per month and your budget with tax.</p>
<h2>Where to start</h2>
<p>Setting up a garage or shop? Start with the oily rags guide: it's a fire-safety issue. Torn between two products? The terry vs T-shirt comparison helps you choose. Planning an order? The calculator gives you the number of bags and the budget before you request a quote.</p>"""}

GROS_EXTRA = {
 "fr": """<h2>Commandes en volume</h2>
<p>La quantité est illimitée. Une livraison hors Laval et Montréal commence à 1 000 lb, soit 40 [packs], et vous pouvez mélanger les quatre produits dans une même commande. Pour des commandes régulières ou de grands volumes, demandez une soumission : nous calculons le prix et la livraison selon votre adresse et votre fréquence.</p>
<h2>Pour distributeurs et revendeurs</h2>
<p>Distributeurs de produits sanitaires, quincailleries, fournisseurs de garages et d'ateliers : nos chiffons sont emballés en [packs] scellés, faciles à entreposer et à revendre. Indiquez dans votre demande les volumes prévus et les adresses de livraison.</p>
<h2>Comment se passe une commande</h2>
<ol><li>Vous demandez une soumission avec la quantité et l'adresse.</li><li>Nous confirmons le prix, les frais de livraison et la date.</li><li>La commande est confirmée et payée une semaine avant la livraison.</li><li>Nous livrons à votre adresse, avec une facture incluant TPS et TVQ.</li></ol>""",
 "en": """<h2>Volume orders</h2>
<p>Quantity is unlimited. A delivery outside Laval and Montréal starts at 1,000 lb, or 40 [packs], and you can mix all four products in one order. For recurring or large-volume orders, request a quote: we price the order and delivery based on your address and frequency.</p>
<h2>For distributors and resellers</h2>
<p>Janitorial distributors, hardware stores, garage and shop suppliers: our rags come in sealed [packs], easy to store and resell. Include your expected volumes and delivery addresses in your request.</p>
<h2>How an order works</h2>
<ol><li>You request a quote with the quantity and address.</li><li>We confirm the price, delivery fee and date.</li><li>The order is confirmed and paid one week before delivery.</li><li>We deliver to your address, with an invoice showing GST and QST.</li></ol>"""}

CALC_EXTRA = {
 "fr": """<h2>Exemples</h2>
<table><thead><tr><th>Consommation</th><th>Sacs par mois</th><th>Couleur (32 $)</th><th>Blanc (42 $)</th></tr></thead><tbody>
<tr><td>10 lb par semaine</td><td>2</td><td>64 $</td><td>84 $</td></tr>
<tr><td>25 lb par semaine</td><td>5</td><td>160 $</td><td>210 $</td></tr>
<tr><td>50 lb par semaine</td><td>9</td><td>288 $</td><td>378 $</td></tr>
<tr><td>100 lb par semaine</td><td>18</td><td>576 $</td><td>756 $</td></tr></tbody></table>
<p>Montants avant taxes, arrondis au sac supérieur (un mois = 52 semaines ÷ 12).</p>""",
 "en": """<h2>Examples</h2>
<table><thead><tr><th>Usage</th><th>Bags per month</th><th>Colored ($32)</th><th>White ($42)</th></tr></thead><tbody>
<tr><td>10 lb per week</td><td>2</td><td>$64</td><td>$84</td></tr>
<tr><td>25 lb per week</td><td>5</td><td>$160</td><td>$210</td></tr>
<tr><td>50 lb per week</td><td>9</td><td>$288</td><td>$378</td></tr>
<tr><td>100 lb per week</td><td>18</td><td>$576</td><td>$756</td></tr></tbody></table>
<p>Amounts before tax, rounded up to the next bag (one month = 52 weeks ÷ 12).</p>"""}

EN_SECTOR_EXTRA = {
 "carrosserie": "<h2>How much does a body shop use?</h2><p>Usage depends on the number of bays and how much prep work you do. Start with a few [packs] of each type, note how long they last, then use our <a href=\"{{calculateur}}\">calculator</a> to plan a monthly order.</p>",
 "esthetique-auto": "<h2>Keeping costs down</h2><p>A detailer who uses recycled rags for wheels, engines and jambs replaces fewer microfibers. Keep one bin of colored rags for the dirty jobs and a separate bin of microfibers for paint, so they never mix.</p><p>Car washes with several bays can order in volume: see <a href=\"{{gros}}\">wholesale</a>.</p>",
 "ebenisterie": "<h2>Wiping off excess finish</h2><p>After applying oil or stain, wipe the excess with a clean white rag, following the product's directions. Change rags often: a saturated rag spreads finish instead of removing it. Then lay used rags flat to dry outdoors or store them in water in a closed metal container.</p>",
 "plomberie-cvac": "<h2>On the customer's premises</h2><p>A clean rag under a fitting or a valve protects floors and finishes during repairs. Keep a bag in each truck, and a closed metal container for rags soaked with oil or solvent.</p><p>To estimate how many bags your team needs, use our <a href=\"{{calculateur}}\">calculator</a>.</p>",
 "marine": "<h2>Storing rags on site</h2><p>Keep clean rags in their sealed bag, away from moisture, so they stay ready for the season. Dirty rags go in a closed metal container away from fuel tanks and boats, then to a proper collection point.</p><p>Marinas can also check <a href=\"{{gros}}\">volume orders</a> before launch season.</p>",
 "agriculture": "<h2>Before planting and harvest</h2><p>Order before the busy seasons: orders are confirmed and paid one week before delivery. Store bags in a dry building, away from fuel and chemicals. Rags soaked with oil or fuel go in a closed metal container, never in a pile in the barn.</p>",
 "usinage": "<h2>One bin per station</h2><p>A bin of rags at each machine avoids waste and keeps oil off the floor. Used rags go in a closed metal container emptied daily, especially with cutting oils.</p><p>For several shifts or sites, see <a href=\"{{gros}}\">wholesale</a>.</p>",
 "municipal": "<h2>Planning a yearly supply</h2><p>Municipal garages use more rags during snow-removal season. Use our <a href=\"{{calculateur}}\">calculator</a> to estimate monthly needs, then request a quote for regular deliveries.</p>",
 "construction": "<h2>On the job site</h2><p>Keep a bag in each trailer or truck. Use colored rags for tools, equipment and cleanup, and white rags for painting and finishing trades. Rags soaked with solvent or stain go in a closed metal container.</p><p>Contractors with several sites can order in volume: see <a href=\"{{gros}}\">wholesale</a>.</p>"}

CITY_LOCAL = {
 "ville-laval": ("A-15, A-13, A-19, A-25 et A-440", "A-15, A-13, A-19, A-25 and A-440", "la Ville de Laval"),
 "ville-montreal": ("A-15, A-13, A-40, A-20 et A-25", "A-15, A-13, A-40, A-20 and A-25", "la Ville de Montréal"),
 "ville-longueuil": ("A-20, A-30 et route 132", "A-20, A-30 and Route 132", "la Ville de Longueuil"),
 "ville-terrebonne": ("A-25 et A-640", "A-25 and A-640", "la Ville de Terrebonne ou de Mascouche"),
 "ville-blainville": ("A-15, A-640 et route 117", "A-15, A-640 and Route 117", "votre municipalité (Blainville, Boisbriand, Sainte-Thérèse…)"),
 "ville-rive-nord": ("A-15, A-13, A-640 et A-40", "A-15, A-13, A-640 and A-40", "votre municipalité ou votre MRC"),
 "ville-rive-sud": ("A-10, A-20, A-30 et route 132", "A-10, A-20, A-30 and Route 132", "votre municipalité"),
 "ville-quebec": ("A-20, A-40 et A-73", "A-20, A-40 and A-73", "la Ville de Québec ou de Lévis"),
 "ville-sherbrooke": ("A-10, A-55 et A-410", "A-10, A-55 and A-410", "la Ville de Sherbrooke"),
 "ville-trois-rivieres": ("A-40 et A-55", "A-40 and A-55", "la Ville de Trois-Rivières"),
 "ville-gatineau": ("A-50 et A-5", "A-50 and A-5", "la Ville de Gatineau")}

def city_extra(key, page):
    fr_r, en_r, muni = CITY_LOCAL[key]
    muni_en = muni.replace("la Ville de ", "the City of ").replace(" ou de ", " or ").replace("votre municipalité ou votre MRC", "your municipality or MRC").replace("votre municipalité", "your municipality")
    core = page["core"]
    fr = f"""<h2>Zones industrielles et commerciales</h2>
<p>Nous livrons les garages, ateliers et entreprises des parcs industriels et commerciaux le long de l'{fr_r}. Indiquez l'adresse exacte et les heures de réception dans votre demande.</p>
<h2>Jeter les chiffons souillés</h2>
<p>Les chiffons imbibés d'huile, de solvant ou de peinture sont des résidus dangereux. Les particuliers les apportent aux écocentres ou aux collectes de résidus domestiques dangereux de {muni}; les entreprises font appel à une entreprise de collecte spécialisée. Vérifiez les règles locales. Voir aussi le guide <a href="{{{{guide-ranger}}}}">ranger, laver et jeter ses chiffons</a>.</p>""" + ("" if core else """
<h2>Atteindre le minimum de 1 000 lb</h2>
<p>Peu d'entreprises utilisent 40 sacs d'un coup. Vous pouvez mélanger les quatre produits, commander pour plusieurs mois, ou regrouper une commande avec une entreprise voisine livrée à la même adresse. Notre <a href="{{calculateur}}">calculateur</a> indique combien de mois de consommation représentent 1 000 lb.</p>""")
    en = f"""<h2>Industrial and commercial areas</h2>
<p>We deliver to garages, shops and businesses in the industrial and commercial parks along the {en_r}. Include the exact address and receiving hours in your request.</p>
<h2>Disposing of dirty rags</h2>
<p>Rags soaked with oil, solvent or paint are hazardous waste. Households take them to the ecocentres or household hazardous waste collections run by {muni_en}; businesses use a specialized waste pickup company. Check local rules. See also the guide <a href="{{{{guide-ranger}}}}">storing, washing and disposing of rags</a>.</p>""" + ("" if core else """
<h2>Reaching the 1,000 lb minimum</h2>
<p>Few businesses use 40 bags at once. You can mix all four products, order for several months, or combine an order with a neighbouring business delivered to the same address. Our <a href="{{calculateur}}">calculator</a> shows how many months of usage 1,000 lb represents.</p>""")
    return fr.replace("{{{{", "{{").replace("}}}}", "}}"), en.replace("{{{{", "{{").replace("}}}}", "}}")
