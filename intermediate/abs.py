#data Abstraction
"""Data abstraction means showing only the essential features and hiding the complex internal details."""
"""Abstract classes are created using abc module and @abstractmethod decorator,
 allowing developers to enforce method implementation in subclasses while hiding complex internal logic."""
from abc import ABC, abstractmethod

class greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass #Abstarct method

class English(greet):
    def say_hello(self):
        return "hello"
    
g = English()
print(g.say_hello())

#Abstarct Method
"""Abstract methods are method declarations without a body defined inside an abstract class. 
They act as placeholders that force subclasses to provide their own specific implementation, 
ensuring consistent structure across derived classes."""
