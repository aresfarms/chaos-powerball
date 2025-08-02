
import streamlit as st

def format_odds(numerator, denominator):
    percentage = (1 / denominator) * 100
    return f"1 in {denominator} ({percentage:.8f}%)"

def main():
    st.title("Powerball Odds Summary")

    st.markdown("""
    ### Here’s a friendly, percentage-based summary of your Powerball odds and payouts:
    - Match Powerball only ($4): **{}**
    - Match 1 white ball + Powerball ($4): **{}**
    - Match 2 white balls + Powerball ($7): **{}**
    - Match 3 white balls ($7): **{}**
    - Match 3 white balls + Powerball ($100): **{}**
    - Match 4 white balls ($100): **{}**
    - Match 4 white balls + Powerball ($50,000): **{}**
    - Match 5 white balls only ($1 million): **{}**
    - Match 5 white balls + Powerball (Jackpot): **{}**
    """.format(
        format_odds(1, 26),
        format_odds(1, 92),
        format_odds(1, 701),
        format_odds(1, 579),
        format_odds(1, 14494),
        format_odds(1, 36525),
        format_odds(1, 913129),
        format_odds(1, 11688053),
        format_odds(1, 292201338)
    ))

if __name__ == "__main__":
    main()
