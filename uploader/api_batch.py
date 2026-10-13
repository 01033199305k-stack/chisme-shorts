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
    ap.add_argument("--day", default="auto", help="1-3, or auto = from today's KST date")
    ap.add_argument("--dir", default="videos")
    a = ap.parse_args()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    n_day = (dt.datetime.now(KST).date() - START).days + 1 if a.day == "auto" else int(a.day)
    if n_day not in PLAN:
        print(f"day {n_day}: nothing planned (batch1 runs {START} + {len(PLAN)} days)")
        return 0
    day = START + dt.timedelta(days=n_day - 1)
    rc = 0
    for n, hour in zip(PLAN[n_day], SLOTS_KST):
        if state.get(n, {}).get("video_id"):
            print(n, "already uploaded:", state[n]["url"])
            continue
        mp4 = next(Path(a.dir).glob(f"{n}-*.mp4"))
        script = json.loads(next(p for d in ("batch1", "test1") for p in (ROOT / d).glob(f"{n}-*.json")).read_text(encoding="utf-8"))
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
