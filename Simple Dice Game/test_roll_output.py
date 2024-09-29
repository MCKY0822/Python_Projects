import pytest
from simple_dice_game import roll


def test_roll_output_type(): # Test that the roll function returns a list.
    result = roll()
    assert isinstance(result, list), "Roll did not return a list"