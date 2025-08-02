
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Chaos Powerball Predictor")

st.title("🎯 Chaos Powerball Predictor")
st.markdown("Get insights into your odds and explore number combinations with statistical backing.")

# --- Friendly Odds Table ---
st.subheader("📊 Friendly Odds Summary")
friendly_odds = {
    "Match Type": [
        "Powerball only",
        "1 white ball + Powerball",
        "2 white balls + Powerball",
        "3 white balls",
        "3 white balls + Powerball",
        "4 white balls",
        "4 white balls + Powerball",
        "5 white balls",
        "5 white balls + Powerball (Jackpot)"
    ],
    "Prize": [
        "$4", "$4", "$7", "$7", "$100", "$100", "$50,000", "$1 million", "Jackpot"
    ],
    "Odds (1 in X)": [
        26, 92, 701, 579, 14494, 36525, 913129, 11688053, 292201338
    ]
}
friendly_df = pd.DataFrame(friendly_odds)
friendly_df["Win %"] = (1 / friendly_df["Odds (1 in X)"] * 100).round(6)
st.dataframe(friendly_df)

# --- Ball Frequency Tables ---
st.subheader("⚪ White Ball Frequency")
white_freq = pd.read_csv("white_ball_frequency.csv")
st.dataframe(white_freq)

st.subheader("🔴 Powerball (Red Ball) Frequency")
red_freq = pd.read_csv("red_ball_frequency.csv")
st.dataframe(red_freq)

# --- Number Combination Calculator ---
st.subheader("🔢 Enter Your Powerball Combination")
white_balls = st.text_input("Enter 5 white ball numbers (1-69), comma-separated", "")
red_ball = st.number_input("Enter Powerball (1-26)", min_value=1, max_value=26, step=1)

if white_balls:
    try:
        white_list = sorted([int(x.strip()) for x in white_balls.split(",") if x.strip()])
        if len(white_list) != 5 or any(not (1 <= x <= 69) for x in white_list):
            st.error("Please enter exactly 5 white ball numbers between 1 and 69.")
        else:
            # Compute odds of jackpot match
            odds = 1 / 292201338
            percentage = odds * 100
            st.success(f"Your odds of winning the jackpot with this combination are:
"
                       f"1 in 292,201,338 ({percentage:.8f}%)
"
                       f"(That's approximately 0% chance)")
    except ValueError:
        st.error("Invalid input. Please enter only numbers separated by commas.")

# --- Draw History ---
st.subheader("📅 Historical Draws")
draw_data = pd.read_csv("draw_history.csv")
st.dataframe(draw_data.tail(10))
