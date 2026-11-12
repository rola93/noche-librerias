import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent
NS = {"k": "http://www.opengis.net/kml/2.2"}


def data(pm, name):
    for d in pm.findall("k:ExtendedData/k:Data", NS):
        if d.get("name") == name:
            return d.findtext("k:value", default="", namespaces=NS) or ""
    return ""


def desc_block(pm):
    raw = pm.findtext("k:description", default="", namespaces=NS) or ""
    t = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    m = re.search(r"descripción:(.*?)(?:\ndirección:|$)", t, flags=re.S)
    block = m.group(1) if m else ""
    m2 = re.search(r"Actividades:(.*?)(?:\nParticipantes:|$)", block, flags=re.S)
    return (m2.group(1).strip() if m2 else ""), block


root = ET.parse(HERE / "mapa-imm.kml").getroot()
out = []
for pm in root.findall(".//k:Placemark", NS):
    d_act, _ = desc_block(pm)
    out.append(
        {
            "name": pm.findtext("k:name", default="", namespaces=NS).strip(),
            "barrio": data(pm, "Barrio").strip(),
            "addr": (data(pm, "Dirección") or data(pm, "dirección") or pm.findtext("k:address", default="", namespaces=NS)).strip(),
            "participantes": data(pm, "Participantes").strip(),
            "act_ext": data(pm, "Actividades").strip(),
            "act_desc": d_act,
        }
    )

(HERE / "kml-raw.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
with open(HERE / "kml-raw.txt", "w", encoding="utf-8") as f:
    for p in out:
        f.write(f"\n########## {p['name']} | {p['barrio']} | {p['addr']}\n")
        if p["participantes"]:
            f.write(f"PARTICIPANTES: {p['participantes']}\n")
        f.write("--- EXT ---\n" + p["act_ext"] + "\n")
        if re.sub(r"\s+", " ", p["act_desc"]) != re.sub(r"\s+", " ", p["act_ext"]):
            f.write("--- DESC (difiere) ---\n" + p["act_desc"] + "\n")
print(len(out))
