
import streamlit as st
import pandas as pd
import math

# Suggested combinations (example set)
suggested_combos = [
    ([5, 28, 62, 64, 65], 18),
    ([5, 28, 62, 64, 65], 13),
    ([5, 28, 62, 64, 65], 11),
    ([5, 28, 62, 64, 65], 4),
    ([5, 28, 62, 64, 66], 24),
    ([5, 28, 62, 65, 66], 18),
    ([5, 28, 62, 65, 66], 13),
    ([5, 28, 62, 65, 66], 11),
    ([5, 28, 62, 65, 66], 4),
    ([5, 28, 60, 62, 70], 24),
]

# Calculate odds
def calculate_odds(main_nums, powerball):
    total_combinations = math.comb(69, 5) * 26
    return 1 / total_combinations

# Page Title
st.title("📊 Top Frequency-Based Suggested Combos")

# Show the table
combo_data = []
for combo, pb in suggested_combos:
    prob = calculate_odds(combo, pb)
    combo_data.append({
        "Main Numbers": combo,
        "Powerball": pb,
        "Est. Chance (%)": round(prob * 100, 12)
    })

st.dataframe(pd.DataFrame(combo_data))

# User-defined combination
st.header("🎯 Test Your Own Combination")
user_main = st.text_input("Enter 5 main numbers separated by commas (1–69):")
user_power = st.text_input("Enter Powerball number (1–26):")

if st.button("Calculate Winning Chance"):
    try:
        main_numbers = [int(x.strip()) for x in user_main.split(",")]
        power_number = int(user_power.strip())
        if len(main_numbers) == 5 and all(1 <= n <= 69 for n in main_numbers) and (1 <= power_number <= 26):
            odds = calculate_odds(main_numbers, power_number)
            st.success(f"Estimated Winning Chance: {round(odds * 100, 12)}%")
        else:
            st.error("Please enter valid numbers within the correct range.")
    except:
        st.error("Invalid input format.")
