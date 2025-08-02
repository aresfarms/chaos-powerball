
import streamlit as st
import pandas as pd

# Load frequency data
white_stats = pd.read_csv("white_ball_stats.csv")
red_stats = pd.read_csv("red_ball_stats.csv")

st.title("Chaos Powerball Predictor")

st.header("White Ball Frequencies (1–69)")
st.dataframe(white_stats)

st.header("Red Ball Frequencies (1–26)")
st.dataframe(red_stats)

st.header("Enter Your Powerball Numbers")

white_balls = []
for i in range(5):
    num = st.number_input(f"White Ball #{i+1}", min_value=1, max_value=69, step=1, key=f"white_{i}")
    white_balls.append(num)

red_ball = st.number_input("Powerball (Red Ball)", min_value=1, max_value=26, step=1, key="red")

if st.button("Calculate Winning Odds"):
    total_combinations = (69 * 68 * 67 * 66 * 65) / (5 * 4 * 3 * 2 * 1) * 26
    odds = 1 / total_combinations
    percent = odds * 100
    formatted = f"{percent:.12f}%"
    st.subheader("📊 Estimated Winning Chance")
    st.success(f"{formatted} chance of hitting the jackpot with this combination.")
