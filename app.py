
import streamlit as st

def get_friendly_odds(combination):
    # Simulate checking a Powerball combination and returning human-readable odds
    odds_dict = {
        "Powerball only": (1/26, "$4"),
        "1 white + Powerball": (1/92, "$4"),
        "2 white + Powerball": (1/701, "$7"),
        "3 white": (1/579, "$7"),
        "3 white + Powerball": (1/14494, "$100"),
        "4 white": (1/36525, "$100"),
        "4 white + Powerball": (1/913129, "$50,000"),
        "5 white": (1/11688053, "$1 million"),
        "5 white + Powerball": (1/292201338, "Jackpot"),
    }

    results = []
    for key, (odds, prize) in odds_dict.items():
        percent = round(odds * 100, 8)
        one_in_x = round(1 / odds)
        results.append(f"{key} ({prize}): 1 in {one_in_x} chance ({percent}%)")
    return results

st.title("Powerball Odds Calculator")
st.markdown("### Here's a friendly, percentage-based summary of your Powerball odds and payouts:")

odds_list = get_friendly_odds(None)
for line in odds_list:
    st.write("•", line)
