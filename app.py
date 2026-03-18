import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 15,
    "Normal": 10,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    #BUG: Attempts were off by one because the attempt count was being updated after the display logic, causing the displayed attempts left to be inaccurate.
    #FIX: Initialize attempts to 0 here, and then update it after the submit button is clicked, to ensure the attempt count is accurate.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

#BUG: Show hint button was not working because it was inside the submit block, so it disappears after every rerun().
#
if "hint" not in st.session_state:
    st.session_state.hint = None

st.subheader("Make a guess")
# BUG: Attempts display does not match up with the actual number of attempts left, due to the attempt count being updated after the display logic.
# FIX: Store the hint in sessioon state and display it based on checkbox value outside submit block.
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if show_hint and st.session_state.hint:
    st.warning(st.session_state.hint)

if new_game:
    # BUG: The "New Game" button doesn't reset the game state properly, allowing players to carry over their score and attempts. This can be exploited to win easily.
    # FIX: Reset all relevant session state variables to their initial values when starting a new game
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.history = []
    st.session_state.status = "playing"
    st.session_state.hint = None
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # BUG: The secret is sometimes treated as a string, sometimes as an int. This causes the hints to be inconsistent.
        # if st.session_state.attempts % 2 == 0:
        #     secret = str(st.session_state.secret)
        # else:
        #     secret = st.session_state.secret
        # FIX: Always treat the secret as an int to avoid the glitch.
        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        st.session_state.hint = message

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )
    #BUG: Had to press submit twice to see the updated attempts left and score, because the state updates were happening after the display logic.
    #FIX: Ran st.rerun() after updating the session state to ensure the display logic runs with the updated state immediately after a guess is submitted.
    st.rerun()

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
