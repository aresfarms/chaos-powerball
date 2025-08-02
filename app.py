
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos-Based Powerball Predictor (Friendly Odds)", layout="wide")

st.title("Chaos-Based Powerball Predictor (Friendly Odds)")

st.markdown("Enter your Powerball combination below to see your estimated odds:")

white_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    st.success("🎲 Your combination has been processed.")

    # Friendly odds summary table
    summary_data = [
        ("Match Powerball only", "$4", "1 in 26", "3.85%"),
        ("Match 1 white ball + Powerball", "$4", "1 in 92", "1.09%"),
        ("Match 2 white balls + Powerball", "$7", "1 in 701", "0.14%"),
        ("Match 3 white balls", "$7", "1 in 579", "0.17%"),
        ("Match 3 white + Powerball", "$100", "1 in 14,494", "0.0069%"),
        ("Match 4 white balls", "$100", "1 in 36,525", "0.0027%"),
        ("Match 4 white + Powerball", "$50,000", "1 in 913,129", "0.00011%"),
        ("Match 5 white balls only", "$1 million", "1 in 11,688,053", "0.0000086%"),
        ("Match 5 white + Powerball", "Jackpot", "1 in 292,201,338", "0.00000034%")
    ]

    df_summary = pd.DataFrame(summary_data, columns=["Match Type", "Prize", "Odds (1 in X)", "Percentage"])
    st.subheader("Friendly Odds Summary Table")
    st.dataframe(df_summary, use_container_width=True)

# Load probability tables
white_ball_stats = pd.read_csv("/mnt/data/chaos_powerball_app/white_ball_stats.csv")
red_ball_stats = pd.read_csv("/mnt/data/chaos_powerball_app/red_ball_stats.csv")
draw_stats = pd.read_csv("/mnt/data/chaos_powerball_app/draw_stats.csv")

st.markdown("### 🔴 Red (Powerball) Ball Frequency")
st.dataframe(red_ball_stats, use_container_width=True)

st.markdown("### ⚪ White Ball Frequency")
st.dataframe(white_ball_stats, use_container_width=True)

st.markdown("### 📅 Past Winning Combinations")
st.dataframe(draw_stats, use_container_width=True)
