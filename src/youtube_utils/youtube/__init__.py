from yt_dlp import YoutubeDL
from .utils import Path


class Youtube:
    WATCH_LATER_URL = "https://www.youtube.com/playlist?list=WL"
    path = Path(__file__).parent

    def __init__(self, browser: str):
        self.browser = browser
        self.cookies_from_browser = (browser,)

    def __repr__(self):
        return self.browser

    def yt_dlp(self, updated_options):
        options = {
            "cookiesfrombrowser": self.cookies_from_browser,
        }
        options.update(updated_options)
        print(options)
        return YoutubeDL(options)

    # @see https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py
    def watch_later(self):
        yt = self.yt_dlp(
            {
                "extract_flat": "in_playlist",
                "dump_single_json": True,
                "allow_unplayable_formats": True,
                "ignoreerrors": True,
                "no_warnings": True,
                "clean_infojson": True,
                #    E.g. {'youtube': {'skip': ['dash', 'hls']}}
                "extractor_args": {"youtubetab": {"approximate_date": [""]}},
                "print": "ID: %(id)s %(title)s %(upload_date)s   %(view_count)s",
            }
        )
        info = yt.extract_info(self.WATCH_LATER_URL, download=False)
        return info
