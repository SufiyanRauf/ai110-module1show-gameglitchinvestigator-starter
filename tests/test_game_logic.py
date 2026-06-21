from app import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_says_go_lower():
    # Guess is above the secret -> player must go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_guess_too_low_says_go_higher():
    # Guess is below the secret -> player must go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_too_high_hint_direction_string_secret():
    # App stringifies the secret on even attempts, exercising the
    # except TypeError fallback in check_guess.
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_direction_string_secret():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
