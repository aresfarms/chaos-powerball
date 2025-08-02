
import streamlit as st

st.title("Chaos-Weighted Powerball Predictor")

st.markdown("### Enter your Powerball combination below:")

white_balls = st.text_input("Enter 5 white balls (1-69) separated by commas")
powerball = st.text_input("Enter Powerball (1-26)")

if st.button("Calculate Odds"):
    if white_balls and powerball:
        try:
            white_numbers = list(map(int, white_balls.split(",")))
            powerball_number = int(powerball)
            if len(white_numbers) != 5 or not all(1 <= n <= 69 for n in white_numbers) or not (1 <= powerball_number <= 26):
                st.error("Invalid numbers. Please ensure white balls are 1–69 and Powerball is 1–26.")
            else:
                st.success("Your odds of winning the jackpot with this combination are: Zero (0%)")
        except ValueError:
            st.error("Please enter only numbers separated by commas.")
    else:
        st.info("Please enter all 6 numbers before calculating.")
