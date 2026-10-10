#!/usr/bin/env python3
"""Generates every page of entretienlaval.ca from tools/content.py. Run: python3 tools/build.py"""
import datetime, glob, hashlib, html, json, os, re, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
import content as C
import content_order as O

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

# ---------- stable page dates (SEO) ----------
# Each page keeps its own published/modified date; "modified" only changes when the page content changes,
# so sitemap <lastmod> and schema dateModified stay trustworthy for Google.
DATES_FILE = os.path.join(ROOT, "tools", "pagedates.json")
DATES = json.load(open(DATES_FILE, encoding="utf-8")) if os.path.exists(DATES_FILE) else {}
D_MOD, D_PUB = "__DATE_MODIFIED__", "__DATE_PUBLISHED__"
GSC = getattr(C, "GOOGLE_SITE_VERIFICATION", "")

def git_date(relpath, first=False):
    import subprocess
    args = ["git", "-C", ROOT, "log", "--format=%as"] + (["--diff-filter=A"] if first else ["-1"]) + ["--", relpath]
    try:
        out = subprocess.run(args, capture_output=True, text=True, timeout=20).stdout.split()
        return (out[-1] if first else out[0]) if out else TODAY
    except Exception:
        return TODAY

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
def head(lang, title, desc, key, ldobj, image="/img/og-chiffons-eco.jpg", noindex=False, ogtype="website", image_alt=""):
    if not noindex and (len(title) > 65 or len(desc) > 160):
        print(f"SEO length warning [{lang}] {key}: title {len(title)} / desc {len(desc)}")
    iw, ih = Image.open(os.path.join(ROOT, image.lstrip("/"))).size
    alt = image_alt or title
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
<meta property="og:image" content="{C.SITE}{image}"><meta property="og:image:width" content="{iw}"><meta property="og:image:height" content="{ih}"><meta property="og:image:alt" content="{esc(alt)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image:alt" content="{esc(alt)}">
{f'<meta name="google-site-verification" content="{GSC}">' if GSC else ''}
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
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
<a class="langsw" href="{L(key, other)}" hreflang="{other}-CA" lang="{other}-CA" title="{u['lang_name']}">{other.upper()}</a>
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
{col(u['products'], (['commander'] if 'commander' in C.PAGES else []) + ['couleur', 'blancs', 'gros', 'livraison', 'apropos'])}
{col(u['sectors'], [k for k in C.SECTOR_KEYS if k != 'gros'] + ['secteurs'])}
{col(u['guides'], ['guide-huileux', 'guide-papier', 'guide-ratine', 'guide-ranger', 'glossaire', 'calculateur', 'faq'])}
</div>
<div class="ftop"><div class="legal">Entretien Laval · NEQ 2280629637 · TPS 783132566 RT0001 · TVQ 4054025241 TQ0001<br>309-1355 Boul. Le Corbusier, Laval, QC H7N 0G4</div><div class="legal cityline">{u['delivery_to']} {" · ".join(f'<a href="{L(k, lang)}">{C.PAGES[k][lang]["short"]}</a>' for k in C.CITY_KEYS)}</div></div>
<div class="fbot"><span>© {YEAR} Entretien Laval — Chiffons ÉCO / ECO Rags</span><span><a href="{L('home', 'fr')}" lang="fr-CA">Français</a> · <a href="{L('home', 'en')}" lang="en-CA">English</a></span></div>
</div>
</footer>
<a class="wafab" href="{C.WA[lang]}" target="_blank" rel="noopener" aria-label="{u['wa_fab']}">{ICON['wa'].replace('<svg', HID, 1)}<span>WhatsApp</span></a>
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
    return f'<div class="pbox"><h2>{fill(u["prices_h"], lang)}</h2>{rows}<p class="small">{u["prices_note"]}</p>{order_btn(lang)}<a class="btn btn-primary" href="{L("home#devis", lang)}">{u["quote"]}</a><a class="btn btn-ghost" href="{C.TEL}">{u["call_btn"]} {C.PHONE}</a></div>'

def order_btn(lang):
    if "commander" not in C.PAGES: return ""
    return f'<a class="btn btn-primary" href="{L("commander", lang)}">{C.PAGES["commander"][lang]["short"]}</a>'

def order_html(lang):
    ck, ou = O.CHECKOUT, O.UI[lang]
    qty = "".join(f'<div><label for="o-{p["id"]}">{p[lang][0]} – {price(p["price"], lang)}</label><input id="o-{p["id"]}" class="oqty" data-id="{p["id"]}" type="number" min="0" max="{ck["max_bags"]}" step="1" value="0" inputmode="numeric"></div>' for p in C.PRODUCTS)
    def fld(name, label, typ="text", req=True, ac="", full=False, extra=""):
        star = " *" if req else ""
        tag = f'<textarea id="o-{name}" name="{name}" maxlength="500"></textarea>' if typ == "textarea" else f'<input id="o-{name}" name="{name}" type="{typ}"{" required" if req else ""}{" autocomplete=" + chr(34) + ac + chr(34) if ac else ""}{extra}>'
        return f'<div{" class=" + chr(34) + "full" + chr(34) if full else ""}><label for="o-{name}">{label}{star}</label>{tag}</div>'
    fields = (fld("nom", ou["name"], ac="name") + fld("entreprise", ou["company"], req=False, ac="organization")
              + fld("courriel", ou["email"], "email", ac="email") + fld("telephone", ou["phone"], "tel", ac="tel", extra=' minlength="7"')
              + fld("adresse", ou["address"], ac="street-address", full=True) + f'<div><label for="o-ville">{ou["city"]} *</label><select id="o-ville" name="ville" required autocomplete="address-level2"><option value="">–</option>' + "".join(f'<option value="{esc(z["name"])}">{esc(z["name"])}</option>' for z in ck["zones"]) + '</select></div>'
              + fld("code_postal", ou["postal"], ac="postal-code", extra=' maxlength="7" placeholder="H7N 0G4"')
              + fld("instructions", ou["notes"], "textarea", req=False, full=True))
    rows = "".join(f'<tr><th scope="row">{a}</th><td id="{b}">–</td></tr>' for a, b in [(ou["goods"], "o-goods"), (ou["delivery"], "o-del"), (ou["gst"], "o-gst"), (ou["qst"], "o-qst")])
    cfg = {"lang": lang, "zones": ck["zones"], "free": ck["free_delivery_from"], "max": ck["max_bags"], "gst": ck["gst"], "qst": ck["qst"],
           "postal": ck["postal_regex"], "fn": "/.netlify/functions", "thanks": L("merci", lang), "ui": ou,
           "products": [{"id": p["id"], "price": p["price"], "name": p[lang][0]} for p in C.PRODUCTS]}
    names = ["langue", "commande_paypal", "capture", "statut", "montant", "details", "totaux", "nom", "entreprise", "courriel", "telephone", "adresse", "ville", "code_postal", "instructions"]
    hidden = '<form name="commande" data-netlify="true" netlify-honeypot="bot-field" hidden><input name="bot-field">' + "".join(f'<input name="{n}">' for n in names) + "</form>"
    sdk = f'https://www.paypal.com/sdk/js?client-id={ck["paypal_client_id"]}&currency=CAD&intent=capture&components=buttons&enable-funding=card&locale={lang}_CA'
    return f"""<section class="section band" id="commande"><div class="wrap"><form class="qform oform" id="oform" novalidate>
<h3>{C.PAGES["commander"][lang]["h1"]}</h3><p class="sub">{ou["note"]}</p>
<div class="fgrid">{qty}</div>
<h3 style="margin-top:26px;font-size:20px">{ou["contact_h"]}</h3>
<div class="fgrid">{fields}</div>
<h3 style="margin-top:26px;font-size:20px">{ou["sum_h"]}</h3>
<table class="osum">{rows}<tr class="tot"><th scope="row">{ou["total"]}</th><td id="o-total">–</td></tr></table>
<p class="oerr" id="o-err" role="alert" hidden></p>
<div id="paypal-buttons" aria-label="{ou["pay_h"]}"></div>
</form>{hidden}</div></section>
<script src="{esc(sdk)}" defer></script>
<script>window.ORDER_CFG={json.dumps(cfg, ensure_ascii=False).replace("</", "<" + chr(92) + "/")};</script>
<script>{rd("order.js")}</script>"""

def checkout_catalog():
    ck = O.CHECKOUT
    os.makedirs(os.path.join(ROOT, "netlify", "lib"), exist_ok=True)
    cat = {"enabled": O.ready(), "zones": ck["zones"], "free": ck["free_delivery_from"], "max": ck["max_bags"],
           "gst": ck["gst"], "qst": ck["qst"], "postal": ck["postal_regex"],
           "products": {p["id"]: {"price": p["price"], "name_fr": p["fr"][0], "name_en": p["en"][0]} for p in C.PRODUCTS}}
    json.dump(cat, open(os.path.join(ROOT, "netlify", "lib", "catalog.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    if not O.ready():
        print("Online ordering OFF: set zones and paypal_client_id in tools/content_order.py")

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
            "offers": {"@type": "Offer", "price": f"{p['price']}.00", "priceCurrency": "CAD", "availability": "https://schema.org/InStock", "priceValidUntil": "2026-12-31",
                       "url": C.SITE + L(p["page"], lang), "seller": {"@id": BIZ_ID}}}

def business(lang):
    b = json.load(open(os.path.join(SRC, f"ld-{lang}.json"), encoding="utf-8"))["@graph"][0]
    b["image"] = [C.SITE + "/img/og-chiffons-eco.jpg", C.SITE + "/img/" + C.IMG_BAG]
    b["logo"] = C.SITE + "/img/logo-chiffons-eco-512.png"
    b["priceRange"] = "32 $ – 42 $" if lang == "fr" else "$32 – $42"
    b["areaServed"] = [{"@type": "City", "name": c} for c in ["Laval", "Montréal", "Longueuil", "Terrebonne", "Blainville", "Boisbriand", "Saint-Eustache", "Mirabel", "Saint-Jérôme", "Repentigny", "Brossard", "Boucherville", "Québec", "Lévis", "Sherbrooke", "Trois-Rivières", "Gatineau"]] + [{"@type": "AdministrativeArea", "name": "Québec"}]
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
    h = hashlib.sha1(re.sub(r"/assets/site\.[0-9a-f]+\.css", "", s).encode()).hexdigest()
    rel = os.path.relpath(out, ROOT)
    rec = DATES.get(path)
    if not rec:
        rec = {"published": git_date(rel, first=True), "modified": git_date(rel), "hash": h}
    elif rec["hash"] != h:
        rec = {**rec, "modified": TODAY, "hash": h}
    DATES[path] = rec
    s = s.replace(D_MOD, rec["modified"]).replace(D_PUB, rec["published"])
    open(out, "w", encoding="utf-8").write(s)

def gloss(t):
    if not t.get("terms"): return ""
    return '<dl class="gloss">' + "".join(f"<dt>{esc(a)}</dt><dd>{esc(b)}</dd>" for a, b in t["terms"]) + "</dl>"

def calc_html(t, lang):
    x = t["tool"]
    opts = "".join(f'<option value="{p["price"]}">{p[lang][0]} – {price(p["price"], lang)}</option>' for p in C.PRODUCTS)
    h = f"""<section class="section"><div class="wrap"><form class="calc" id="calc" onsubmit="return false">
<div class="row"><div><label for="c-lbw">{x['lbw']}</label><input id="c-lbw" type="number" min="1" step="1" value="25" inputmode="numeric"></div>
<div><label for="c-prod">{x['prod']}</label><select id="c-prod">{opts}</select></div>
<div><label for="c-zone">{x['zone']}</label><select id="c-zone"><option value="0">{x['z1']}</option><option value="1">{x['z2']}</option></select></div></div>
<div class="res" aria-live="polite"><div>{x['bags']}<output id="c-bags">–</output></div><div>{x['pre']}<output id="c-pre">–</output></div><div>{x['tax']}<output id="c-tax">–</output></div><div>{x['tot']}<output id="c-tot">–</output></div></div>
<p class="note" id="c-min" hidden></p></form></div></section>
<script>(function(){{var L='LANG',M=MINMSG;function f(n){{return L=='fr'?n.toLocaleString('fr-CA',{{minimumFractionDigits:2,maximumFractionDigits:2}})+' $':'$'+n.toLocaleString('en-CA',{{minimumFractionDigits:2,maximumFractionDigits:2}})}}
function g(i){{return document.getElementById(i)}}function r(){{var w=parseFloat(g('c-lbw').value)||0,pr=parseFloat(g('c-prod').value),z=g('c-zone').value=='1';
var bags=Math.ceil(w*52/12/25),pre=bags*pr,tax=Math.round(pre*0.14975*100)/100;g('c-bags').textContent=bags;g('c-pre').textContent=f(pre);g('c-tax').textContent=f(tax);g('c-tot').textContent=f(pre+tax);
var n=g('c-min');if(z&&w>0){{var m=Math.round(1000/(w*52/12)*10)/10;n.textContent=M.replace('{{m}}',m.toLocaleString(L=='fr'?'fr-CA':'en-CA'));n.hidden=false}}else n.hidden=true}}
['c-lbw','c-prod','c-zone'].forEach(function(i){{g(i).addEventListener('input',r)}});r()}})();</script>"""
    return h.replace("'LANG'", repr(lang)).replace("MINMSG", json.dumps(x["min"], ensure_ascii=False))

# ---------- subpages ----------
def subpage(key, lang):
    pg = C.PAGES[key]; t = pg[lang]; u = C.UI[lang]; kind = pg["kind"]
    parent = {"sector": [(C.PAGES["secteurs"][lang]["short"], L("secteurs", lang))], "product": [(u["products"], L("home#produits", lang))],
              "guide": [(C.PAGES["guides"][lang]["short"], L("guides", lang))], "tool": [(C.PAGES["guides"][lang]["short"], L("guides", lang))],
              "city": [(C.PAGES["livraison"][lang]["short"], L("livraison", lang))],
              "order": [(u["products"], L("home#produits", lang))]}.get(kind, [])
    ch, cj = crumbs(lang, parent + [(t["short"], L(key, lang))])
    faq = t.get("faq") or (C.FAQ[lang] if kind == "faq" else [])
    graph = [{"@type": "Article" if kind == "guide" else "WebPage", "@id": C.SITE + L(key, lang) + "#page", "url": C.SITE + L(key, lang),
              "name": t["title"], "headline": t["h1"], "description": t["desc"], "inLanguage": f"{lang}-CA",
              "isPartOf": {"@id": C.SITE + "/#website"}, "about": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "dateModified": D_MOD}, cj,
             {"@type": "LocalBusiness", "@id": BIZ_ID, "name": "Entretien Laval — Chiffons ÉCO", "url": C.SITE + "/", "telephone": "+1-438-831-3611"}]
    if kind == "guide": graph[0].update({"author": {"@id": BIZ_ID}, "image": C.SITE + "/img/" + pg["img"], "datePublished": D_PUB})
    if faq and kind != "thanks": graph.append(faq_ld(faq, lang))
    for pid in pg.get("products", []): graph.append(product_ld(pid, lang))
    if kind == "city":
        cname = pg["city"] if lang == "fr" else pg["city_en"]
        graph.append({"@type": "Service", "name": t["h1"], "serviceType": "Livraison de chiffons d'essuyage recyclés" if lang == "fr" else "Recycled wiping rag delivery",
                      "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "Place", "name": cname.replace("la ", "").replace("the ", "")},
                      "offers": [{"@type": "Offer", "price": f"{q['price']}.00", "priceCurrency": "CAD", "itemOffered": {"@type": "Product", "name": f"{q[lang][0]} – {C.PACK[lang][0]}"}} for q in C.PRODUCTS]})
    if t.get("terms"):
        graph.append({"@type": "DefinedTermSet", "name": t["h1"], "inLanguage": f"{lang}-CA", "hasDefinedTerm": [{"@type": "DefinedTerm", "name": a, "description": b} for a, b in t["terms"]]})
    lst = {"guides": C.GUIDE_KEYS, "hub": [k for k in C.SECTOR_KEYS if k != "gros"]}.get(kind) or (C.CITY_KEYS if key == "livraison" else None)
    if lst:
        graph.append({"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": C.SITE + L(k, lang), "name": C.PAGES[k][lang]["short"]} for i, k in enumerate(lst)]})
    noindex = kind == "thanks"
    media = f'<div class="frame">{img_tag(pg["img"], t["alt"], lazy=False, hi=True)}</div>' if pg.get("img") else ""
    hero_cta = "" if noindex else f'<div class="cta-row"><a class="btn btn-primary" href="{L("home#devis", lang)}">{u["quote"]}</a><a class="btn btn-ghost" href="{C.TEL}">{u["call_btn"]} {C.PHONE}</a></div>'
    if noindex: hero_cta = f'<div class="cta-row"><a class="btn btn-primary" href="{L("home", lang)}">{u["home"]}</a></div>'
    hero = f'<section class="phero"><div class="wrap {"phero-grid" if media else ""}"><div><div class="eyebrow">{t["eyebrow"]}</div><h1>{t["h1"]}</h1><p class="lede">{fill(t["lede"], lang)}</p>{hero_cta}</div>{media}</div></section>'
    body = ""
    if kind in ("sector", "product", "info", "guide", "city", "tool", "order"):
        ids = pg.get("products")
        side = price_box(lang, ids)
        if kind == "product":
            prods = "".join(f'<div class="prod"><span class="code">{PROD[i][lang][1]}</span><h3>{PROD[i][lang][0]}</h3><div class="price">{price(PROD[i]["price"], lang)}<small>{fill(u["unit"], lang)}</small></div><p>{PROD[i][lang][2]}</p></div>' for i in ids)
            body += f'<section class="section band"><div class="wrap"><div class="prods" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">{prods}</div><div class="terms">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in C.TERMS[lang]) + "</div></div></section>"
        if kind in ("info", "city"):
            body += f'<section class="section band"><div class="wrap"><div class="terms" style="margin-top:0">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in C.TERMS[lang]) + "</div></div></section>"
        if kind == "tool": body += calc_html(t, lang)
        if kind == "order": body += order_html(lang)
        body += f'<section class="section"><div class="wrap cgrid"><article class="prose">{fill(t["body"], lang)}{gloss(t)}</article><aside class="side">{side}</aside></div></section>'
        if faq: body += f'<section class="section band"><div class="wrap"><div class="sec-head"><h2>{u["faq_h"]}</h2></div>{faq_html(faq, lang)}</div></section>'
    elif kind == "faq":
        body += f'<section class="section"><div class="wrap cgrid"><div>{faq_html(faq, lang)}</div><aside class="side">{price_box(lang)}</aside></div></section>'
    elif kind in ("guides", "hub"):
        if t.get("body"): body += f'<section class="section" style="padding-bottom:0"><div class="wrap"><div class="prose">{fill(t["body"], lang)}</div></div></section>'
        body += f'<section class="section"><div class="wrap">{cards(C.GUIDE_KEYS if kind == "guides" else [k for k in C.SECTOR_KEYS if k != "gros"], lang, u["read"] if kind == "guides" else None)}</div></section>'
    if key == "livraison":
        body += f'<section class="section"><div class="wrap"><div class="sec-head"><h2>{"Villes et régions desservies" if lang == "fr" else "Cities and regions we serve"}</h2></div>{cards(C.CITY_KEYS, lang)}</div></section>'
    if pg["rel"]:
        body += f'<section class="section"><div class="wrap"><div class="sec-head"><h2>{u["related"]}</h2></div>{cards(pg["rel"], lang)}</div></section>'
    if not noindex: body += ctaband(lang)
    if kind == "thanks":
        msg = {"fr": ("Merci! Votre paiement est reçu.", "Commande no {id}. Nous vous contactons rapidement pour fixer la date de livraison. Questions : 438-831-3611."),
               "en": ("Thank you! Your payment was received.", "Order no. {id}. We'll contact you shortly to set the delivery date. Questions: 438-831-3611.")}[lang]
        body += ("<script>(function(){var id=new URLSearchParams(location.search).get('commande');if(!id)return;"
                 f"document.querySelector('h1').textContent={json.dumps(msg[0], ensure_ascii=False)};"
                 f"var l=document.querySelector('.lede');if(l)l.textContent={json.dumps(msg[1], ensure_ascii=False)}.replace('{{id}}',id.slice(0,40));}})();</script>")
    img = "/img/" + pg["img"] if pg.get("img") else "/img/og-chiffons-eco.jpg"
    doc = head(lang, t["title"], t["desc"], key, {"@context": "https://schema.org", "@graph": graph}, image=img, noindex=noindex, image_alt=t.get("alt", "") if pg.get("img") else "",
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
    prods = "".join(f'<div class="prod"><span class="code">{p[lang][1]}</span><h3>{p[lang][0]}</h3><div class="price">{price(p["price"], lang)}<small>{fill(u["unit"], lang)}</small></div><p>{p[lang][2]}</p><a href="{L(p["page"], lang)}">{u["more"]}</a></div>' for p in C.PRODUCTS)
    terms = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in C.TERMS[lang])
    photos = f'<div class="prodphoto"><div class="frame">{img_tag(C.IMG_BAG, h["photo_alt"][1])}</div><div class="frame">{img_tag(C.IMG_BAGS, h["photo_alt"][0])}</div></div>'
    products = f'<section class="section" id="produits"><span id="grades"></span><div class="wrap"><div class="sec-head"><div class="eyebrow">{h["prod_eyebrow"]}</div><h2>{h["prod_h2"]}</h2><p>{fill(h["prod_p"], lang)}</p></div><div class="prods">{prods}</div><div class="terms">{terms}</div>{photos}</div></section>'
    part = part.replace("<!--PRODUCTS-->", products)
    sectors = f'<section class="section" id="secteurs"><span id="uses"></span><div class="wrap"><div class="sec-head"><div class="eyebrow">{h["sec_eyebrow"]}</div><h2>{h["sec_h2"]}</h2><p>{h["sec_p"]}</p></div>{cards(C.SECTOR_KEYS, lang)}</div></section>'
    cities = "".join(f'<a href="{L(k, lang)}">{C.PAGES[k][lang]["short"]}</a>' for k in C.CITY_KEYS) + f'<span>{"Partout au Québec (1 000 lb +)" if lang == "fr" else "Anywhere in Québec (1,000 lb +)"}</span>'
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
             {"@type": "WebPage", "@id": C.SITE + h["path"] + "#page", "url": C.SITE + h["path"], "name": h["title"], "description": h["desc"], "inLanguage": f"{lang}-CA", "isPartOf": {"@id": C.SITE + "/#website"}, "about": {"@id": BIZ_ID}, "dateModified": D_MOD}]
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
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for k in indexable():
        for l in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}-CA" href="{C.SITE}{L(k, x)}"/>' for x in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{C.SITE}{L(k, "fr")}"/>'
            im = C.IMG_BAG if k == "home" else C.PAGES[k].get("img")
            imtag = f"<image:image><image:loc>{C.SITE}/img/{im}</image:loc></image:image>" if im else ""
            out.append(f"<url><loc>{C.SITE}{L(k, l)}</loc><lastmod>{DATES.get(L(k, l), {}).get('modified', TODAY)}</lastmod>{alts}{imtag}</url>")
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
    ai = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'Google-Extended', 'Bingbot', 'Applebot-Extended', 'CCBot'])
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /merci/\nDisallow: /en/thanks/\n\n{ai}Sitemap: {C.SITE}/sitemap.xml\n")
    full = lines[:]
    for l in LANGS:
        full += ["", "## " + ("Pages (français)" if l == "fr" else "Pages (English)")]
        for k in indexable():
            if k == "home": continue
            t = C.PAGES[k][l]
            full += ["", f"### {t['h1']}", f"URL: {C.SITE}{L(k, l)}", text(fill(t['desc'], l))]
            full += [f"- Q: {text(fill(q, l))} A: {text(fill(a, l))}" for q, a in t.get("faq", [])]
        full += ["", "## FAQ"] + [f"- Q: {text(fill(q, l))} A: {text(fill(a, l))}" for q, a in C.FAQ[l]]
    open(os.path.join(ROOT, "llms-full.txt"), "w").write("\n".join(full) + "\n")
    open(os.path.join(ROOT, f"{C.INDEXNOW_KEY}.txt"), "w").write(C.INDEXNOW_KEY)

# ---------- icons, Merchant Center feeds ----------
def icons():
    logo = Image.open(os.path.join(ROOT, "img", "logo-chiffons-eco-512.png")).convert("RGBA")
    logo.resize((180, 180), Image.LANCZOS).save(os.path.join(ROOT, "apple-touch-icon.png"))
    logo.resize((48, 48), Image.LANCZOS).save(os.path.join(ROOT, "favicon-48.png"))

# Only products with a REAL photo of that product go in the feed (Google rejects mismatched images).
FEED_IMG = {"tshirt-couleur": C.IMG_BAG, "ratine-couleur": C.IMG_BAG}  # add the white rags once a white-bag photo exists

def merchant_feed(lang):
    ptype = "Chiffons d'essuyage recyclés" if lang == "fr" else "Recycled wiping rags"
    items = []
    for p in C.PRODUCTS:
        src = FEED_IMG.get(p["id"])
        if not src:
            continue
        jpg = os.path.splitext(src)[0] + "-feed.jpg"
        if not os.path.exists(os.path.join(ROOT, "img", jpg)):
            Image.open(os.path.join(ROOT, "img", src)).convert("RGB").save(os.path.join(ROOT, "img", jpg), "JPEG", quality=88)
        name, _, d = p[lang]
        items.append(
            f"<item><g:id>{p['id']}</g:id><title>{esc(name + ' – ' + C.PACK[lang][0])}</title>"
            f"<description>{esc(d)}</description><link>{C.SITE}{L(p['page'], lang)}</link>"
            f"<g:image_link>{C.SITE}/img/{jpg}</g:image_link><g:price>{p['price']}.00 CAD</g:price>"
            f"<g:availability>in_stock</g:availability><g:condition>new</g:condition><g:brand>Chiffons ÉCO</g:brand>"
            f"<g:identifier_exists>no</g:identifier_exists><g:shipping_weight>25 lb</g:shipping_weight>"
            f"<g:product_type>{esc(ptype)}</g:product_type></item>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0"><channel>'
           f"<title>Chiffons ÉCO ({lang})</title><link>{C.SITE}{L('home', lang)}</link><description>Chiffons ÉCO</description>"
           + "".join(items) + "</channel></rss>\n")
    open(os.path.join(ROOT, f"merchant-feed-{lang}.xml"), "w", encoding="utf-8").write(xml)

CSS = build_css()
icons()
for l in LANGS:
    homepage(l)
    for k in C.PAGES: subpage(k, l)
notfound(); sitemap(); llms()
merchant_feed("fr"); merchant_feed("en")
checkout_catalog()
json.dump(DATES, open(DATES_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
print("built", 2 * (1 + len(C.PAGES)), "pages + 404;", CSS)
