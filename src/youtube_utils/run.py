from . import Youtube, Path
import sqlite3
import pandas as pd


def main():
    yt = Youtube("vivaldi")
    folder = Path(".cache")

    watch_later = yt.watch_later()
    entries = watch_later.items()
    raw = folder / "watch-later.entries.json"
    raw.write_json(watch_later.raw_data())
    df = pd.DataFrame(entries)
    # df.to_csv('data.csv', index=False)
    conn = sqlite3.connect(folder / "watch_later.db")
    df.to_sql("watch_later_table", conn, if_exists="replace")
    df.to_csv(folder / "watch_later.csv")
    (folder / "watch-later.json").write_json(entries)
