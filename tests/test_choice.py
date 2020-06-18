import psidialogs


def test_empty_choices():
    assert psidialogs.choice(choices=[]) is None
    assert psidialogs.multi_choice(choices=[]) is None

def test_one_choice():
    assert psidialogs.choice(choices=["1"]) == "1"
