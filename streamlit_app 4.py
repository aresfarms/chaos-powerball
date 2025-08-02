
import streamlit as st
import numpy as np

st.title("🎯 Powerball Winning Probability Calculator")

# Section: User Number Input
st.header("🔢 Enter Your Powerball Combination")
main_numbers = st.multiselect("Select 5 main numbers (1–69):", list(range(1, 70)), max_selections=5)
powerball_number = st.selectbox("Select Powerball number (1–26):", list(range(1, 27)))

# Official odds
def calculate_odds(main, pb):
    if len(main) != 5:
        return None
    total_combinations = (np.math.comb(69, 5) * 26)
    return round(1 / total_combinations * 100, 12)  # return as a %

if st.button("Calculate Winning Chance"):
    if len(main_numbers) == 5:
        chance = calculate_odds(main_numbers, powerball_number)
        st.success(f"Your chance of winning the next jackpot with this combination is {chance}%")
    else:
        st.warning("Please select exactly 5 main numbers.")

# Top 10 high-frequency combos (mock data)
st.header("📋 Top Frequency-Based Suggested Combos")
import pandas as pd
data = {
    "Main Numbers": [[5, 28, 62, 64, 65], [8, 19, 27, 49, 53], [7, 14, 21, 28, 41], [1, 12, 18, 26, 35],
                     [2, 9, 17, 36, 47], [6, 13, 24, 39, 55], [4, 16, 22, 45, 67], [11, 23, 33, 38, 48],
                     [10, 29, 30, 44, 52], [3, 20, 25, 34, 59]],
    "Powerball": [18, 13, 11, 4, 24, 3, 12, 7, 5, 9],
    "Est. Chance (%)": [calculate_odds([5, 28, 62, 64, 65], 18)] * 10
}
df = pd.DataFrame(data)
st.dataframe(df)
