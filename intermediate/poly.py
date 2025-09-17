#polymorphism
"""Polymorphism means "many forms". It refers to the ability of an entity 
(like a function or object) to perform different actions based on the context."""

#1. Compile-time Polymorphism
"""Compile-time polymorphism means deciding which method or operation to run during compilation,
 usually through method or operator overloading."""
class Calculator:
    def multiply(self, a =1, b=1, *args):
        result =  a * b
        for num in args:
            result *= num
        return result
#Create an object
calc = Calculator()

#using default arguments
print(calc.multiply())
print(calc.multiply(4))

#using mutiple argument
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))

#2. Runtime Polymorphism (Overriding)
"""Runtime polymorphism means that the behavior of a method is decided while program is running, 
based on the object calling it."""
class Animal:
    def sound(self):
        return "Any Generic Sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"    

#polymorphism  Behaviour
animals =[Dog(), Cat(), Animal()]
for animal in  animals:
    print(animal.sound())

#Polymorphism in Built-in Functions
"""Python’s built-in functions like len() and max() are polymorphic they work with different
 data types and return results based on type of object passed."""
print(len("Hello")) #strings
print(len([2, 4, 6, 7]))

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings

#Polymorphism in Functions
"""In Python, polymorphism lets functions accept different object types as long as they support needed behavior"""
class Pen:
    def ude(self):
        return "writing"
    
class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())    

perform_task(Pen())  
perform_task(Eraser())        

#Polymorphism in Operators
"""In Python, same operator (+) can perform different tasks depending on operand types. 
This is known as operator overloading. This flexibility is a key aspect of polymorphism in Python."""
print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation
