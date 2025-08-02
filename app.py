
import streamlit as st
import pandas as pd

st.title("Chaos Powerball Probability App")

st.markdown("### Enter your Powerball number combination:")

white_balls = [st.number_input(f"White Ball #{i+1}", min_value=1, max_value=69, step=1, key=f"wb_{i}") for i in range(5)]
red_ball = st.number_input("Red Powerball", min_value=1, max_value=26, step=1, key="rb")

if st.button("Calculate Odds"):
    white_odds = (1/69) ** 5
    red_odds = 1/26
    total_odds = white_odds * red_odds
    percent_chance = total_odds * 100
    st.markdown(f"#### Estimated Chance of Winning Jackpot:")
    st.markdown(f"**{percent_chance:.12f}%**")

st.markdown("---")
st.markdown("### Draw Statistics Table:")
try:
    df = pd.read_csv("draw_stats.csv")
    st.dataframe(df)
except FileNotFoundError:
    st.error("Draw statistics file not found.")
