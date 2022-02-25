# ! ANABEL
class ClassFizzBuzz():
    def __init__(self,input):
        self.input = input

    def transform(self):
        if self.input % 3 == 0 and self.input % 5 == 0:
            return 'FizzBuzz'
        if self.input % 3 == 0:
            return 'Fizz'
        if self.input % 5 == 0:
            return 'Buzz'
        return str(self.input)