"""Example: Here, we create a parent class Animal that has a method info(). 
Then we create a child classes Dog that inherit from Animal and add their own behavior."""
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name is", self.name)  

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()  #inherited method
d.sound() 
