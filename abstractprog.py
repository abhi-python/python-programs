from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    def __init__(self):
        self.length = int(input("Enter length :\t"))
        self.breadth = int(input ("Enter breadth :\t"))
    def printarea(self):
        return f"The area is : {self.length * self.breadth}"

rect1 = rectangle()
print(rect1.printarea())
