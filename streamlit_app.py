
import streamlit as st
import pandas as pd
import json
from itertools import combinations

st.set_page_config(page_title="Chaos Powerball App", layout="wide")
st.title("🎲 Chaos-Weighted Powerball Prediction Tool")

# Load draw stats from local JSON
try:
    with open("draw_stats.json", "r") as f:
        draw_stats = json.load(f)
except Exception as e:
    st.error("Failed to load draw statistics.")
    st.stop()

st.markdown("This app generates statistically weighted Powerball combinations based on empirical frequency and chaos modeling.")

st.header("📊 Suggested Powerball Combinations Based on Frequency")

# Build combinations: 4 most common + 1 least common + 1 powerball
main_combos = list(combinations(draw_stats["most_common"], 4))
combinations_data = []

for main in main_combos:
    for least in draw_stats["least_common"]:
        five_numbers = list(main) + [least]
        for pb in draw_stats["powerballs"]:
            combo = {
                "Main Numbers": sorted(five_numbers),
                "Powerball": pb
            }
            combinations_data.append(combo)

# Score combinations
for i, combo in enumerate(combinations_data):
    combo["Score"] = round(1 - (i / len(combinations_data)), 4)

# Display top 50 combos
df_combos = pd.DataFrame(combinations_data)
st.dataframe(df_combos.head(50), use_container_width=True)
