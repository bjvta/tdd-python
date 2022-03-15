"""
Test Numbers
"""


from lib.numbers import Numbers


def test_highest_number_one():
    expected = 3
    result = Numbers.highest_number(1, 2, 3)
    assert result == expected

