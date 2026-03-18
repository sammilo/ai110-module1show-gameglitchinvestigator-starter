from streamlit.testing.v1 import AppTest
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_new_game_resets_state():
    at = AppTest.from_file("app.py").run()

    # Simulate accumulated game state
    at.session_state.score = 75
    at.session_state.attempts = 7
    at.session_state.history = [10, 20, 30]

    # Click the "New Game" button (index 1: Submit=0, New Game=1)
    at.button[1].click().run()

    assert at.session_state.score == 0
    assert at.session_state.attempts == 0
    assert at.session_state.history == []
