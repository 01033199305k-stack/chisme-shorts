"""Test 1 (2026-10-13): does a frame that does not match 썰가챠 get Shorts-feed impressions?

Day 1's four videos (썰가챠 pictures, layout, music copied 1:1) got 0% Shorts-feed traffic.
These two use the Chismepón theme (config theme: chisme, new BGM) AND pictures/stock searches
written fresh here (every segment patched). They fill 10/15 09:00 and 12:00, next to two
old-look batch1 videos at 03:00 and 06:00 the same day.

    python test1/specs.py      # writes test1/<slug>.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from adapt import adapt   # noqa: E402

SRC = Path.home() / "issue-shorts" / "scripts"


def it(q, size="l", pos="center", fx="pop", at=0.0):
    return {"type": "illust", "q": q, "pos": pos, "size": size, "at": at, "fx": fx}


def emo(t, pos="top-right", fx="pop", at=0.4):
    return {"type": "emoji", "text": t, "pos": pos, "size": "s", "at": at, "fx": fx}


POST = {"type": "text", "style": "post", "text": "", "pos": "center", "at": 0.0, "fx": "pop"}

SPECS = [
 {"src": "2026-10-07-1800", "lane": "A", "slug": "es-baby-climbs-mountain", "out": "t1-0900",
  "title": ["Tiene 9 meses", "y ya sube montañas"],
  "lines": ["Un bebé de 9 meses\nsubió una montaña gateando",
            "Y la razón de su papá es todavía más rara.",
            "En China, subió escalón por escalón con rodilleras.",
            "Empezó a gatear a los 6 meses y a los 8 ya subía escaleras.",
            "¿Y por qué lo llevó su papá?",
            "No era entrenamiento: era para que gastara energía.",
            "El video tuvo 200 mil likes, y la gente se dividió.",
            "¿Tú llevarías a tu bebé?"],
  "say": {"0": "Un bebé de nueve meses subió una montaña gateando",
          "3": "Empezó a gatear a los seis meses y a los ocho ya subía escaleras.",
          "6": "El video tuvo doscientos mil likes, y la gente se dividió."},
  "patch": {
      "0": {"bg": "white", "items": [POST]},
      "1": {"bg": "park", "items": [it(["お父さん 赤ちゃん 抱っこ", "父親 赤ちゃん", "お父さん"]), emo("🤔")]},
      "2": {"bg": "mountain", "video": ["mountain stone stairs", "stone steps trail", "mountain stairs hiking"],
            "items": [it(["登山 赤ちゃん", "ハイハイ"], size="s", pos="top-left")]},
      "3": {"bg": "living", "items": [it(["ハイハイ", "赤ちゃん ハイハイ"]), emo("📅")]},
      "4": {"bg": "night", "items": [it(["考える 男性", "父親"]), emo("❓")]},
      "5": {"bg": "park", "items": [it(["走る 子供", "元気な子供"]), emo("⚡")]},
      "6": {"bg": "white", "video": ["people watching phone", "scrolling phone feed", "smartphone hand scrolling"],
            "items": [emo("👍", pos="right")]},
      "7": {"bg": "mountain", "cap": "react", "items": [it(["山登り", "ハイキング"]), emo("🏔️")]}},
  "yt": {"title": "Tiene 9 meses y ya sube montañas gateando #shorts",
         "description": "En una zona turística de montaña en Hubei, China, un bebé de 9 meses subió los escalones "
                        "gateando, con rodilleras. Empezó a gatear a los 6 meses y a los 8 ya subía escaleras. "
                        "Su papá dijo que no era entrenamiento, sino para que gastara energía. El video tuvo "
                        "unos 200 mil likes y opiniones divididas.",
         "tags": ["bebé", "montaña", "china", "viral", "historias reales", "chisme"]}},
 {"src": "2026-10-06-1800", "lane": "K", "slug": "es-fried-chicken-weight", "out": "t1-1200",
  "pick": [0, 2, 3, 5, 6, 7, 8, 9],
  "title": ["Pidió pollo de 1 kilo", "y pesó 695 gramos"],
  "lines": ["Pidió pollo de 1 kilo\ny pesó solo 695 gramos",
            "En Corea, una asociación de consumidores pesó pollo frito de 5 marcas.",
            "Uno llegó más de 30% más ligero de lo que dice el menú.",
            "¿Y saben por qué no es trampa?",
            "El peso del menú es del pollo crudo, antes de freírlo.",
            "Al freírlo pierde agua, así que te llega más ligero.",
            "¡Pero otro pollo con salsa pesó 17% más de lo anunciado!",
            "¿Tú pesas tu pedido?"],
  "say": {"0": "Pidió pollo de un kilo y pesó solo seiscientos noventa y cinco gramos",
          "1": "En Corea, una asociación de consumidores pesó pollo frito de cinco marcas.",
          "2": "Uno llegó más de treinta por ciento más ligero de lo que dice el menú.",
          "6": "¡Pero otro pollo con salsa pesó diecisiete por ciento más de lo anunciado!"},
  "patch": {
      "0": {"bg": "white", "items": [POST]},
      "1": {"bg": "kitchen", "video": ["fried chicken", "chicken wings", "chicken fried"],
            "items": [it(["フライドチキン", "からあげ"], size="s", pos="top-left")]},
      "2": {"bg": "restaurant", "items": [it(["キッチンスケール", "はかり デジタル", "はかり"]), emo("📉")]},
      "3": {"bg": "night", "items": [it(["探偵", "虫眼鏡 男性"]), emo("🕵️")]},
      "4": {"bg": "kitchen", "items": [it(["鶏肉", "生肉"]), emo("🐔")]},
      "5": {"bg": "white", "video": ["frying oil pan", "chicken frying", "oil frying"],
            "items": [it(["揚げ物", "天ぷら"], size="s", pos="top-left")]},
      "6": {"bg": "white", "cap": "hit", "items": [it(["驚く 女性", "びっくり 女性"]), emo("📈")]},
      "7": {"bg": "living", "cap": "react", "items": [it(["出前 受け取る", "宅配 受け取る", "出前"]), emo("⚖️")]}},
  "yt": {"title": "Pidió pollo de 1 kilo y pesó solo 695 gramos #shorts",
         "description": "En Corea del Sur, una asociación de consumidores pesó el pollo frito a domicilio de 5 marcas. "
                        "Uno pesó en promedio 695 gramos, más de 30% menos de lo que dice el menú. No es trampa: el "
                        "peso anunciado es del pollo crudo, y al freírlo pierde agua. Otro, con salsa, pesó 17% más.",
         "tags": ["pollo frito", "corea", "comida", "delivery", "historias reales", "chisme coreano"]}},
]

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    from rules import lint, validate
    for es in SPECS:
        src = json.loads((SRC / f"{es['src']}.json").read_text(encoding="utf-8"))
        s = adapt(src, es)
        out = ROOT / "test1" / f"{es['out']}-{es['slug']}.json"
        out.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
        probs = validate(s) + lint(s)
        print(out.name, sum(len(x["say"]) for x in s["segments"]), "chars", "OK" if not probs else "")
        for p in probs:
            print("   ", p)
