import pytest
from src.color_stack_sorter import ColorStackSorter

def test_sorting_basic_scenario():
    """
    Test a basic scenario where balls need to be rearranged
    """
    sorter = ColorStackSorter(
        red_stack=['blue', 'green', 'red'],
        blue_stack=['red', 'blue', 'green'],
        green_stack=['green', 'red', 'blue']
    )
    
    moves = sorter.sort()
    
    # Verify final state
    assert sorter.stacks['red'] == ['red', 'red', 'red']
    assert sorter.stacks['blue'] == ['blue', 'blue', 'blue']
    assert sorter.stacks['green'] == ['green', 'green', 'green']

def test_already_sorted_scenario():
    """
    Test scenario where stacks are already sorted
    """
    sorter = ColorStackSorter(
        red_stack=['red', 'red', 'red'],
        blue_stack=['blue', 'blue', 'blue'],
        green_stack=['green', 'green', 'green']
    )
    
    moves = sorter.sort()
    
    # No moves should be made
    assert len(moves) == 0
    
    # Verify state remains the same
    assert sorter.stacks['red'] == ['red', 'red', 'red']
    assert sorter.stacks['blue'] == ['blue', 'blue', 'blue']
    assert sorter.stacks['green'] == ['green', 'green', 'green']

def test_unequal_stack_lengths():
    """
    Test that an error is raised when stack lengths are unequal
    """
    with pytest.raises(ValueError, match="All stacks must have equal number of balls"):
        ColorStackSorter(
            red_stack=['red', 'red'],
            blue_stack=['blue', 'blue', 'blue'],
            green_stack=['green', 'green']
        )

def test_invalid_ball_color():
    """
    Test that an error is raised when an invalid ball color is present
    """
    with pytest.raises(ValueError, match="Invalid ball color"):
        ColorStackSorter(
            red_stack=['red', 'yellow', 'red'],
            blue_stack=['blue', 'blue', 'blue'],
            green_stack=['green', 'green', 'green']
        )

def test_sorting_complexity():
    """
    Test a more complex sorting scenario
    """
    sorter = ColorStackSorter(
        red_stack=['blue', 'green', 'blue'],
        blue_stack=['red', 'blue', 'green'],
        green_stack=['green', 'red', 'red']
    )
    
    moves = sorter.sort()
    
    # Verify final state
    assert sorter.stacks['red'] == ['red', 'red', 'red']
    assert sorter.stacks['blue'] == ['blue', 'blue', 'blue']
    assert sorter.stacks['green'] == ['green', 'green', 'green']
    
    # Verify moves were made
    assert len(moves) > 0