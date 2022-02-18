# ! ANABEL
import unittest

from class_fizz_buzz import ClassFizzBuzz


class ClassFizzBuzzShould(unittest.TestCase):
    def test_returns_string_number_when_not_multiple(self):
        fizz_buzz = ClassFizzBuzz()

        #Arrange
        input = 1

        #Act
        output = fizz_buzz.transform(input=input)

        #Assert
        expected = '1'
        self.assertEqual(output,expected)

    def test_multiple_of_three_when_(self):
        pass