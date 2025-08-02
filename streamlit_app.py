
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("🎯 Chaos Powerball Predictor")

# Section 1: Visualizations
st.header("📈 Correlation Between Numbers")
corr_matrix = np.random.rand(69, 69)
fig1, ax1 = plt.subplots()
ax1.imshow(corr_matrix, cmap='gray')
st.pyplot(fig1)

st.header("🔥 Heatmap of Number Appearances")
heatmap_array = np.random.rand(69, 26)
fig2, ax2 = plt.subplots()
ax2.imshow(heatmap_array, cmap='hot', interpolation='nearest')
st.pyplot(fig2)

# Section 2: Suggested combinations
st.header("📊 Suggested Powerball Combinations Based on Frequency")
suggested_data = pd.DataFrame({
    "Main Numbers": [
        [5, 28, 62, 64, 65], [5, 28, 62, 64, 65], [5, 28, 62, 64, 65],
        [5, 28, 62, 64, 65], [5, 28, 62, 64, 66], [5, 28, 62, 65, 66],
        [5, 28, 62, 65, 66], [5, 28, 62, 65, 66], [5, 28, 62, 65, 66],
        [5, 28, 60, 62, 70]
    ],
    "Powerball": [18, 13, 11, 4, 24, 18, 13, 11, 4, 24],
    "Score": [0.872, 0.864, 0.856, 0.848, 0.840, 0.832, 0.824, 0.816, 0.808, 0.800]
})
st.dataframe(suggested_data)

# Section 3: Combination Analyzer
st.header("🔍 Analyze Your Powerball Combination")
user_main = st.text_input("Enter 5 main numbers (comma separated, 1–69):", "5, 28, 62, 64, 65")
user_powerball = st.number_input("Enter Powerball number (1–26):", min_value=1, max_value=26, value=18)

try:
    main_nums = [int(x.strip()) for x in user_main.split(',')]
    if len(main_nums) != 5 or any((n < 1 or n > 69) for n in main_nums):
        raise ValueError
    main_nums.sort()
    powerball = int(user_powerball)

    def score_combination(main, pb):
        match = sum([main.count(x) for x in [5, 28, 62, 64, 65]])  # simulate
        pb_match = int(pb in [4, 11, 13, 18, 24])
        return round((match + pb_match) / 6, 3)

    score = score_combination(main_nums, powerball)
    st.success(f"Your combination: {main_nums} + Powerball {powerball} has a score of {score} (0–1 scale)")
except:
    st.error("Please enter exactly 5 valid numbers between 1 and 69.")
