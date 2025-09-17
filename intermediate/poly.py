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


