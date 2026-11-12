import concurrent.futures as cf
import json
import ssl
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
CTX = ssl.create_default_context()


def urls(d):
    out = {}
    for k, s in d["sources"].items():
        out.setdefault(s["url"], f"fuente:{k}")
    for p in d["places"]:
        for l in p["links"]:
            out.setdefault(l["url"], f"local:{p['name']}")
        for x in p["discounts"]:
            out.setdefault(x["url"], f"descuento:{p['name']}")
        for a in p["acts"]:
            for pp in a["people"]:
                if pp.get("u"):
                    out.setdefault(pp["u"], f"persona:{pp['n']}")
    return out


def check(u):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, method=method, headers={"User-Agent": UA, "Accept-Language": "es-UY,es"})
            with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 400, 404, 429, 999):
                return e.code, u
        except Exception as e:
            if method == "GET":
                return f"ERR {type(e).__name__}: {str(e)[:80]}", u
    return "?", u


def main():
    d = json.loads((HERE / "data.json").read_text(encoding="utf-8"))
    U = urls(d)
    res = {}
    with cf.ThreadPoolExecutor(12) as ex:
        for u, r in zip(U, ex.map(check, U)):
            res[u] = r
    bad = [(U[u], u, s, f) for u, (s, f) in res.items() if not (isinstance(s, int) and s < 400)]
    print(f"{len(U)} URLs, {len(bad)} con problema")
    for who, u, s, f in sorted(bad):
        print(f"  [{s}] {who} -> {u}")
    (HERE / "link-report.json").write_text(json.dumps({u: [U[u], str(s), f] for u, (s, f) in res.items()}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
