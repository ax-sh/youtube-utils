from yt_dlp import YoutubeDL
from pathlib import Path

class Youtube:
    path = Path(__file__).parent
    def __init__(self, browser: str):
        self.browser = browser
        self.cookies_from_browser = (browser, )
    
    def __repr__(self):
        return self.browser
    
    def yt_dlp(self):
        return YoutubeDL({ 'cookiesfrombrowser': self.cookies_from_browser,})