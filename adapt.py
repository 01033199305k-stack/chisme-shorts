"""썰가챠 script + Spanish words -> Chismepón script.

The pictures, stock-video searches, sound effects and caption colours of the Korean
script are kept; every word a viewer hears or reads is replaced. The writer (ROUTINE.md,
or batch1/build.py) only supplies the Spanish:

    {"src": "2026-10-13-0700",                 # 썰가챠 scripts/<src>.json
     "lane": "A" | "K",                        # A = universal, K = "En Corea..." curiosity
     "slug": "es-...",
     "title": ["line 1", "line 2"],            # top band, max 22 chars each
     "lines": ["post card\\nin two lines", ...],   # one per Korean segment (or per `pick`)
     "say": {"3": "numbers spelled out ..."},  # optional: what the voice reads, by index
     "panel": ["¿Tú qué harías?", "① ...", "② ..."],   # vote-board words, in order
     "yt": {"title": "... #shorts", "description": "...", "tags": [...]},
     "pick": [0, 2, 3],                        # optional: keep only these Korean segments
     "patch": {"1": {"video": [...], "bg": "street", "cap": "hit"}}}   # optional

    python adapt.py es.json scripts/2026-10-16-0300.json [--src-dir ../issue-shorts/scripts]
"""
import argparse
import copy
import json
import sys
from pathlib import Path

AI = "\n\nNarración con voz generada por IA."
TAGS = "\n\n#chismepon #historias #chisme #shorts"


def adapt(src: dict, es: dict) -> dict:
    segs = copy.deepcopy([src["segments"][k] for k in es.get("pick", range(len(src["segments"])))])
    for k, ch in (es.get("patch") or {}).items():
        seg = segs[int(k)]
        vis = seg.setdefault("visual", {})
        for key, val in ch.items():
            if key == "cap":
                seg["cap"] = val
            else:
                vis[key] = val
    for seg in segs:   # いらすとや money is yen and its sake bottles carry kanji labels
        for it in (seg.get("visual") or {}).get("items", []):
            if it.get("type") == "illust" and isinstance(it.get("q"), list):
                if it["q"][0] in ("札束", "お金", "一万円札"):
                    it.update(type="emoji", text="💵", size=it.get("size", "l"), fx="drop")
                    it.pop("q")
                elif it["q"][0].startswith("日本酒"):
                    it["q"] = ["ワイン ボトル", "酒瓶"]
    if "pick" in es:   # early scripts: panel words repeat the caption - keep only the post card and the vote rows
        for seg in segs:
            vis = seg.get("visual") or {}
            its = vis.get("items", [])
            rows = sum(1 for it in its if it.get("style") == "row") >= 2
            vis["items"] = [it for it in its if it.get("type") != "text" or it.get("style") in ("post", "row")
                            or (rows and it.get("style") == "label")]
    if len(segs) != len(es["lines"]):
        raise ValueError(f"{len(es['lines'])} Spanish lines for {len(segs)} segments - one line per segment")
    panel = list(es.get("panel", []))
    say = {int(k): v for k, v in (es.get("say") or {}).items()}
    for i, (seg, line) in enumerate(zip(segs, es["lines"])):
        spoken = line.replace("\n", " ")
        seg["text"] = spoken
        seg["say"] = say.get(i, spoken)
        seg.pop("tone", None)   # Korean acting notes; the Spanish voice gets the channel-wide instruct
        for it in (seg.get("visual") or {}).get("items", []):
            if it.get("type") != "text":
                continue
            if it.get("style") == "post":
                it["text"] = line
            elif panel:
                it["text"] = panel.pop(0)
            else:
                raise ValueError(f"segment {i}: panel text {it.get('text')!r} has no Spanish in 'panel'")
    if panel:
        raise ValueError(f"unused panel text {panel}")
    yt = es["yt"]
    return {
        "skip": False, "skip_reason": "", "slug": es["slug"], "title_lines": es["title"], "credit": "",
        "segments": segs,
        "youtube": {"title": yt["title"], "description": yt["description"] + AI + TAGS, "tags": yt["tags"]},
        "source_post": src.get("source_post") or "https://example.invalid",
        "facts_used": src.get("facts_used", []),
        "brief": f"lane {es['lane']} - Spanish rewrite of 썰가챠 {es['src']}",
    }


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("es")
    ap.add_argument("out")
    ap.add_argument("--src-dir", default=str(Path(__file__).resolve().parent.parent / "issue-shorts" / "scripts"))
    a = ap.parse_args()
    es = json.loads(Path(a.es).read_text(encoding="utf-8"))
    src = json.loads((Path(a.src_dir) / f"{es['src']}.json").read_text(encoding="utf-8"))
    script = adapt(src, es)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(script, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
