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
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

#Concrete Method
"""Concrete methods are fully implemented methods within an abstract class. 
Subclasses can inherit and use them directly, promoting code reuse without needing 
to redefine common functionality."""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, to be implemented by subclasses

    def move(self):
        return "Moving"  # Concrete method with implementation
    
#Abstract Properties
"""Abstract properties work like abstract methods but are used for properties. 
These properties are declared with @property decorator and marked as abstract using @abstractmethod. 
Subclasses must implement these properties."""
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)

#Abstract Class Instantiation
"""Abstract classes cannot be instantiated directly. This is because they contain one or more 
abstract methods or properties that lack implementations. Attempting to instantiate an abstract 
class results in a TypeError."""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

animal = Animal()