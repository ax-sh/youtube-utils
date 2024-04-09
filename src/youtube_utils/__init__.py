from yt_dlp import YoutubeDL
from .utils import Path


class WatchLater:
    def __init__(self, data):
        self.data = data

    def raw_data(self):
        return self.data

    @staticmethod
    def process_entry(entry):
        # {
        #     "description": null,

        #     "channel_id": "UCNTVzV1InxHV-YR0fSajqPQ",

        #     "uploader": "Supabase",
        #     "uploader_id": "@Supabase",
        #     "uploader_url": "https://www.youtube.com/@Supabase",

        #     "release_timestamp": null,
        #     "availability": null,

        #     "live_status": null,
        #     "channel_is_verified": null,
        #     "__x_forwarded_for_ip": null
        # },
        thumb = max(entry["thumbnails"], key=lambda x: x["height"] * x["width"])
        return {
            "id": entry["id"],
            "url": entry["url"],
            "upload_date": entry["timestamp"],
            "channel": entry["channel"],
            "channel_url": entry["channel_url"],
            "title": entry["title"],
            "duration": entry["duration"],
            "view_count": entry["view_count"],
            "thumbnail": thumb["url"],
        }

    def items(self):
        return list(map(self.process_entry, self.data["entries"]))


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
            info = yt.extract_info(self.WATCH_LATER_URL, download=False)
            return WatchLater(info)
