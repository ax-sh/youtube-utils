from yt_dlp import YoutubeDL
from .utils import Path

from .watchlater import WatchLater


class Youtube:
    WATCH_LATER_URL = "https://www.youtube.com/playlist?list=WL"
    path = Path(__file__).parent

    def __init__(self, browser: str):
        self.browser = browser
        self.cookies_from_browser = (browser,)

    def __repr__(self):
        return self.browser

    def yt_dlp(self, updated_options={}):
        options = {
            "cookiesfrombrowser": self.cookies_from_browser
        }
        options.update(updated_options)
        return YoutubeDL(options)
    
    def make_api_with_session(self):
        cookies = self.yt_dlp().cookiejar
        api = ''
        # api = youtube_unofficial.YouTube(cookiejar_cls=cookies, logged_in=True)
       
        return api

    # @see https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py
    def watch_later(self):
        with self.yt_dlp(
                {
                    "extract_flat": "in_playlist",
                    "dump_single_json": True,
                    "allow_unplayable_formats": True,
                    "ignoreerrors": True,
                    "no_warnings": True,
                    "clean_infojson": True,
                    #  E.g. {'youtube': {'skip': ['dash', 'hls']}}
                    "extractor_args": {"youtubetab": {"approximate_date": [""]}},
                }
        ) as yt:
            
            # api = self.make_api_with_session()
            # video_id = 'QQPz3eXXgQI'
            # api.login()
            # api.remove_video_id_from_playlist('WL', video_id)
            # exit()
            info = yt.extract_info(self.WATCH_LATER_URL, download=False)
            return WatchLater(info)
