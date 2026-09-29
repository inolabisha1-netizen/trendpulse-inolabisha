
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv("/content/.env")

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")

url = "https://ws.audioscrobbler.com/2.0/"

params = {
    "method": "geo.getTopTracks",
    "country": "India",
    "api_key": LASTFM_API_KEY,
    "format": "json",
    "limit": 200
}

response = requests.get(url, params=params)

data = response.json()

tracks = data["tracks"]["track"]

rows = []

for track in tracks:

    rows.append({
        "rank": track.get("@attr", {}).get("rank"),
        "track": track.get("name"),
        "artist": track.get("artist", {}).get("name"),
        "playcount": track.get("playcount"),
        "listeners": track.get("listeners"),
        "mbid": track.get("mbid")
    })

lastfm_df = pd.DataFrame(rows)

lastfm_df.to_csv(
    "/content/drive/MyDrive/TrendPulse/lastfm_india_top_tracks.csv",
    index=False
)

print("Tracks collected:", len(lastfm_df))
print("Saved successfully.")
