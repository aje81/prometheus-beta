import os
import pytest
from src.word_frequency import count_word_frequencies, get_total_word_count


@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file with sample words for testing."""
    sample_content = "apple, banana, apple, cherry, banana, apple"
    file_path = tmp_path / "sample_words.txt"
    file_path.write_text(sample_content)
    return str(file_path)


def test_count_word_frequencies(sample_file):
    """Test counting word frequencies."""
    result = count_word_frequencies(sample_file)
    
    # Check the correct order and counts
    assert list(result.keys()) == ['apple', 'banana', 'cherry']
    assert result['apple'] == 3
    assert result['banana'] == 2
    assert result['cherry'] == 1


def test_total_word_count(sample_file):
    """Test getting total word count."""
    total_count = get_total_word_count(sample_file)
    assert total_count == 6


def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        count_word_frequencies("non_existent_file.txt")


def test_empty_file(tmp_path):
    """Test handling of empty file."""
    empty_file = tmp_path / "empty.txt"
    empty_file.touch()
    
    with pytest.raises(ValueError, match="The input file is empty."):
        count_word_frequencies(str(empty_file))


def test_file_with_only_whitespace(tmp_path):
    """Test file with only whitespace."""
    whitespace_file = tmp_path / "whitespace.txt"
    whitespace_file.write_text("   ,  ,  ")
    
    with pytest.raises(ValueError, match="No valid words found in the file."):
        count_word_frequencies(str(whitespace_file))


def test_case_sensitivity(tmp_path):
    """Test word frequency is case-sensitive."""
    case_file = tmp_path / "case.txt"
    case_file.write_text("Apple, apple, APPLE, Banana, banana")
    
    result = count_word_frequencies(str(case_file))
    assert list(result.keys()) == ['Apple', 'apple', 'APPLE', 'Banana', 'banana']
    assert result['Apple'] == 1
    assert result['apple'] == 1
    assert result['APPLE'] == 1