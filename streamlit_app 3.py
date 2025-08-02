
import streamlit as st

PRIZE_TIERS = {
    (5, True): ("Jackpot", 292201338),
    (5, False): ("$1 million", 11688053),
    (4, True): ("$50,000", 913129),
    (4, False): ("$100", 36525),
    (3, True): ("$100", 14494),
    (3, False): ("$7", 579),
    (2, True): ("$7", 701),
    (1, True): ("$4", 92),
    (0, True): ("$4", 26)
}

def calculate_friendly_odds(user_white, user_red, winning_white, winning_red):
    white_matches = len(set(user_white) & set(winning_white))
    red_match = (user_red == winning_red)

    tier = PRIZE_TIERS.get((white_matches, red_match))
    if tier:
        prize, odds = tier
        percentage = round(100 / odds, 6)
        return f"Match {white_matches} white{' + Powerball' if red_match else ''} ({prize}): 1 in {odds} chance ({percentage}%)"
    else:
        return "This combination does not match any winning tier. Odds of winning: Zero (0%)"

st.title("Chaos-Based Powerball Predictor (Friendly Odds)")

st.markdown("""
### Powerball Odds and Prize Table (Friendly Format)

| Match Type                       | Prize         | Odds (1 in X)   | Percentage     |
|----------------------------------|---------------|-----------------|----------------|
| Match Powerball only            | $4            | 1 in 26         | 3.85%          |
| Match 1 white ball + Powerball  | $4            | 1 in 92         | 1.09%          |
| Match 2 white balls + Powerball | $7            | 1 in 701        | 0.14%          |
| Match 3 white balls             | $7            | 1 in 579        | 0.17%          |
| Match 3 white + Powerball       | $100          | 1 in 14,494     | 0.0069%        |
| Match 4 white balls             | $100          | 1 in 36,525     | 0.0027%        |
| Match 4 white + Powerball       | $50,000       | 1 in 913,129    | 0.00011%       |
| Match 5 white balls only        | $1 million    | 1 in 11,688,053 | 0.0000086%     |
| Match 5 white + Powerball       | Jackpot       | 1 in 292,201,338| 0.00000034%    |
""")

white_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
red_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    try:
        white_numbers = [int(num.strip()) for num in white_input.split(",")]
        if len(white_numbers) != 5 or any(not (1 <= num <= 69) for num in white_numbers):
            st.error("Please enter exactly 5 white balls (1–69).")
        else:
            # Example reference draw
            winning_white = [12, 18, 24, 33, 52]
            winning_red = 18
            result = calculate_friendly_odds(white_numbers, red_input, winning_white, winning_red)
            st.success(result)
    except ValueError:
        st.error("Invalid input format. Enter numbers only.")
