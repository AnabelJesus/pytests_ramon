# ! ANABEL
class ClassFibonacci():
    def __init__(self, position):
        self.position = position

    def _fibonacci(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self._fibonacci(n-1) + self._fibonacci(n-2)

    def fibonacci(self):
        return self._fibonacci(self.position)