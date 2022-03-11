# ! ANABEL
import unittest

from Fibonacci.class_fibonacci import ClassFibonacci


class ClassFibonacciShould(unittest.TestCase):
    def test_return_0_when_position_is_0(self):
        # Arrange
        input = 0
        # Act
        output = ClassFibonacci(position=input).fibonacci()
        # Assert
        expected = 0
        self.assertEqual(expected,output)

    def test_return_1_when_position_is_1(self):
        # Arrange
        input = 1
        # Act
        output = ClassFibonacci(position=input).fibonacci()
        # Assert
        expected = 1
        self.assertEqual(expected,output)

    def test_return_1_when_position_is_2(self):
        # Arrange
        input = 2
        # Act
        output = ClassFibonacci(position=input).fibonacci()
        # Assert
        expected = 1
        self.assertEqual(expected,output)

    def test_return_610_when_position_is_15(self):
        # Arrange
        input = 15
        # Act
        output = ClassFibonacci(position=input).fibonacci()
        # Assert
        expected = 610
        self.assertEqual(expected,output)