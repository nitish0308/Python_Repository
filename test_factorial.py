from python_practice import factorial
import unittest

  
class TestFactorial(unittest.TestCase):
    def test_zero_factorial(self):
        assert factorial(0) == 1
    
    def test_one_factorial(self):
        assert factorial(1) == 1
    
    def test_small_factorials(self):
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 25
        assert factorial(5) == 120
    

if __name__ == '__main__':
    unittest.main()