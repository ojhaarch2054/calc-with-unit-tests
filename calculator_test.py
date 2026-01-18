import unittest
from unittest.mock import patch
from io import StringIO

#import the functions
from calculator import add, subtract, multiplication, divide, remainder

class TestCalculatorFunctions(unittest.TestCase):

    #test for add() function
    #mock input() to return 5 and 3
    @patch('builtins.input', side_effect=[5, 3])
    #capture printed output
    @patch('sys.stdout', new_callable=StringIO)
    def test_add(self, mock_stdout, mock_input):
        add()
        self.assertEqual(mock_stdout.getvalue().strip(), "Sum of 5 and 3 is 8")

    #test for subtract() function
    @patch('builtins.input', side_effect=[10, 3])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract(self, mock_stdout, mock_input):
        subtract()
        self.assertEqual(mock_stdout.getvalue().strip(), "Subtraction of 10 and 3 is 7")

    #test for multiplication() function
    @patch('builtins.input', side_effect=[4, 5])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        multiplication()
        self.assertEqual(mock_stdout.getvalue().strip(), "Multiplication of 4 and 5 is 20")

    #test for divide() function
    @patch('builtins.input', side_effect=[10, 2])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divide(self, mock_stdout, mock_input):
        divide()
        self.assertEqual(mock_stdout.getvalue().strip(), "Division of 10 by 2 is 5.0")

    #test for remainder() function
    @patch('builtins.input', side_effect=[10, 3])
    @patch('sys.stdout', new_callable=StringIO)
    def test_remainder(self, mock_stdout, mock_input):
        remainder()
        self.assertEqual(mock_stdout.getvalue().strip(), "Remainder of 10 divided by 3 is 1")

    #test for invalid input (ValueError) handling in addition
    @patch('builtins.input', side_effect=["abc", 3])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_add(self, mock_stdout, mock_input):
        add()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    unittest.main()
