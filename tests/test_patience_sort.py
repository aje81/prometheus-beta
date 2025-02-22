import pytest
from src.patience_sort import patience_sort

def test_patience_sort_basic_list():
    """Test sorting a basic list of integers"""
    input_list = [5, 2, 8, 12, 1, 6]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    """Test sorting a list with a single element"""
    assert patience_sort([42]) == [42]

def test_patience_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_patience_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_with_strings():
    """Test sorting a list of strings"""
    input_list = ["banana", "apple", "cherry", "date"]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -8, 12, 1, -6]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected