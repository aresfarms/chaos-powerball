import streamlit as st

st.title("🎯 Chaos Powerball Predictor")

# User inputs
white_balls = st.multiselect("Choose 5 white balls (1–69):", list(range(1, 70)))
powerball = st.number_input("Choose 1 Powerball (1–26):", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    if len(white_balls) != 5:
        st.error("Please select exactly 5 white balls.")
    else:
        st.success("Your numbers have been recorded.")
        st.markdown("### 🧮 Estimated Winning Odds")
        st.markdown("**Jackpot Odds:** 1 in 292,201,338")
        st.markdown("**Any Prize Odds:** 1 in 24.9")
        st.info("These estimates are based on historical Powerball data.")

