import streamlit as st

st.title("🎯 Chaos Powerball Predictor with Odds Breakdown")

# User inputs
white_balls = st.multiselect("Choose 5 white balls (1–69):", list(range(1, 70)))
powerball = st.number_input("Choose 1 Powerball (1–26):", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    if len(white_balls) != 5:
        st.error("Please select exactly 5 white balls.")
    else:
        st.success("Your numbers have been recorded.")

        # Jackpot odds
        total_white_combinations = 11238513  # C(69,5)
        total_powerball_options = 26
        jackpot_odds = 1 / (total_white_combinations * total_powerball_options)
        jackpot_percentage = jackpot_odds * 100

        # Individual component odds
        white_odds = 1 / total_white_combinations
        red_odds = 1 / total_powerball_options

        # Display results
        st.markdown("### 🧮 Estimated Winning Odds")
        st.markdown(f"**Jackpot (All 5 white balls + Powerball):** 1 in {int(1/jackpot_odds):,} (~{jackpot_percentage:.10f}%)")
        st.markdown(f"**Matching 5 White Balls Only:** 1 in {total_white_combinations:,} (~{white_odds*100:.8f}%)")
        st.markdown(f"**Matching Powerball Only:** 1 in {total_powerball_options} (~{red_odds*100:.2f}%)")
        st.info("These estimates are based on combinatorial probability only.")

