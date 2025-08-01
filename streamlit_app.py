
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Load the arrays
heatmap_array = np.load('heatmap_array.npy')
corr_array = np.load('corr_array.npy')

# Display Heatmap
st.subheader("Draw Frequency Heatmap")
st.pyplot(plt.imshow(heatmap_array, cmap='hot', interpolation='nearest'))
plt.clf()

# Display Correlation
st.subheader("Ball Correlation Matrix")
st.pyplot(plt.imshow(corr_array, cmap='coolwarm', interpolation='nearest'))
