from yt_dlp import postprocessor

from . import Youtube, Path
import sqlite3
import pandas as pd

# from fastapi import FastAPI, BackgroundTasks
# import logging
#
# from youtube_watchlater_api.youtube import YoutubeTools
#
# logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.
#                                       # This will get the root logger since no logger in the configuration has this name.
# app = FastAPI()
#
#
# def write_watch_later_playlist():
#     yt = YoutubeTools()
#     info = yt.watch_later_fast()
#     return info
#
#
# @app.get("/")
# def read_root(background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_watch_later_playlist)
#     file_path = (YoutubeTools.path/"watchlater-21.json")
#
#     return file_path.read_json()['entries']
#
#
# def start():
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
#
#
# if __name__ == "__main__":
#     start()

# ℹ️ See help(yt_dlp.postprocessor.PostProcessor)
class YoutubeUtilPP(postprocessor.PostProcessor):
    def run(self, info):
        # self.to_screen('Doing stuff')

        info['foooo'] = 66
        print(info['title'])
        return [], info


def main():
    yt = Youtube("vivaldi")
    folder = Path(".cache")

    watch_later = yt.watch_later(YoutubeUtilPP())
    entries = watch_later.items()
    raw = folder / "watch-later.entries.json"
    raw.write_json(watch_later.raw_data())
    df = pd.DataFrame(entries)
    # df.to_csv('data.csv', index=False)
    conn = sqlite3.connect(folder / "watch_later.db")
    df.to_sql("watch_later_table", conn, if_exists="replace")
    df.to_csv(folder / "watch_later.csv")
    (folder / "watch-later.json").write_json(entries)
