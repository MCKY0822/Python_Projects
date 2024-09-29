import pytest
from simple_dice_game import roll


def test_roll_valid(): # Ensures the returned dice values (if any) are between 1 and 6.
    result = roll()

    if not result:
        assert result == [], "Roll should return an empty list when no valid result"

    else:
        first, second = result
        assert 1 <= first <= 6, f"First dice roll out of range: {first}"
        assert 1 <= second <= 6, f"Second dice roll out of range: {second}"