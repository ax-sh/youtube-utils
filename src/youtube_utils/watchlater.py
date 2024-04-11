class WatchLater:
    def __init__(self, data):
        self.data = data

    def raw_data(self):
        return self.data

    @staticmethod
    def process_entry(entry):
        # {
        #     "description": null,

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
            "channel_id": entry["channel_id"],
            "title": entry["title"],
            "duration": entry["duration"],
            "view_count": entry["view_count"],
            "thumbnail": thumb["url"],
        }

    def items(self):
        return list(map(self.process_entry, self.data["entries"]))
