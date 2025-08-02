
import streamlit as st
from math import comb

st.title("Chaos-Weighted Powerball Odds Calculator")

st.markdown("### Enter Your Powerball Numbers")
white_balls = st.multiselect("Select 5 white balls (1–69):", options=list(range(1, 70)), max_selections=5)
red_ball = st.number_input("Select 1 red Powerball (1–26):", min_value=1, max_value=26, step=1)

def format_odds(odds):
    if odds == 0:
        return "0%"
    elif odds > 0.1:
        return f"{round(odds, 2)}%"
    elif odds > 0.01:
        return f"{round(odds, 3)}%"
    else:
        return f"{odds:.8f}%"

def get_prize_and_odds(w, r):
    prize_table = {
        (0,1): ("$4", 1/26),
        (1,1): ("$4", 1/92),
        (2,1): ("$7", 1/701),
        (3,0): ("$7", 1/579),
        (3,1): ("$100", 1/14494),
        (4,0): ("$100", 1/36525),
        (4,1): ("$50,000", 1/913129),
        (5,0): ("$1 million", 1/11688053),
        (5,1): ("JACKPOT", 1/292201338)
    }
    return prize_table.get((w, r), ("No prize", 0))

def simulate_combination(white_balls, red_ball):
    if len(white_balls) != 5:
        return None

    winning_combination = set([10, 20, 30, 40, 50])  # example pattern
    winning_red = 15

    white_matches = len(set(white_balls).intersection(winning_combination))
    red_match = 1 if red_ball == winning_red else 0

    prize, odds = get_prize_and_odds(white_matches, red_match)
    percent = round(odds * 100, 8)
    odds_ratio = f"1 in {int(1/odds):,}" if odds > 0 else "No chance"

    return prize, percent, odds_ratio

if st.button("Calculate Odds"):
    if len(white_balls) != 5:
        st.error("Please select exactly 5 white balls.")
    else:
        prize, percent, odds_ratio = simulate_combination(white_balls, red_ball)
        st.success(f"Your prize tier: {prize}")
        st.info(f"Your odds of winning with this combination are: **{percent}%** ({odds_ratio})")
