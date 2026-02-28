"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6     # Test with mixed positive and negative numbers
    assert max_subarray_sum([1]) == 1                         # Test with single element
    assert max_subarray_sum([-1]) == -1                       # Test with single negative element
    assert max_subarray_sum([-2,-3,-1]) == -1                # Test with all negative numbers
    assert max_subarray_sum([5,4,-1,7,8]) == 23              # Test with larger positive numbers
    assert max_subarray_sum([-9, -1, -2] * 1_000_000) == -1                  # Test with a large list

if __name__ == "__main__":
    pytest.main()