from .youtube import Youtube, Path

def process_entries(entry):
    entry['thumbnails'] = ''
    return entry

def main():
    yt = Youtube('vivaldi')
    watch_later = yt.watch_later()
    entries = list(map(process_entries,watch_later['entries']))
    Path('watch-later.json').write_json(entries)
