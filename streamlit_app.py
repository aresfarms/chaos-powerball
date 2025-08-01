
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

heatmap_array = np.load("heatmap_array.npy")
corr_array = np.load("corr_array.npy")

st.title("🎲 Chaos Powerball Explorer")

st.header("📈 Correlation Between Numbers")
fig_corr, ax_corr = plt.subplots()
ax_corr.imshow(corr_array, cmap="gray", interpolation="nearest")
st.pyplot(fig_corr)

st.header("🔥 Heatmap of Number Appearances")
fig_heat, ax_heat = plt.subplots()
ax_heat.imshow(heatmap_array, cmap="hot", interpolation="nearest")
st.pyplot(fig_heat)
