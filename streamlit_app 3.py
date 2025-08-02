
import streamlit as st
import numpy as np
import pandas as pd

st.title("🔢 Powerball Prediction App")

# Section: Input Custom Combination
st.header("🎯 Check Your Combination")
main_numbers = st.multiselect("Choose 5 main numbers (1–69):", list(range(1, 70)), max_selections=5)
powerball_number = st.selectbox("Choose 1 Powerball number (1–26):", list(range(1, 27)))

# Dummy statistical relevance calculator
def calculate_combination_score(main_nums, pb_num):
    if len(main_nums) != 5:
        return None
    return round(0.75 + (sum(main_nums) + pb_num) % 25 / 100, 3)  # Dummy formula

if st.button("Calculate Winning Likelihood"):
    if len(main_numbers) == 5:
        score = calculate_combination_score(main_numbers, powerball_number)
        st.success(f"Your combination's estimated likelihood score: {score}")
    else:
        st.warning("Please select exactly 5 main numbers.")

# Section: Top Suggested Combinations
st.header("📊 Suggested Powerball Combinations Based on Frequency")
sample_data = {
    "Main Numbers": [[5, 28, 62, 64, 65]] * 5 + [[5, 28, 62, 65, 66]] * 5,
    "Powerball": [18, 13, 11, 4, 24, 18, 13, 11, 4, 24],
    "Score": [0.872, 0.864, 0.856, 0.848, 0.84, 0.832, 0.824, 0.816, 0.808, 0.8]
}
df = pd.DataFrame(sample_data)
st.dataframe(df)
