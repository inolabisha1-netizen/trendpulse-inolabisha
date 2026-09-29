# TrendPulse: Identifying Potentially Rediscovered Music Classics

TrendPulse is a data-driven project that identifies **older songs that are currently receiving significant attention among listeners in India**.

The project combines current music popularity data from **Last.fm** with original release-date information from **MusicBrainz** to identify older songs—both **Indian and international**—that appear among the current top tracks for India.

> **Note:** The project identifies **potentially rediscovered classics**. It does not claim that a song has definitively experienced a revival or rediscovery, since current listener activity alone cannot establish the reason for its popularity.

## Project Objective

The main objective of TrendPulse is to answer:

**"Which older Indian and international songs are currently prominent among Last.fm's top tracks for India and could potentially represent rediscovered classics?"**

The project:

1. Collects the current top 200 tracks for India from Last.fm.
2. Enriches the tracks with original release-date information using MusicBrainz.
3. Identifies songs released in or before 2016.
4. Ranks these older songs based on their current Last.fm listener counts.
5. Visualizes the results using bar and scatter plots.

## Data Sources

### Last.fm API

Used to collect current music popularity information for India, including:

* Track name
* Artist
* Rank
* Play count
* Listener count
* MusicBrainz ID (when available)

### MusicBrainz API

Used to obtain release-date information for the collected tracks.

## Project Workflow

```text
Last.fm API
     ↓
Collect Top 200 Tracks for India
     ↓
MusicBrainz API
     ↓
Add Release Dates
     ↓
Identify Older Songs
     ↓
Identify Potentially Rediscovered Classics
     ↓
Rank by Current Listeners
     ↓
Visualize Results
```

## Project Files

| File                         | Description                                                |
| ---------------------------- | ---------------------------------------------------------- |
| `01_collect_lastfm.py`       | Collects the current top 200 tracks for India from Last.fm |
| `02_enrich_musicbrainz.py`   | Adds release-date information using MusicBrainz            |
| `03_analyze_trendpulse.py`   | Identifies and ranks potentially rediscovered classics     |
| `04_visualize_trendpulse.py` | Creates charts for the identified older songs              |

## Definition of an Older Song

For this project, a song is classified as an **older song** if its release year is **2016 or earlier**.

This threshold can be modified in the analysis script if required.

## Latest Project Result

In the latest run:

* **200 tracks** were analyzed.
* **37 tracks** were classified as older songs.
* This represents **18.5%** of the analyzed tracks.
* MusicBrainz successfully provided release dates for **163 tracks**.

These 37 older songs are treated as **potentially rediscovered classics** based on their presence among the current Last.fm top tracks for India.

## Visualizations

The project generates two visualizations:

### 1. Top 15 Older Songs

A horizontal bar chart showing the 15 older songs with the highest current Last.fm listener counts.

### 2. Release Year vs Current Listeners

A scatter plot showing the relationship between:

* Release year
* Current Last.fm listener count

for the top 10 older songs.

These visualizations help explore which older songs currently have substantial listener activity.

## Important Data Interpretation

The `listeners` value comes from Last.fm and should be interpreted as a **Last.fm listener count**.

It should **not** be interpreted as the exact number of listeners located only in India.

Therefore, the project uses the India-specific Last.fm chart to identify tracks currently prominent in that chart, while the listener count is treated as the popularity metric provided by Last.fm.

The presence of an older song in the current chart does **not by itself prove why the song is popular or that it has been rediscovered**.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Requests
* Last.fm API
* MusicBrainz API
* Google Colab
* GitHub

## Future Improvements

Possible future improvements include:

* Tracking the same songs over multiple time periods
* Comparing historical and current popularity
* Adding more music platforms
* Measuring changes in popularity over time
* Building a dashboard for interactive exploration
* Developing a stronger definition of "rediscovery" using multiple signals

## Author

**Inol Abisha L**

TrendPulse is developed as a data/AI-ML portfolio project exploring music trends through APIs and data analysis.
