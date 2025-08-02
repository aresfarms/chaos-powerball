
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Chaos Powerball Predictor", layout="wide")
st.title("🎯 Chaos Powerball Predictor with Odds Breakdown")

# Load stats
white_stats = pd.read_csv("white_ball_stats.csv")
red_stats = pd.read_csv("red_ball_stats.csv")
draw_stats = pd.read_csv("draw_stats.csv")

# Display the stats table
st.subheader("White Ball Frequencies")
st.dataframe(white_stats)

st.subheader("Red Ball Frequencies")
st.dataframe(red_stats)

# User input
st.subheader("Try Your Own Number Combination")
white_balls = st.text_input("Enter 5 white balls (1-69) separated by commas", "10,20,30,40,50")
power_ball = st.number_input("Enter Powerball (1-26)", min_value=1, max_value=26, value=15)

def calculate_probability():
    total_combinations = (np.math.comb(69, 5)) * 26
    return round(1 / total_combinations * 100, 10)  # as percent

if st.button("Calculate Winning Odds"):
    try:
        white_list = [int(num.strip()) for num in white_balls.split(",")]
        if len(white_list) != 5 or not all(1 <= n <= 69 for n in white_list):
            st.error("Please enter exactly 5 valid white ball numbers between 1 and 69.")
        else:
            prob = calculate_probability()
            st.success(f"Your chance of winning the jackpot is approximately **{prob}%**")
    except:
        st.error("Invalid input format. Enter numbers only.")

