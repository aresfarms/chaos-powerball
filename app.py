
import streamlit as st
import pandas as pd
import math

def calculate_odds(white_balls, powerball):
    total_combinations = math.comb(69, 5) * 26
    selected_combination = 1  # only one exact match
    odds = selected_combination / total_combinations
    return odds * 100  # return as percentage

st.title("🎯 Chaos Powerball Predictor with Odds Breakdown")

white_balls_input = st.text_input("Enter 5 white balls (1-69) separated by commas:", "")
powerball_input = st.number_input("Enter Powerball (1-26):", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    try:
        white_balls = [int(x.strip()) for x in white_balls_input.split(",")]
        if len(white_balls) != 5 or any(b < 1 or b > 69 for b in white_balls):
            st.error("Please enter exactly 5 valid white ball numbers between 1 and 69.")
        elif powerball_input < 1 or powerball_input > 26:
            st.error("Powerball must be between 1 and 26.")
        else:
            odds_percentage = calculate_odds(white_balls, powerball_input)
            st.success(f"Estimated Winning Chance: {odds_percentage:.12f}%")
    except ValueError:
        st.error("Invalid input. Please enter numbers only, separated by commas.")
