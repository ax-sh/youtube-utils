from .youtube import Youtube, Path

def main():
    yt = Youtube('vivaldi')
    Path('watch-later.json').write_json(yt.watch_later())
