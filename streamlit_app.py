
import streamlit as st
import numpy as np
import json
import os

st.set_page_config(page_title="Chaos Powerball Predictor", layout="centered")

st.title("🎲 Chaos-Based Powerball Predictor")
st.markdown("This tool uses empirical draw data, chaos theory, and inter-number correlation to help analyze trends in Powerball outcomes. For entertainment only.")

# Check and load model files
required_files = ["heatmap_array.npy", "corr_array.npy", "draw_stats.json"]
missing = [f for f in required_files if not os.path.exists(f)]
if missing:
    st.error(f"Missing required files: {', '.join(missing)}")
    st.stop()

# Load files
heatmap = np.load("heatmap_array.npy")
correlation = np.load("corr_array.npy")
with open("draw_stats.json", "r") as f:
    draw_stats = json.load(f)

# Display stats
st.subheader("📊 Most Common Draw Stats")
st.write("White Ball Frequency:", draw_stats["white_frequency"])
st.write("Powerball Frequency:", draw_stats["powerball_frequency"])
st.write("Most Common White Ball:", draw_stats["most_common_white"])
st.write("Most Common Powerball:", draw_stats["most_common_powerball"])
st.write("Average White Ball Value:", round(draw_stats["average_white"], 2))
st.write("Average Powerball Value:", round(draw_stats["average_powerball"], 2))

# Future features
st.subheader("🚧 In Progress")
st.markdown("- Chaos-weighted number simulation")
st.markdown("- Heatmap visualizations")
st.markdown("- Optimized ticket generator")
st.markdown("- Inter-number correlation matrix")

st.info("Note: All outputs are for entertainment only and do not increase your odds of winning.")

