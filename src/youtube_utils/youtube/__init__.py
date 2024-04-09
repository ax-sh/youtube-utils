from yt_dlp import YoutubeDL
from .utils import Path

def progress_hook( response ):
    ##  send  response['status']  to whatever subprocess you have going on.
    print( response['status'],"77777777" )

class Youtube:
    WATCH_LATER_URL = 'https://www.youtube.com/playlist?list=WL'
    path = Path(__file__).parent
    def __init__(self, browser: str):
        self.browser = browser
        self.cookies_from_browser = (browser, )
    
    def __repr__(self):
        return self.browser
    
    def yt_dlp(self, updated_options):
        
        options = { 'cookiesfrombrowser': self.cookies_from_browser,}
        options.update(updated_options)
        print(options)
        return YoutubeDL(options)
    
    def watch_later(self):
        yt = self.yt_dlp({
            "extract_flat": True,
            'allow_unplayable_formats':True,
            "ignoreerrors": True,
            'progress_hooks': [progress_hook],
            "no_warnings":True,
            "clean_infojson":True,
            "extractor_args":"youtubetab:approximate_date",
            "print":"ID: %(id)s %(title)s %(upload_date)s   %(view_count)s"
        })
        info = yt.extract_info(self.WATCH_LATER_URL, download=False)
        return info