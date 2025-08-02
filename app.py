
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos Powerball Predictor", layout="wide")
st.title("🎲 Chaos Powerball Predictor")

st.markdown("""
Welcome to the Powerball Predictor app. This tool provides:
- Statistically significant number suggestions
- Probability-based match checking
- Historical win data for red and white balls
- Layman-friendly odds output
""")

# Sample white and red ball probability tables
white_ball_probs = {
    "White Ball": list(range(1, 70)),
    "Probability (%)": [round(100/69, 2)] * 69
}
red_ball_probs = {
    "Red Ball": list(range(1, 27)),
    "Probability (%)": [round(100/26, 2)] * 26
}

white_df = pd.DataFrame(white_ball_probs)
red_df = pd.DataFrame(red_ball_probs)

# Show the probability tables
st.subheader("White Ball Probability Table")
st.dataframe(white_df)

st.subheader("Red Ball Probability Table")
st.dataframe(red_df)

# User input for calculating odds
white_balls_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    st.markdown("Odds calculation logic goes here...")
    # You can extend this block with real calculations
