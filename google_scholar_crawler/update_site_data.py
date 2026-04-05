import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = ROOT / "results" / "data.json"
SITE_DATA_PATH = ROOT / "_data" / "scholar.json"


def main() -> None:
    with RESULTS_PATH.open("r", encoding="utf-8") as infile:
        author = json.load(infile)

    payload = {
        "citations": author.get("citedby", ""),
        "hindex": author.get("hindex", ""),
        "i10index": author.get("i10index", ""),
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

    SITE_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SITE_DATA_PATH.open("w", encoding="utf-8") as outfile:
        json.dump(payload, outfile, ensure_ascii=False, indent=2)
        outfile.write("\n")


if __name__ == "__main__":
    main()
