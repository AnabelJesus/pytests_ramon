# ! ANABEL
class ClassFibonacci():
    def __init__(self, input):
        self.input = input

    def _fibonacci(self):
        return 0 if self.input == 0 else 1

    def transform(self):
        return self._fibonacci()