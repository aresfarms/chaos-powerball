
import streamlit as st

st.title("Powerball Odds Checker")

def friendly_odds(match_tuple):
    odds_table = {
        (0, 1): ("Match Powerball only ($4)", "1 in 26", "3.85%"),
        (1, 1): ("Match 1 white ball + Powerball ($4)", "1 in 92", "1.09%"),
        (2, 1): ("Match 2 white balls + Powerball ($7)", "1 in 701", "0.14%"),
        (3, 0): ("Match 3 white balls ($7)", "1 in 579", "0.17%"),
        (3, 1): ("Match 3 white balls + Powerball ($100)", "1 in 14,494", "0.0069%"),
        (4, 0): ("Match 4 white balls ($100)", "1 in 36,525", "0.0027%"),
        (4, 1): ("Match 4 white balls + Powerball ($50,000)", "1 in 913,129", "0.00011%"),
        (5, 0): ("Match 5 white balls only ($1 million)", "1 in 11,688,053", "0.0000086%"),
        (5, 1): ("Match 5 white balls + Powerball (Jackpot)", "1 in 292,201,338", "0.00000034%"),
    }
    return odds_table.get(match_tuple, None)

user_white = st.text_input("Enter 5 white balls (1-69) separated by commas")
user_pb = st.number_input("Enter Powerball (1-26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    try:
        white_nums = list(map(int, user_white.strip().split(",")))
        if len(white_nums) != 5:
            st.error("Please enter exactly 5 white ball numbers.")
        else:
            # Simulate winning numbers
            winning_white = [10, 20, 30, 40, 50]
            winning_pb = 15

            white_matches = len(set(white_nums) & set(winning_white))
            pb_match = int(user_pb == winning_pb)

            result = friendly_odds((white_matches, pb_match))
            if result:
                tier, odds_str, percent = result
                st.success(f"{tier}: {odds_str} chance ({percent})")
            else:
                st.warning("This combination does not match any winning tier. Odds of winning: Zero (0%)")
    except:
        st.error("Invalid input. Please enter numbers only, separated by commas.")
