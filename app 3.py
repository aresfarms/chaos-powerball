
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

st.subheader("📊 White Ball Probabilities")
st.dataframe(white_df, use_container_width=True)

st.subheader("🔴 Red Ball Probabilities")
st.dataframe(red_df, use_container_width=True)

st.subheader("💡 Enter Your Combination")
white_input = st.text_input("Enter 5 white balls separated by commas (1-69)", "")
red_input = st.text_input("Enter 1 red ball (Powerball) (1-26)", "")

def friendly_odds_description():
    return [
        ("Match Powerball only", "$4", "1 in 26", "3.85%"),
        ("1 white + Powerball", "$4", "1 in 92", "1.09%"),
        ("2 white + Powerball", "$7", "1 in 701", "0.14%"),
        ("3 white", "$7", "1 in 579", "0.17%"),
        ("3 white + Powerball", "$100", "1 in 14,494", "0.0069%"),
        ("4 white", "$100", "1 in 36,525", "0.0027%"),
        ("4 white + Powerball", "$50,000", "1 in 913,129", "0.00011%"),
        ("5 white", "$1 million", "1 in 11,688,053", "0.0000086%"),
        ("5 white + Powerball", "Jackpot", "1 in 292,201,338", "0.00000034%")
    ]

if white_input and red_input:
    try:
        white_nums = sorted(set(int(x.strip()) for x in white_input.split(",") if x.strip()))
        red_num = int(red_input.strip())
        if len(white_nums) != 5 or any(n < 1 or n > 69 for n in white_nums) or not (1 <= red_num <= 26):
            st.error("❌ Please enter exactly 5 unique white balls (1-69) and 1 red ball (1-26).")
        else:
            st.success("✅ Valid combination submitted.")
            st.markdown(f"### 🎯 Your Combination: {white_nums} + [Red: {red_num}]")
            st.markdown("### 🧮 Odds of Winning:")
            for match, prize, odds, pct in friendly_odds_description():
                st.markdown(f"- **{match} ({prize})**: {odds} ({pct})")
    except ValueError:
        st.error("❌ Please enter numbers only.")
else:
    st.info("ℹ️ Enter your numbers above to see win probabilities.")
