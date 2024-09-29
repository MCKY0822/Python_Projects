import pytest
from simple_dice_game import roll

def test_roll_no_double_ones_or_sixes(): # Ensures that the function never returns [1, 1] or [6, 6].
    for _ in range(1000):
        result = roll()
        
        if result:
            assert result != [1, 1], "Roll result [1, 1], should be skipped"
            assert result != [6, 6], "Roll result [6, 6], should be skipped"