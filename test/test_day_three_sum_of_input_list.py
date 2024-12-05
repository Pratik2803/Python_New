import unittest
from unittest.mock import patch
from day_three_sum_of_input_list import sum_of_numbers


class TestSumOfNumbers(unittest.TestCase):

    @patch('builtins.input', return_value='1, 2 , 2.5, 3, 4 ,5')
    def test_valid_comma_separated(self, mock_input):
        result = sum_of_numbers()
        self.assertEqual(result, 17.5)


if __name__ == '__main__':
    unittest.main()
