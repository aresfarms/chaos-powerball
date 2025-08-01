
import streamlit as st
import random
import numpy as np
from collections import Counter
import datetime

# Load precomputed probabilities (insert your actual values here)
white_probs = {1: 0.014460, 2: 0.014785, 3: 0.014947, 4: 0.013810, 5: 0.012998, 6: 0.015110, 7: 0.013485, 8: 0.013160, 9: 0.013810, 10: 0.013485, 11: 0.014135, 12: 0.015760, 13: 0.010723, 14: 0.012673, 15: 0.013810, 16: 0.015110, 17: 0.014135, 18: 0.013972, 19: 0.014785, 20: 0.015110, 21: 0.018197, 22: 0.013323, 23: 0.017547, 24: 0.014135, 25: 0.012998, 26: 0.011698, 27: 0.016734, 28: 0.016084, 29: 0.012835, 30: 0.014297, 31: 0.013972, 32: 0.016897, 33: 0.017384, 34: 0.012185, 35: 0.013647, 36: 0.016734, 37: 0.016247, 38: 0.013810, 39: 0.016409, 40: 0.014460, 41: 0.013160, 42: 0.013485, 43: 0.014135, 44: 0.015760, 45: 0.015110, 46: 0.012023, 47: 0.015922, 48: 0.012835, 49: 0.011373, 50: 0.014297, 51: 0.012510, 52: 0.015272, 53: 0.015597, 54: 0.014297, 55: 0.014622, 56: 0.014947, 57: 0.015760, 58: 0.013810, 59: 0.016084, 60: 0.014622, 61: 0.018197, 62: 0.016409, 63: 0.016734, 64: 0.016572, 65: 0.014947, 66: 0.014785, 67: 0.015435, 68: 0.014460, 69: 0.017222}
red_probs = {1: 0.038180, 2: 0.040617, 3: 0.041430, 4: 0.047929, 5: 0.043054, 6: 0.042242, 7: 0.039805, 8: 0.035743, 9: 0.037368, 10: 0.038993, 11: 0.040617, 12: 0.043867, 13: 0.036556, 14: 0.043867, 15: 0.030869, 16: 0.030057, 17: 0.041430, 18: 0.045491, 19: 0.042242, 20: 0.038180, 21: 0.047116, 22: 0.040617, 23: 0.037368, 24: 0.047116, 25: 0.044679, 26: 0.038180}

# Placeholder loading function
def load_heatmap_and_correlation():
    st.warning("This is a placeholder. Replace with actual heatmap_array and corr_array loading logic.")
    heatmap_array = np.ones((69, 5)) / 69  # flat dummy weights
    corr_array = np.ones((69, 69)) / 69    # flat dummy weights
    return heatmap_array, corr_array

def chaos_weighted_draw_fast(corr_array, heatmap_array, noise_level=0.05):
    selected = []
    available = set(range(69))
    for pos in range(5):
        scores = []
        for i in available:
            base = white_probs[i + 1]
            position_weight = heatmap_array[i, pos]
            if selected:
                corr_weight = np.mean([corr_array[i, j] for j in selected])
            else:
                corr_weight = 1.0
            chaos = np.random.normal(1.0, noise_level)
            score = base * position_weight * corr_weight * chaos
            scores.append((score, i))
        scores.sort(reverse=True)
        best = scores[0][1]
        selected.append(best)
        available.remove(best)
    white_draw = sorted([i + 1 for i in selected])
    red_draw = random.choices(range(1, 27), weights=[red_probs[i] for i in range(1, 27)])[0]
    return white_draw, red_draw

def top_chaos_picks(n_sets, samples, corr_array, heatmap_array):
    scored_draws = []
    for _ in range(samples):
        draw = chaos_weighted_draw_fast(corr_array, heatmap_array)
        scored_draws.append(draw)
    counter = Counter(scored_draws)
    return counter.most_common(n_sets)

# Streamlit UI
st.title("Chaos-Based Powerball Predictor")
st.markdown("Generate optimized Powerball numbers using historical bias + chaos theory.")

heatmap_array, corr_array = load_heatmap_and_correlation()

if st.button("Generate Top 10 Picks"):
    picks = top_chaos_picks(10, 5000, corr_array, heatmap_array)
    for i, ((white, red), freq) in enumerate(picks, 1):
        st.markdown(f"**#{i}** 🎱 White Balls: `{white}`, 🔴 Red Ball: `{red}`, 🔁 Frequency: `{freq}`")

st.caption(f"Last run: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
