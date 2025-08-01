
import streamlit as st
import json
import numpy as np

# Load draw stats from JSON
with open("draw_stats.json", "r") as f:
    draw_stats = json.load(f)

# Load arrays
heatmap_array = np.load("heatmap_array.npy")
corr_array = np.load("corr_array.npy")

st.title("🎲 Chaos-Based Powerball Predictor")
st.markdown("This tool uses empirical draw data, chaos theory, and inter-number correlation to help analyze trends in Powerball outcomes. For entertainment only.")

st.subheader("📊 Most Common Draw Stats")
st.write("Most Common White Balls:", draw_stats["most_common"])
st.write("Least Common White Balls:", draw_stats["least_common"])
st.write("Most Common Powerballs:", draw_stats["powerballs"])

st.subheader("🔥 Heatmap of Number Appearances")
st.image(heatmap_array, caption="Heatmap of White Ball Frequencies", use_column_width=True)

st.subheader("📈 Correlation Between Numbers")
st.image(corr_array, caption="Correlation Matrix of Drawn Numbers", use_column_width=True)
