"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]     # Test with mixed positive and negative numbers
    assert two_sum([3, 2, 4], 6) == [1, 2]         # Test with single element
    assert two_sum([3, 3], 6) == [0, 1]            # Test with all negative numbers
    assert two_sum([1, 2, 4], 7) == []              # Test with impossible target
    assert two_sum(list(range(1000)), 999) == [499, 500] # Test with a large list

if __name__ == "__main__":
    pytest.main()