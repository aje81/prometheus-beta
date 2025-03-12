import pytest
from src.list_rotation import rotate_list

def test_basic_rotation():
    """Test basic list rotation"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to list length"""
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_partial_rotation():
    """Test rotation less than list length"""
    assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]

def test_zero_rotation():
    """Test rotation of 0"""
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_empty_list():
    """Test rotation of empty list"""
    assert rotate_list([], 5) == []

def test_large_rotation():
    """Test rotation larger than list length"""
    assert rotate_list([1, 2, 3, 4], 6) == [3, 4, 1, 2]

def test_invalid_input_type():
    """Test invalid input type for list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_list("not a list", 2)

def test_invalid_rotation_type():
    """Test invalid rotation type"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_list([1, 2, 3], "2")

def test_does_not_modify_original():
    """Ensure original list is not modified"""
    original = [1, 2, 3, 4]
    rotated = rotate_list(original, 2)
    assert original == [1, 2, 3, 4]
    assert rotated == [3, 4, 1, 2]