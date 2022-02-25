# ! ANABEL
import unittest

from Fibonacci.class_fibonacci import ClassFibonacci


class ClassFibonacciShould(unittest.TestCase):
    def test_returns_0_when_position_is_0(self):
        # Arrange
        input = 0
        # Act
        output = ClassFibonacci(input=input).transform()
        # Assert
        expected = 0
        self.assertEqual(expected,output)