# ! ANABEL
import unittest

from class_fizz_buzz import ClassFizzBuzz


class ClassFizzBuzzShould(unittest.TestCase):
    def test_returns_1_as_string_when_not_multiple(self):
        #Arrange
        input = 1
        #Act
        output = ClassFizzBuzz(input=input).transform()
        #Assert
        expected = '1'
        self.assertEqual(output,expected)

    def test_returns_2_as_string_when_not_multiple(self):
        #Arrange
        input = 2
        #Act
        output = ClassFizzBuzz(input=input).transform()
        #Assert
        expected = '2'
        self.assertEqual(output,expected)

    def test_returns_4_as_string_when_not_multiple(self):
        # Arrange
        input = 4
        # Act
        output = ClassFizzBuzz(input=input).transform()
        # Assert
        expected = '4'
        self.assertEqual(output, expected)

    def test_returns_3_as_Fizz_when_multiple_of_three(self):
        # Arrange
        input = 3
        # Act
        output = ClassFizzBuzz(input=input).transform()
        # Assert
        expected = 'Fizz'
        self.assertEqual(output, expected)

    def test_returns_6_as_Fizz_when_multiple_of_three(self):
        # Arrange
        input = 6
        # Act
        output = ClassFizzBuzz(input=input).transform()
        # Assert
        expected = 'Fizz'
        self.assertEqual(output, expected)

    def test_returns_9_as_Fizz_when_multiple_of_three(self):
        # Arrange
        input = 9
        # Act
        output = ClassFizzBuzz(input=input).transform()
        # Assert
        expected = 'Fizz'
        self.assertEqual(output, expected)

    def test_returns_5_as_Fizz_when_multiple_of_five(self):
        # Arrange
        input = 5
        # Act
        output = ClassFizzBuzz(input=input).transform()
        # Assert
        expected = 'Buzz'
        self.assertEqual(output, expected)

    def test_returns_5_as_Fizz_when_multiple_of_five(self):
        # Arrange
        input = 15
        # Act
        output = ClassFizzBuzz(input=input).transform()
        # Assert
        expected = 'FizzBuzz'
        self.assertEqual(output, expected)