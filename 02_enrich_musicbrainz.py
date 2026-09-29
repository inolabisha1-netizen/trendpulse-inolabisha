
import time
import requests
import pandas as pd

input_file = "/content/drive/MyDrive/TrendPulse/lastfm_india_top_tracks.csv"

output_file = "/content/drive/MyDrive/TrendPulse/trendpulse_enriched.csv"

headers = {
    "User-Agent": "TrendPulse/1.0"
}


def get_release_date_from_mbid(mbid):

    if not mbid:
        return None

    url = f"https://musicbrainz.org/ws/2/recording/{mbid}"

    params = {
        "fmt": "json",
        "inc": "releases"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    if response.status_code != 200:
        return None

    data = response.json()

    dates = []

    for release in data.get("releases", []):

        date = release.get("date")

        if date:
            dates.append(date)

    if dates:
        return min(dates)

    return None


def get_release_date_by_search(track, artist):

    url = "https://musicbrainz.org/ws/2/recording"

    params = {
        "query": f'recording:"{track}" AND artist:"{artist}"',
        "fmt": "json",
        "limit": 10
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    if response.status_code != 200:
        return None

    recordings = response.json().get(
        "recordings",
        []
    )

    dates = []

    for recording in recordings:

        title = recording.get(
            "title",
            ""
        ).strip().lower()

        if title == str(track).strip().lower():

            date = recording.get(
                "first-release-date"
            )

            if date:
                dates.append(date)

    if dates:
        return min(dates)

    return None


def get_release_date(track, artist, mbid):

    date = get_release_date_from_mbid(mbid)

    if date:
        return date, "MBID"

    date = get_release_date_by_search(
        track,
        artist
    )

    if date:
        return date, "Search"

    return None, "Not found"


df = pd.read_csv(input_file)

release_dates = []
date_sources = []

for i, row in df.iterrows():

    date, source = get_release_date(
        row["track"],
        row["artist"],
        row["mbid"]
    )

    release_dates.append(date)
    date_sources.append(source)

    time.sleep(1.1)


df["release_date"] = release_dates

df["date_source"] = date_sources

df["release_year"] = pd.to_datetime(
    df["release_date"],
    errors="coerce"
).dt.year


df.to_csv(
    output_file,
    index=False
)

print("MusicBrainz enrichment complete.")
print("Release dates found:", df["release_date"].notna().sum())
