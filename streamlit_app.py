
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos Powerball Predictor", layout="wide")

st.title("🎯 Chaos Powerball Predictor")

st.markdown("Enter your Powerball combination below to see your estimated odds:")

# User inputs
white_balls = st.text_input("Enter 5 white balls (1-69) separated by commas", "10,22,35,44,60")
powerball = st.number_input("Enter Powerball (1-26)", min_value=1, max_value=26, value=15)

try:
    white_list = [int(x.strip()) for x in white_balls.split(',')]
    if len(white_list) != 5 or any(not (1 <= num <= 69) for num in white_list):
        st.error("Please enter exactly 5 valid white ball numbers between 1 and 69.")
    else:
        odds_table = {
            "Match Powerball only ($4)": (26, 1, 3.85),
            "1 white + Powerball ($4)": (92, 1, 1.09),
            "2 white + Powerball ($7)": (701, 1, 0.14),
            "3 white only ($7)": (579, 1, 0.17),
            "3 white + Powerball ($100)": (14494, 1, 0.0069),
            "4 white only ($100)": (36525, 1, 0.0027),
            "4 white + Powerball ($50,000)": (913129, 1, 0.00011),
            "5 white only ($1M)": (11688053, 1, 0.0000086),
            "5 white + Powerball (Jackpot)": (292201338, 1, 0.00000034)
        }

        st.success("🎲 Your combination has been processed.")
        st.markdown("### Friendly Odds Summary Table")
        df = pd.DataFrame([
            {"Match Type": k, "1 in X Odds": f"1 in {v[0]:,}", "Chance (%)": f"{v[2]}%"}
            for k, v in odds_table.items()
        ])
        st.dataframe(df, use_container_width=True)

except ValueError:
    st.error("Invalid input. Make sure all white balls are numbers separated by commas.")

# Red Ball Probability Table
red_freq = {i: round(100/26, 2) for i in range(1, 27)}
red_df = pd.DataFrame(list(red_freq.items()), columns=["Red Ball", "Probability (%)"])

# White Ball Probability Table
white_freq = {i: round(100/69, 2) for i in range(1, 70)}
white_df = pd.DataFrame(list(white_freq.items()), columns=["White Ball", "Probability (%)"])

st.markdown("### 🔴 Red Ball Probability Table")
st.dataframe(red_df, use_container_width=True)

st.markdown("### ⚪ White Ball Probability Table")
st.dataframe(white_df, use_container_width=True)
