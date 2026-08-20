# test_prime_finder.py
from prime_finder import prime_finder

def test_prime_finder_mixed_list():
    # Input list has primes, composites, and edge cases
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected_output = [2, 3, 5, 7, 11]
    assert prime_finder(input_list) == expected_output

def test_prime_finder_no_primes():
    assert prime_finder([4, 6, 8, 9, 10]) == []

def test_prime_finder_empty_and_negatives():
    assert prime_finder([]) == []
    assert prime_finder([-5, -3, 0, 1]) == []
