import pytest
from src.knights_tour import KnightsTour

def test_knights_tour_initialization():
    """Test KnightsTour class initialization."""
    kt = KnightsTour()
    assert kt.board_size == 8
    assert len(kt.moves) == 8

def test_is_valid_move():
    """Test the is_valid_move method."""
    kt = KnightsTour()
    
    # Valid moves
    assert kt.is_valid_move(0, 0) == True
    assert kt.is_valid_move(7, 7) == True
    assert kt.is_valid_move(3, 4) == True
    
    # Invalid moves
    assert kt.is_valid_move(-1, 0) == False
    assert kt.is_valid_move(0, 8) == False
    assert kt.is_valid_move(8, 8) == False

def test_knights_tour_solution():
    """Test finding a Knight's Tour solution."""
    kt = KnightsTour()
    
    # Test solution from different starting positions
    test_cases = [
        (0, 0),   # Top-left corner
        (7, 7),   # Bottom-right corner
        (3, 3),   # Middle of the board
        (2, 1)    # Another valid starting point
    ]
    
    for start_x, start_y in test_cases:
        tour = kt.solve(start_x, start_y)
        
        # Check tour exists
        assert tour is not None, f"No tour found for start ({start_x}, {start_y})"
        
        # Check tour length
        assert len(tour) == 64, f"Tour length incorrect for start ({start_x}, {start_y})"
        
        # Check all positions are unique
        assert len(set(tour)) == 64, f"Duplicate positions in tour for start ({start_x}, {start_y})"

def test_invalid_start_position():
    """Test handling of invalid starting positions."""
    kt = KnightsTour()
    
    # Test out-of-bounds starting positions
    with pytest.raises(ValueError, match="Invalid starting position"):
        kt.solve(-1, 0)
    
    with pytest.raises(ValueError, match="Invalid starting position"):
        kt.solve(8, 8)

def test_knight_move_validation():
    """Test that moves follow knight's move rules."""
    kt = KnightsTour()
    
    # Test a solution (using one of the valid starting points)
    tour = kt.solve(0, 0)
    assert tour is not None
    
    # Validate moves
    for i in range(len(tour) - 1):
        x1, y1 = tour[i]
        x2, y2 = tour[i+1]
        
        # Check move is a valid knight's move
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        assert (dx == 2 and dy == 1) or (dx == 1 and dy == 2), \
            f"Invalid knight's move from {tour[i]} to {tour[i+1]}"