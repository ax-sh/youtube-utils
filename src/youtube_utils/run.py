from .youtube import Youtube, Path
import sqlite3
import pandas as pd

def process_entries(entry):
    # {

    #     "id": "2wlXszWz_Uc",
  
    #     "description": null,
    #     "duration": 587,
    #     "channel_id": "UCNTVzV1InxHV-YR0fSajqPQ",
    
    #     "channel_url": "https://www.youtube.com/channel/UCNTVzV1InxHV-YR0fSajqPQ",
    #     "uploader": "Supabase",
    #     "uploader_id": "@Supabase",
    #     "uploader_url": "https://www.youtube.com/@Supabase",
  
    #     "release_timestamp": null,
    #     "availability": null,

    #     "live_status": null,
    #     "channel_is_verified": null,
    #     "__x_forwarded_for_ip": null
    # },
    thumb = max(entry['thumbnails'], key=lambda x:x['height']*x['width'])
    return { 
            "id": entry['id'],
            "url": entry['url'],
            "upload_date": entry['timestamp'],
            "channel": entry['channel'],
            "title": entry['title'],
            "duration": entry['duration'],
            "view_count": entry['view_count'],
            "thumbnail": thumb['url']
    }

def main():
    yt = Youtube('vivaldi')
    folder = Path('.cache')
    
    watch_later = yt.watch_later()
    entries = list(map(process_entries,watch_later['entries']))
    raw = folder / 'watch-later.entries.json'
    raw.write_json(watch_later)
    df = pd.DataFrame(entries)
    # df.to_csv('data.csv', index=False)
    conn = sqlite3.connect(folder / 'watch_later.db')
    df.to_sql( 'watch_later_table', conn, if_exists='replace')
    (folder / 'watch-later.json').write_json(entries)
