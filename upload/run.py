"""Schedule one day's Chismepón uploads in YouTube Studio through the Aside browser.

    python upload/run.py --day 1            # uploads day 1's videos, scheduled
    python upload/run.py --day 1 --only 03  # just one
    python upload/run.py --day 1 --draft    # stop before Schedule (private draft)

4 a day at 12/15/18/21 h Mexico City = 03/06/09/12 h KST. Universal (A) and Korea (K)
stories alternate so the two lanes get the same slots. State: upload/state.json.
"""
import argparse
import datetime as dt
import functools
import http.server
import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEOS = Path.home() / "Desktop" / "Chismepón 1차"
ASIDE = Path(os.environ["LOCALAPPDATA"]) / "Aside" / "CLI" / "current" / "aside.exe"
STATE = ROOT / "upload" / "state.json"
SLOTS_KST = [3, 6, 9, 12]
PLAN = {   # day -> batch1 numbers, A/K alternating
    1: ["03", "06", "02", "07"],
    2: ["05", "09", "04", "10"],
    3: ["01", "08"],
}
START = dt.date(2026, 10, 13)   # day 1 (KST)


def kst_label(h: int) -> str:
    return f"{'오전' if h < 12 else '오후'} {h if h <= 12 else h - 12}:00"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, required=True)
    ap.add_argument("--only")
    ap.add_argument("--draft", action="store_true")
    a = ap.parse_args()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    day = START + dt.timedelta(days=a.day - 1)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8766), functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=str(VIDEOS)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    tpl = (ROOT / "upload" / "up.js").read_text(encoding="utf-8")
    for n, hour in zip(PLAN[a.day], SLOTS_KST):
        if a.only and n != a.only:
            continue
        if state.get(n, {}).get("link"):
            print(n, "already uploaded:", state[n]["link"])
            continue
        mp4 = next(VIDEOS.glob(f"{n}-*.mp4"))
        script = json.loads(next((ROOT / "batch1").glob(f"{n}-*.json")).read_text(encoding="utf-8"))
        yt = script["youtube"]
        meta = {"file": mp4.name, "title": yt["title"], "description": yt["description"], "tags": yt["tags"],
                "dateText": f"{day.year}. {day.month}. {day.day}.", "dateCheck": f"{day.year}.{day.month}.{day.day}",
                "timeText": kst_label(hour)}
        js = tpl.replace("__META__", json.dumps(meta, ensure_ascii=False)).replace("__PUBLISH__", "false" if a.draft else "true")
        print(f"=== {n} -> {day} {meta['timeText']} KST: {yt['title']}")
        out = subprocess.run([str(ASIDE), "repl", js], capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=900).stdout
        tail = "\n".join(out.strip().splitlines()[-8:])
        print(tail)
        m = re.search(r"LINK (\S+)", out)
        state[n] = {"day": str(day), "time": meta["timeText"], "title": yt["title"],
                    "link": m.group(1) if m and m.group(1) != "(none)" else "",
                    "stopped": "STOP:" in out}
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
        if "STOP:" in out:
            print("  -> stopped before scheduling; fix up.js before the next one")
            break
    srv.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
