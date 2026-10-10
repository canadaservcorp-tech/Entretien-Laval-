#!/usr/bin/env python3
"""Generates every page of entretienlaval.ca from tools/content.py. Run: python3 tools/build.py"""
import datetime, glob, hashlib, html, json, os, re, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "src")
TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year
rd = lambda p: open(os.path.join(SRC, p), encoding="utf-8").read()
ICON = json.load(open(os.path.join(SRC, "icons.json"), encoding="utf-8"))
SPRITE = rd("sprite.html")
LANGS = ("fr", "en")
BIZ_ID = C.SITE + "/#business"
CUR = ' aria-current="page"'
HID = '<svg aria-hidden="true"'

ROUTES = {"home": {l: C.HOME[l]["path"] for l in LANGS}}
ROUTES.update({k: {l: p[l]["path"] for l in LANGS} for k, p in C.PAGES.items()})
PROD = {p["id"]: p for p in C.PRODUCTS}

def L(key, lang):
    key, _, anchor = key.partition("#")
    return ROUTES[key][lang] + ("#" + anchor if anchor else "")

def fill(s, lang):
    s = re.sub(r"\{\{([\w-]+(?:#[\w-]+)?)\}\}", lambda m: L(m.group(1), lang), s)
    one, many = C.PACK[lang]
    return s.replace("[packs]", many).replace("[pack]", one)

def text(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()
def esc(s): return html.escape(s, quote=True)

def img_tag(name, alt, cls="", lazy=True, hi=False):
    w, h = Image.open(os.path.join(ROOT, "img", name)).size
    extra = (' loading="lazy"' if lazy else "") + (' fetchpriority="high"' if hi else "")
    return f'<img src="/img/{name}" alt="{esc(alt)}" width="{w}" height="{h}" decoding="async"{extra}{cls}>'

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"

# ---------- CSS ----------
def build_css():
    css = rd("fonts.css") + rd("base.css") + rd("extra.css")
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*\n\s*", "\n", css).strip() + "\n"
    h = hashlib.sha1(css.encode()).hexdigest()[:10]
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    for old in glob.glob(os.path.join(ROOT, "assets", "site.*.css")): os.remove(old)
    open(os.path.join(ROOT, "assets", f"site.{h}.css"), "w", encoding="utf-8").write(css)
    return f"/assets/site.{h}.css"

# ---------- shared blocks ----------
def head(lang, title, desc, key, ldobj, image="/img/og-chiffons-eco.jpg", noindex=False, ogtype="website"):
    path = L(key, lang); url = C.SITE + path
    alts = "" if noindex else "".join(f'<link rel="alternate" hreflang="{l}-CA" href="{C.SITE}{L(key, l)}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{C.SITE}{L(key, "fr")}">'
    other = "en" if lang == "fr" else "fr"
    return f"""<!DOCTYPE html>
<html lang="{lang}-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{url}">{alts}
<meta name="theme-color" content="#4A5D3A">
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="Chiffons ÉCO — Entretien Laval">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}"><meta property="og:locale" content="{lang}_CA"><meta property="og:locale:alternate" content="{other}_CA">
<meta property="og:image" content="{C.SITE}{image}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/Archivo-600-900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/IBMPlexSans-400-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{CSS}">
{ld(ldobj) if ldobj else ''}
</head>"""

def header(lang, key):
    u = C.UI[lang]; other = "en" if lang == "fr" else "fr"
    links = "".join(f'<a href="{L(k, lang)}"{CUR if k == key else ""}>{t}</a>' for t, k in C.NAV[lang])
    devis = f'<a class="ndevis" href="{L("home#devis", lang)}">{u["quote"]}</a>'
    return f"""<body>
{SPRITE}
<a class="skip" href="#main">{u['skip']}</a>
<header>
<div class="wrap bar">
<a class="brand" href="{L('home', lang)}"><svg aria-hidden="true"><use href="#mark"></use></svg><span>Chiffons ÉCO<small>ECO RAGS · ENTRETIEN LAVAL</small></span></a>
<nav class="main" aria-label="{u['nav_label']}">{links}{devis}</nav>
<div class="tools">
<a class="langsw" href="{L(key, other)}" hreflang="{other}-CA" lang="{other}-CA" aria-label="{u['lang_name']}">{other.upper()}</a>
<a class="call" href="{C.TEL}" aria-label="{u['call']}">{ICON['phone'].replace('<svg', HID, 1)}<span>{C.PHONE}</span></a>
<details class="mnav"><summary aria-label="{u['menu']}"><span></span></summary><nav aria-label="{u['menu']}">{links}<a class="btn btn-primary" href="{L('home#devis', lang)}">{u['quote']}</a></nav></details>
</div>
</div>
</header>
<main id="main">"""

def footer(lang):
    u = C.UI[lang]
    col = lambda title, keys: f'<div><h2>{title}</h2>' + "".join(f'<a href="{L(k, lang)}">{C.PAGES[k][lang]["short"]}</a>' for k in keys) + "</div>"
    return f"""</main>
<footer>
<div class="wrap">
<div class="fcols">
<div><div class="fbrand"><svg aria-hidden="true"><use href="#mark"></use></svg> Chiffons ÉCO — Entretien Laval</div>
<p class="legal" style="margin-top:14px">{u['foot_tag']}</p>
<p class="legal" style="margin-top:10px"><a href="{C.TEL}">{C.PHONE}</a><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br><a href="https://www.instagram.com/entretienlaval/" rel="noopener">Instagram @entretienlaval</a></p></div>
{col(u['products'], ['couleur', 'blancs', 'gros', 'livraison'])}
{col(u['sectors'], ['garage', 'peinture', 'entretien', 'construction', 'restauration', 'industrie'])}
{col(u['guides'], ['guide-huileux', 'guide-papier', 'guides', 'faq'])}
</div>
<div class="ftop"><div class="legal">Entretien Laval · NEQ 2280629637 · TPS 783132566 RT0001 · TVQ 4054025241 TQ0001<br>309-1355 Boul. Le Corbusier, Laval, QC H7N 0G4</div></div>
<div class="fbot"><span>© {YEAR} Entretien Laval — Chiffons ÉCO / ECO Rags</span><span><a href="{L('home', 'fr')}" lang="fr-CA">Français</a> · <a href="{L('home', 'en')}" lang="en-CA">English</a></span></div>
</div>
</footer>
<script>document.querySelectorAll('.mnav a').forEach(function(a){{a.addEventListener('click',function(){{a.closest('details').removeAttribute('open')}})}});</script>
</body>
</html>
"""

def faq_html(items, lang):
    return '<div class="faq">' + "".join(f'<details><summary>{fill(q, lang)}</summary><div class="a"><p>{fill(a, lang)}</p></div></details>' for q, a in items) + "</div>"

def faq_ld(items, lang):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": text(fill(q, lang)), "acceptedAnswer": {"@type": "Answer", "text": text(fill(a, lang))}} for q, a in items]}

def price_box(lang, ids=None):
    u = C.UI[lang]
    rows = "".join(f'<div class="pline"><span>{PROD[i][lang][0]}</span><b>{price(PROD[i]["price"], lang)}</b></div>' for i in (ids or [p["id"] for p in C.PRODUCTS]))
    return f'<div class="pbox"><h2>{fill(u["prices_h"], lang)}</h2>{rows}<p class="small">{u["prices_note"]}</p><a class="btn btn-primary" href="{L("home#devis", lang)}">{u["quote"]}</a><a class="btn btn-ghost" href="{C.TEL}">{u["call_btn"]} {C.PHONE}</a></div>'

def price(n, lang): return f"{n},00 $" if lang == "fr" else f"${n}.00"

def cards(keys, lang, more=None):
    u = C.UI[lang]
    return '<div class="cards">' + "".join(f'<a class="card" href="{L(k, lang)}"><h3>{C.PAGES[k][lang]["short"]}</h3><p>{fill(C.PAGES[k][lang]["card"], lang)}</p><span class="more">{more or u["more"]}</span></a>' for k in keys) + "</div>"

def ctaband(lang):
    u = C.UI[lang]
    return f'<section class="ctaband"><div class="wrap"><div><h2>{u["cta_h"]}</h2><p>{u["cta_p"]}</p></div><div class="cta-row" style="margin-top:0"><a class="btn btn-primary" href="{L("home#devis", lang)}">{u["quote"]}</a><a class="btn btn-ghost" href="{C.TEL}">{u["call_btn"]} {C.PHONE}</a></div></div></section>'

def product_ld(pid, lang):
    p = PROD[pid]; name, _, d = p[lang]
    return {"@type": "Product", "name": f"{name} – {C.PACK[lang][0]}", "description": d, "brand": {"@type": "Brand", "name": "Chiffons ÉCO"},
            "image": C.SITE + "/img/" + C.IMG_BAG, "material": "coton recyclé" if lang == "fr" else "recycled cotton",
            "offers": {"@type": "Offer", "price": f"{p['price']}.00", "priceCurrency": "CAD", "availability": "https://schema.org/InStock",
                       "url": C.SITE + L(p["page"], lang), "seller": {"@id": BIZ_ID}}}

def business(lang):
    b = json.load(open(os.path.join(SRC, f"ld-{lang}.json"), encoding="utf-8"))["@graph"][0]
    b["image"] = [C.SITE + "/img/og-chiffons-eco.jpg", C.SITE + "/img/" + C.IMG_BAG]
    b["priceRange"] = "32 $ – 42 $" if lang == "fr" else "$32 – $42"
    b["areaServed"] = [{"@type": "City", "name": c} for c in ["Laval", "Montréal", "Longueuil", "Terrebonne", "Blainville", "Boisbriand"]] + [{"@type": "AdministrativeArea", "name": "Québec"}]
    b["makesOffer"] = [{"@type": "Offer", "price": f"{p['price']}.00", "priceCurrency": "CAD", "itemOffered": {"@type": "Product", "name": f"{p[lang][0]} – {C.PACK[lang][0]}"}} for p in C.PRODUCTS]
    return b

def crumbs(lang, items):
    u = C.UI[lang]
    trail = [(u["home"], L("home", lang))] + items
    h = f'<nav class="crumbs wrap" aria-label="{u["crumbs"]}">' + " › ".join(f'<a href="{href}">{esc(t)}</a>' if i < len(trail) - 1 else f'<span aria-current="page">{esc(t)}</span>' for i, (t, href) in enumerate(trail)) + "</nav>"
    j = {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t, "item": C.SITE + href.split("#")[0]} for i, (t, href) in enumerate(trail)]}
    return h, j

def write(path, s):
    out = os.path.join(ROOT, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    s = re.sub(r"\n{2,}", "\n", s)
    open(out, "w", encoding="utf-8").write(s)

# ---------- subpages ----------
def subpage(key, lang):
    pg = C.PAGES[key]; t = pg[lang]; u = C.UI[lang]; kind = pg["kind"]
    parent = {"sector": [(u["sectors"], L("home#secteurs", lang))], "product": [(u["products"], L("home#produits", lang))],
              "guide": [(C.PAGES["guides"][lang]["short"], L("guides", lang))]}.get(kind, [])
    ch, cj = crumbs(lang, parent + [(t["short"], L(key, lang))])
    faq = t.get("faq") or (C.FAQ[lang] if kind == "faq" else [])
    graph = [{"@type": "Article" if kind == "guide" else "WebPage", "@id": C.SITE + L(key, lang) + "#page", "url": C.SITE + L(key, lang),
              "name": t["title"], "headline": t["h1"], "description": t["desc"], "inLanguage": f"{lang}-CA",
              "isPartOf": {"@id": C.SITE + "/#website"}, "about": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "dateModified": TODAY}, cj,
             {"@type": "LocalBusiness", "@id": BIZ_ID, "name": "Entretien Laval — Chiffons ÉCO", "url": C.SITE + "/", "telephone": "+1-438-831-3611"}]
    if kind == "guide": graph[0].update({"author": {"@id": BIZ_ID}, "image": C.SITE + "/img/" + pg["img"]})
    if faq and kind != "thanks": graph.append(faq_ld(faq, lang))
    for pid in pg.get("products", []): graph.append(product_ld(pid, lang))
    noindex = kind == "thanks"
    media = f'<div class="frame">{img_tag(pg["img"], t["alt"], lazy=False, hi=True)}</div>' if pg.get("img") else ""
    hero_cta = "" if noindex else f'<div class="cta-row"><a class="btn btn-primary" href="{L("home#devis", lang)}">{u["quote"]}</a><a class="btn btn-ghost" href="{C.TEL}">{u["call_btn"]} {C.PHONE}</a></div>'
    if noindex: hero_cta = f'<div class="cta-row"><a class="btn btn-primary" href="{L("home", lang)}">{u["home"]}</a></div>'
    hero = f'<section class="phero"><div class="wrap {"phero-grid" if media else ""}"><div><div class="eyebrow">{t["eyebrow"]}</div><h1>{t["h1"]}</h1><p class="lede">{fill(t["lede"], lang)}</p>{hero_cta}</div>{media}</div></section>'
    body = ""
    if kind in ("sector", "product", "info", "guide"):
        ids = pg.get("products")
        side = price_box(lang, ids)
        if kind == "product":
            prods = "".join(f'<div class="prod"><span class="code">{PROD[i][lang][1]}</span><h3>{PROD[i][lang][0]}</h3><div class="price">{price(PROD[i]["price"], lang)}<small>{fill(u["unit"], lang)}</small></div><p>{PROD[i][lang][2]}</p></div>' for i in ids)
            body += f'<section class="section band"><div class="wrap"><div class="prods" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">{prods}</div><div class="terms">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in C.TERMS[lang]) + "</div></div></section>"
        if kind == "info":
            body += f'<section class="section band"><div class="wrap"><div class="terms" style="margin-top:0">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in C.TERMS[lang]) + "</div></div></section>"
        body += f'<section class="section"><div class="wrap cgrid"><article class="prose">{fill(t["body"], lang)}</article><aside class="side">{side}</aside></div></section>'
        if faq: body += f'<section class="section band"><div class="wrap"><div class="sec-head"><h2>{u["faq_h"]}</h2></div>{faq_html(faq, lang)}</div></section>'
    elif kind == "faq":
        body += f'<section class="section"><div class="wrap cgrid"><div>{faq_html(faq, lang)}</div><aside class="side">{price_box(lang)}</aside></div></section>'
    elif kind == "guides":
        body += f'<section class="section"><div class="wrap">{cards(["guide-huileux", "guide-papier"], lang, u["read"])}</div></section>'
    if pg["rel"]:
        body += f'<section class="section"><div class="wrap"><div class="sec-head"><h2>{u["related"]}</h2></div>{cards(pg["rel"], lang)}</div></section>'
    if not noindex: body += ctaband(lang)
    img = "/img/" + pg["img"] if pg.get("img") else "/img/og-chiffons-eco.jpg"
    doc = head(lang, t["title"], t["desc"], key, {"@context": "https://schema.org", "@graph": graph}, image=img, noindex=noindex,
               ogtype="article" if kind == "guide" else "website") + header(lang, key) + ch + hero + body + footer(lang)
    write(L(key, lang), doc)

# ---------- homepage ----------
def homepage(lang):
    h = C.HOME[lang]; u = C.UI[lang]
    part = rd(f"home-{lang}.html")
    part = re.sub(r' data-i="[^"]*"', "", part)
    part = re.sub(r"<!-- GRADES -->.*?</section>\n", "<!--PRODUCTS-->", part, flags=re.S)
    part = re.sub(r'(<a class="btn btn-primary") href="#contact">[^<]*</a>', rf'\1 href="#devis">{h["hero_cta1"]}</a>', part, count=1)
    part = re.sub(r'(<a class="btn btn-ghost") href="#grades">[^<]*</a>', rf'\1 href="#produits">{h["hero_cta2"]}</a>', part, count=1)
    part = part.replace('href="#contact"', 'href="#devis"').replace('href="#grades"', 'href="#produits"')
    part = re.sub(r'(<div class="hero-media">\s*<div class="frame"><img)', r'\1 fetchpriority="high"', part, count=1)
    part = part.replace("Boîte 25 lb", "Sac de 25 lb").replace("Boîte de 25 lb", "Sac de 25 lb").replace("25 lb box", "25 lb bag").replace("box", "bag")
    part = part.replace("en boîte de 25 lb", "en sac de 25 lb").replace("boîte de 25 lb", "sac de 25 lb").replace("caisse", "sac")
    prods = "".join(f'<div class="prod"><span class="code">{p[lang][1]}</span><h3>{p[lang][0]}</h3><div class="price">{price(p["price"], lang)}<small>{fill(u["unit"], lang)}</small></div><p>{p[lang][2]}</p><a href="{L(p["page"], lang)}">{u["more"]}</a></div>' for p in C.PRODUCTS)
    terms = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in C.TERMS[lang])
    photos = f'<div class="prodphoto"><div class="frame">{img_tag(C.IMG_BAG, h["photo_alt"][1])}</div><div class="frame">{img_tag(C.IMG_BAGS, h["photo_alt"][0])}</div></div>'
    products = f'<section class="section" id="produits"><span id="grades"></span><div class="wrap"><div class="sec-head"><div class="eyebrow">{h["prod_eyebrow"]}</div><h2>{h["prod_h2"]}</h2><p>{fill(h["prod_p"], lang)}</p></div><div class="prods">{prods}</div><div class="terms">{terms}</div>{photos}</div></section>'
    part = part.replace("<!--PRODUCTS-->", products)
    sectors = f'<section class="section" id="secteurs"><span id="uses"></span><div class="wrap"><div class="sec-head"><div class="eyebrow">{h["sec_eyebrow"]}</div><h2>{h["sec_h2"]}</h2><p>{h["sec_p"]}</p></div>{cards(C.SECTOR_KEYS, lang)}</div></section>'
    cities = "".join(f"<span>{c}</span>" for c in C.CITIES) + f'<span>{"Partout au Québec (1 000 lb +)" if lang == "fr" else "Anywhere in Québec (1,000 lb +)"}</span>'
    delivery = f'<section class="section band" id="livraison"><div class="wrap"><div class="sec-head" style="margin-bottom:10px"><div class="eyebrow">{h["del_eyebrow"]}</div><h2>{h["del_h2"]}</h2><p>{h["del_p"]}</p></div><div class="cities">{cities}</div><p style="margin-top:22px"><a class="btn btn-ghost" href="{L("livraison", lang)}">{h["del_link"]}</a></p></div></section>'
    faq = f'<section class="section" id="faq"><div class="wrap"><div class="sec-head"><div class="eyebrow">{h["faq_eyebrow"]}</div><h2>{h["faq_h2"]}</h2></div>{faq_html(C.FAQ[lang][:6], lang)}<p style="margin-top:22px"><a class="btn btn-ghost" href="{L("faq", lang)}">{u["see_all_faq"]}</a></p></div></section>'
    opts = "".join(f"<option>{p[lang][0]}</option>" for p in C.PRODUCTS) + f'<option>{h["f_any"]}</option>'
    form = f"""<form class="qform" name="soumission" method="POST" action="{L('merci', lang)}" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="soumission"><input type="hidden" name="langue" value="{lang}">
<p class="hp"><label>Ne pas remplir <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<h3>{h['form_h']}</h3><p class="sub">{h['form_sub']}</p>
<div class="fgrid">
<div><label for="f-name-{lang}">{h['f_name']} *</label><input id="f-name-{lang}" name="nom" required autocomplete="name"></div>
<div><label for="f-co-{lang}">{h['f_company']}</label><input id="f-co-{lang}" name="entreprise" autocomplete="organization"></div>
<div><label for="f-email-{lang}">{h['f_email']} *</label><input id="f-email-{lang}" name="courriel" type="email" required autocomplete="email"></div>
<div><label for="f-tel-{lang}">{h['f_phone']}</label><input id="f-tel-{lang}" name="telephone" type="tel" autocomplete="tel"></div>
<div><label for="f-city-{lang}">{h['f_city']} *</label><input id="f-city-{lang}" name="ville" required autocomplete="address-level2"></div>
<div><label for="f-qty-{lang}">{h['f_qty']}</label><input id="f-qty-{lang}" name="quantite" type="number" min="1" inputmode="numeric"></div>
<div class="full"><label for="f-prod-{lang}">{h['f_product']}</label><select id="f-prod-{lang}" name="produit">{opts}</select></div>
<div class="full"><label for="f-msg-{lang}">{h['f_msg']}</label><textarea id="f-msg-{lang}" name="message"></textarea></div>
</div>
<button class="btn btn-primary" type="submit">{h['f_send']}</button>
<p class="fine">{h['f_fine']}</p>
</form>"""
    lbl = h["lbl"]
    line = lambda ic, label, val: f'<div class="cline">{ICON[ic].replace("<svg", HID, 1)}<div><div class="lbl">{label}</div>{val}</div></div>'
    info = (line("phone", lbl["phone"], f'<a class="val" href="{C.TEL}">{C.PHONE}</a>') + line("mail", lbl["mail"], f'<a class="val" href="mailto:{C.EMAIL}">{C.EMAIL}</a>')
            + line("wa", lbl["wa"], f'<a class="val" href="{C.WA[lang]}" rel="noopener" target="_blank">{C.PHONE}</a>')
            + line("ig", lbl["ig"], '<a class="val" href="https://www.instagram.com/entretienlaval/" rel="noopener" target="_blank">@entretienlaval</a>')
            + line("pin", lbl["pin"], '<span class="val">309-1355 Boul. Le Corbusier<br>Laval, QC H7N 0G4</span>')
            + line("biz", lbl["biz"], '<span class="val">Entretien Laval</span><div class="mono" style="font-size:12px;color:#5f5d53;margin-top:4px">NEQ 2280629637</div>'))
    devis = f"""<section class="section band" id="devis"><span id="contact"></span><div class="wrap"><div class="sec-head"><div class="eyebrow">{h['devis_eyebrow']}</div><h2>{h['devis_h2']}</h2></div>
<div class="contact-grid">{form}<div><div class="cbox"><h3>{h['ready_h']}</h3><p>{h['ready_p']}</p><div class="actions">
<a class="cta" href="mailto:{C.EMAIL}"><span>{h['c_email_btn']}</span>{ICON['arrow']}</a>
<a class="cta" href="{C.WA[lang]}" rel="noopener" target="_blank"><span>{h['c_wa_btn']}</span>{ICON['wa']}</a>
<a class="cta" href="{C.TEL}"><span>{h['c_call_btn']}</span>{ICON['arrow']}</a></div></div>
<div class="cinfo" style="margin-top:18px">{info}</div></div></div></div></section>"""
    biz = business(lang)
    graph = [biz, {"@type": "WebSite", "@id": C.SITE + "/#website", "url": C.SITE + "/", "name": "Chiffons ÉCO — Entretien Laval", "inLanguage": ["fr-CA", "en-CA"], "publisher": {"@id": BIZ_ID}},
             {"@type": "WebPage", "@id": C.SITE + h["path"] + "#page", "url": C.SITE + h["path"], "name": h["title"], "description": h["desc"], "inLanguage": f"{lang}-CA", "isPartOf": {"@id": C.SITE + "/#website"}, "about": {"@id": BIZ_ID}, "dateModified": TODAY}]
    graph += [product_ld(p["id"], lang) for p in C.PRODUCTS]
    doc = head(lang, h["title"], h["desc"], "home", {"@context": "https://schema.org", "@graph": graph}) + header(lang, "home") + part + sectors + delivery + faq + devis + footer(lang)
    write(h["path"], doc)

# ---------- 404, sitemap, llms, robots, indexnow ----------
def notfound():
    u = C.UI["fr"]
    body = f"""<section class="phero"><div class="wrap"><div class="eyebrow">404</div><h1>Page introuvable</h1><p class="lede">Cette page n'existe pas ou a été déplacée. <span lang="en-CA">This page doesn't exist or has moved.</span></p>
<div class="cta-row"><a class="btn btn-primary" href="/">Accueil</a><a class="btn btn-ghost" href="/en/" lang="en-CA">English home</a><a class="btn btn-ghost" href="/#devis">{u['quote']}</a></div></div></section>
<section class="section"><div class="wrap">{cards(['couleur', 'blancs', 'gros', 'livraison'], 'fr')}</div></section>"""
    doc = head("fr", "Page introuvable | Chiffons ÉCO", "Page introuvable.", "home", None, noindex=True) + header("fr", "home") + body + footer("fr")
    doc = doc.replace(f'<link rel="canonical" href="{C.SITE}/">', "")
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(re.sub(r"\n{2,}", "\n", doc))

def indexable():
    return ["home"] + [k for k, p in C.PAGES.items() if p["kind"] != "thanks"]

def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for k in indexable():
        for l in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}-CA" href="{C.SITE}{L(k, x)}"/>' for x in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{C.SITE}{L(k, "fr")}"/>'
            out.append(f"<url><loc>{C.SITE}{L(k, l)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>")
    out.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(out) + "\n")

def llms():
    lines = ["# Chiffons ÉCO — Entretien Laval", "",
             "> Entretien Laval (Chiffons ÉCO / ECO Rags) sells recycled cotton wiping rags (shop rags, guenilles) in 25 lb bags, washed, sorted and treated against bedbugs, packed in Laval, Québec. Delivery across Greater Montreal and, from 1,000 lb, anywhere in Québec.", "",
             "Products and prices (per 25 lb bag, before tax): colored T-shirt rags $32, colored terry rags $32, white terry rags $42, white T-shirt rags $42. Delivery fee depends on location. Orders confirmed and paid one week before delivery.", "",
             f"Contact: {C.PHONE} · {C.EMAIL} · 309-1355 Boul. Le Corbusier, Laval, QC H7N 0G4 · NEQ 2280629637", "", "## Français"]
    lines += [f"- [{C.PAGES[k]['fr']['short'] if k != 'home' else 'Accueil'}]({C.SITE}{L(k, 'fr')})" for k in indexable()]
    lines += ["", "## English"] + [f"- [{C.PAGES[k]['en']['short'] if k != 'home' else 'Home'}]({C.SITE}{L(k, 'en')})" for k in indexable()]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(lines) + "\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /merci/\nDisallow: /en/thanks/\n\nSitemap: {C.SITE}/sitemap.xml\n")
    open(os.path.join(ROOT, f"{C.INDEXNOW_KEY}.txt"), "w").write(C.INDEXNOW_KEY)

CSS = build_css()
for l in LANGS:
    homepage(l)
    for k in C.PAGES: subpage(k, l)
notfound(); sitemap(); llms()
print("built", 2 * (1 + len(C.PAGES)), "pages + 404;", CSS)
