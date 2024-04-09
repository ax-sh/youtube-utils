from .youtube import Youtube, Path

import pandas as pd


def process_entries(entry):
    
        # {
    #     "_type": "url",
    #     "ie_key": "Youtube",
    #     "id": "2wlXszWz_Uc",
    #     "url": "https://www.youtube.com/watch?v=2wlXszWz_Uc",
    #     "title": "Supabase + ElectricSQL",
    #     "description": null,
    #     "duration": 587,
    #     "channel_id": "UCNTVzV1InxHV-YR0fSajqPQ",
    #     "channel": "Supabase",
    #     "channel_url": "https://www.youtube.com/channel/UCNTVzV1InxHV-YR0fSajqPQ",
    #     "uploader": "Supabase",
    #     "uploader_id": "@Supabase",
    #     "uploader_url": "https://www.youtube.com/@Supabase",
    #     "thumbnails": "",
    #     "timestamp": 1704758400,
    #     "release_timestamp": null,
    #     "availability": null,
    #     "view_count": 1800,
    #     "live_status": null,
    #     "channel_is_verified": null,
    #     "__x_forwarded_for_ip": null
    # },
    entry['thumbnails'] = ''
    return { 
            "id": entry['id'],
            "url": entry['url'],
            "upload_date": entry['timestamp'],
            "view_count": entry['view_count'],
            "title": entry['title'],
            "channel": entry['channel'],
            "duration": entry['duration'],
            }  # noqa: F821

def main():
    yt = Youtube('vivaldi')
    watch_later = yt.watch_later()
    entries = list(map(process_entries,watch_later['entries']))
    Path('watch-later.entries.json').write_json(watch_later)
    df = pd.DataFrame(entries)
    df.to_csv('data.csv', index=False)
    Path('watch-later.json').write_json(entries)
