import json
import re
import sys
import unicodedata
from pathlib import Path

from base import PLACES, SOURCES

HERE = Path(__file__).parent
OUT = HERE.parent / "site" / "index.html"

TAGS = {
    "ninos": "Para niños",
    "musica": "Música en vivo",
    "charla": "Charla",
    "presentacion": "Presentación de libro",
    "lectura": "Lectura",
    "taller": "Taller",
}
ISSUER_NAMES = {
    "itau": "Itaú", "scotia": "Scotiabank", "oca": "OCA", "bbva": "BBVA", "brou": "BROU",
    "santander": "Santander", "hsbc": "HSBC", "clubelpais": "Club El País", "prex": "Prex",
    "midinero": "Midinero", "anda": "Anda", "creditel": "Creditel", "cabal": "Cabal",
    "mercadopago": "Mercado Pago", "libreria": "Propio de la librería",
}
ISSUER_ORDER = ["libreria", "itau", "scotia", "oca", "bbva", "brou"]


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load(name, default):
    p = HERE / name
    if not p.exists():
        print(f"aviso: falta {name}", file=sys.stderr)
        return default
    return json.loads(p.read_text(encoding="utf-8"))


BAD_LINK = re.compile(r"shops1000\.com|linkedin\.com|/shop/product/|/products/")


def clean_url(u):
    if "instagram.com" in u:
        u = u.split("?")[0]
    return u


def ok_url(u):
    return isinstance(u, str) and re.match(r"^https?://", u)


def main():
    people = {}
    for f in ("research-people-A.json", "research-people-B.json"):
        for k, v in load(f, {}).items():
            if v and ok_url(v.get("url")):
                people.setdefault(k.strip(), v["url"])

    place_research = {}
    for f in ("research-places-A.json", "research-places-B.json"):
        for e in load(f, []):
            place_research[e["name"].strip()] = e
    aliases = {
        "Librería Trazo (FADU)": "Librería Trazo (en FADU)",
        "Centro de Fotografía de Montevideo": "Centro de Fotografía de Montevideo (CdF)",
    }

    disc = load("research-discounts.json", {"verified": []})
    discounts = {}
    for d in disc.get("verified", []):
        if not ok_url(d.get("url")):
            continue
        discounts.setdefault(d["place"].strip(), []).append(
            {"issuer": d["issuer"], "text": d["text"], "url": d["url"]}
        )
    discounts = load("discounts-manual.json", {})
    place_links_manual = load("links-manual.json", {})

    ilinks = load("research-interior-links.json", {"places": {}, "people": {}})
    for k, v in (ilinks.get("people") or {}).items():
        if v and ok_url(v.get("url")):
            people.setdefault(k.strip(), v["url"])
    people.update({k: v for k, v in load("people-manual.json", {}).items() if ok_url(v)})
    for k, v in load("people-manual.json", {}).items():
        if v is None:
            people.pop(k, None)

    places = [{**p, "city": "Montevideo", "dept": "Montevideo"} for p in PLACES]
    upd = load("interior-updates.json", {"sources": {}, "places": {}})
    for k, s in (upd.get("sources") or {}).items():
        if ok_url(s.get("url")):
            SOURCES.setdefault(k, {"label": s["label"], "url": s["url"]})
    for e in load("interior.json", []):
        u = (upd.get("places") or {}).get(e["name"])
        usrc = [u["src"]] if u and u.get("src") in SOURCES else []
        if u:
            e = dict(e)
            if u.get("addr"):
                e["addr"] = u["addr"]
            if u.get("hours"):
                e["hours"] = u["hours"]
            if u.get("note"):
                e["note"] = " ".join(x for x in (e.get("note"), u["note"]) if x)
            if u.get("acts"):
                e["acts"] = [{**a, "_src": usrc} for a in u["acts"]]
        hrs = e.get("hours") or [None, None]
        r = (ilinks.get("places") or {}).get(e["name"], {})
        links = place_links_manual.get(e["name"])
        if links is None:
            links = [
                {"label": l["label"], "url": clean_url(l["url"])}
                for l in (r.get("links") or [])
                if ok_url(l.get("url")) and not BAD_LINK.search(l["url"])
            ][:3]
        places.append({
            "name": e["name"], "city": e["city"], "dept": e["dept"],
            "barrio": e.get("barrio") or e["city"], "addr": e.get("addr") or "",
            **({"hours": hrs} if any(hrs) else {}),
            **({"note": e["note"]} if e.get("note") else {}),
            "links_override": links,
            "discount_text": e.get("discount"),
            "acts": [
                {"start": a.get("start"), "end": a.get("end"), "title": a["title"], "desc": a.get("desc") or "",
                 "tags": a.get("tags") or [], "people": a.get("people") or [], "src": a.get("_src") or ["mec"]}
                for a in e.get("acts", [])
            ],
        })

    used_issuers, missing_people, out_places = set(), set(), []
    for p in places:
        name = p["name"]
        r = place_research.get(name) or place_research.get(aliases.get(name, ""), {})
        links = p.get("links_override") if "links_override" in p else place_links_manual.get(name)
        if links is None:
            links = [
                {"label": l["label"], "url": clean_url(l["url"])}
                for l in (r.get("links") or [])
                if ok_url(l.get("url")) and not BAD_LINK.search(l["url"])
            ][:3]
        ds = discounts.get(name) or discounts.get(aliases.get(name, ""), [])
        if p.get("discount_text") and not ds:
            ds = [{"issuer": "libreria", "text": p["discount_text"], "url": SOURCES["mec"]["url"]}]
        for d in ds:
            used_issuers.add(d["issuer"])
        acts = []
        for a in p["acts"]:
            ppl = []
            for n in a["people"]:
                u = people.get(n)
                if not u:
                    missing_people.add(n)
                ppl.append({"n": n, **({"u": u} if u else {})})
            acts.append({**a, "people": ppl})
        out_places.append(
            {
                "id": slug(name + " " + p["city"]),
                "name": name,
                "city": p["city"],
                "dept": p["dept"],
                "barrio": p["barrio"],
                "addr": p["addr"],
                **({"hours": p["hours"]} if p.get("hours") else {}),
                "links": links,
                "discounts": ds,
                **({"note": p["note"]} if p.get("note") else {}),
                "acts": acts,
            }
        )

    issuers = {k: {"name": ISSUER_NAMES.get(k, k)} for k in ISSUER_ORDER if k in used_issuers}
    for k in sorted(used_issuers - set(ISSUER_ORDER)):
        issuers[k] = {"name": ISSUER_NAMES.get(k, k)}

    data = {
        "meta": {
            "title": "Noche de las Librerías 2026",
            "date": "Viernes 13 de noviembre",
            "hours": "la mayoría de 18:00 a 01:00",
            "day": "2026-11-13",
            "updated": "2026-11-12",
            "official": [
                {"label": "Mapa oficial (Montevideo)", "url": SOURCES["imm"]["url"]},
                {"label": "Guía del MEC (todo el país, PDF)", "url": SOURCES["mec"]["url"]},
            ],
        },
        "tags": TAGS,
        "issuers": issuers,
        "sources": SOURCES,
        "places": out_places,
    }
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    (HERE / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    assert tpl.count("__DATA__") == 1
    html = tpl.replace("__DATA__", js)
    OUT.write_text(html, encoding="utf-8")
    n_acts = sum(len(p["acts"]) for p in out_places)
    print(f"{len(out_places)} lugares, {n_acts} actividades, {len(OUT.read_bytes())} bytes -> {OUT}")
    print(f"emisores: {list(issuers)}")
    print(f"personas sin enlace ({len(missing_people)}): {sorted(missing_people)}")


if __name__ == "__main__":
    main()
