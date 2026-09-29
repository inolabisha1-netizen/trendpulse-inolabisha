
import pandas as pd
import matplotlib.pyplot as plt

input_file = "/content/drive/MyDrive/TrendPulse/trendpulse_final_results.csv"

df = pd.read_csv(input_file)

df = df.sort_values(
    "listeners",
    ascending=False
)

# -------------------------
# Bar chart - Top 15
# -------------------------

top_15 = df.head(15)

plt.figure(figsize=(12, 7))

plt.barh(
    top_15["track"],
    top_15["listeners"]
)

plt.xlabel("Current Last.fm Listeners")
plt.ylabel("Song")

plt.title(
    "Top 15 Older Songs by Current Last.fm Listeners"
)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()


# -------------------------
# Scatter plot - Top 10
# -------------------------

top_10 = df.head(10)

plt.figure(figsize=(10, 6))

plt.scatter(
    top_10["release_year"],
    top_10["listeners"],
    s=100
)

for _, row in top_10.iterrows():

    plt.annotate(
        row["track"],
        (row["release_year"], row["listeners"]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Release Year")
plt.ylabel("Current Last.fm Listeners")

plt.title(
    "Top 10 Older Songs: Release Year vs Current Listeners"
)

plt.tight_layout()

plt.show()
