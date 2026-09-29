
import pandas as pd

input_file = "/content/drive/MyDrive/TrendPulse/trendpulse_enriched.csv"

output_file = "/content/drive/MyDrive/TrendPulse/trendpulse_final_results.csv"

df = pd.read_csv(input_file)

df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
)

df["listeners"] = pd.to_numeric(
    df["listeners"],
    errors="coerce"
)

df["is_older"] = df["release_year"] <= 2016

older_tracks = df[
    df["is_older"] == True
].copy()

older_tracks["age_years"] = (
    2026 - older_tracks["release_year"]
)

older_tracks = older_tracks.sort_values(
    "listeners",
    ascending=False
)

percentage = len(older_tracks) / len(df) * 100

print("Tracks analyzed:", len(df))

print(
    "Potential rediscovered classics:",
    len(older_tracks)
)

print(
    "Percentage:",
    round(percentage, 1),
    "%"
)

older_tracks.to_csv(
    output_file,
    index=False
)

print("Analysis results saved successfully.")
