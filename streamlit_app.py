import streamlit as st
import pandas as pd
from math import comb

st.set_page_config(page_title="Chaos-Based Powerball Predictor", layout="wide")

st.title("Chaos-Based Powerball Predictor")

# Load stats
white_ball_stats = pd.read_csv("white_ball_stats.csv")
red_ball_stats = pd.read_csv("red_ball_stats.csv")

st.subheader("White Ball Appearance Frequencies")
st.dataframe(white_ball_stats)

st.subheader("Powerball (Red Ball) Appearance Frequencies")
st.dataframe(red_ball_stats)

# User input
st.header("Try Your Own Number Combination")

white_balls_input = st.text_input("Enter 5 white balls (1-69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1-26)", min_value=1, max_value=26, step=1)

def calculate_odds(white_balls, powerball):
    total_combinations = comb(69, 5) * 26
    return 1 / total_combinations * 100  # return as percentage

if st.button("Calculate Winning Odds"):
    try:
        white_balls = [int(num.strip()) for num in white_balls_input.split(',') if num.strip().isdigit()]
        if len(white_balls) != 5 or not all(1 <= n <= 69 for n in white_balls):
            raise ValueError("Must enter exactly five white ball numbers between 1 and 69.")
        if not (1 <= powerball_input <= 26):
            raise ValueError("Powerball must be between 1 and 26.")
    except Exception as e:
        st.error(f"Invalid input format. {str(e)}")
    else:
        odds = calculate_odds(white_balls, int(powerball_input))
        st.success(f"Your odds of winning with this combination are: {odds:.10f}%")
