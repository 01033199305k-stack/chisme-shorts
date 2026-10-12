"""Schedule one day of batch1 through the YouTube API (same upload.py as 썰가챠).

The mp4s are the ones rendered and checked on the PC, attached to the GitHub release
`batch1`. Runs in Actions (upload-batch.yml), where the YOUTUBE_* secrets live.

    python uploader/api_batch.py --day 1 --dir videos
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from uploader.run import PLAN, SLOTS_KST, START   # noqa: E402  (one schedule for both upload paths)
import upload as yt                              # noqa: E402  (repo-root upload.py)

KST = dt.timezone(dt.timedelta(hours=9))
STATE = ROOT / "state" / "batch1.json"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, required=True)
    ap.add_argument("--dir", default="videos")
    a = ap.parse_args()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    day = START + dt.timedelta(days=a.day - 1)
    rc = 0
    for n, hour in zip(PLAN[a.day], SLOTS_KST):
        if state.get(n, {}).get("video_id"):
            print(n, "already uploaded:", state[n]["url"])
            continue
        mp4 = next(Path(a.dir).glob(f"{n}-*.mp4"))
        script = json.loads(next((ROOT / "batch1").glob(f"{n}-*.json")).read_text(encoding="utf-8"))
        meta = script["youtube"]
        at = dt.datetime(day.year, day.month, day.day, hour, tzinfo=KST)
        print(f"=== {n} -> {at:%Y-%m-%d %H:%M} KST: {meta['title']}")
        try:
            res = yt.upload(str(mp4), meta["title"], meta["description"], meta["tags"], at)
        except Exception as ex:
            print(f"::error::{n}: {ex}")
            rc = 1
            continue
        print("  ", res)
        state[n] = {"video_id": res["id"], "url": res["url"], "privacy": res["privacy"],
                    "publish_at": res["publish_at"], "title": meta["title"], "lane": script["brief"].split()[1]}
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    return rc


if __name__ == "__main__":
    sys.exit(main())
