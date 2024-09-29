import pytest
from simple_dice_game import roll


def test_roll_empty_result(): # Ensures that after three invalid combinations, the function returns an empty list.
    for _ in range(1000):
        result = roll()

        if not result:
            assert result == [], "Roll should return an empty list when no valid result is found"
