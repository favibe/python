class Dog:
    species = "Canine" # class atribute
    def __init__(self, name, age, height): 
        self.name = name  #instance attribute
        self.age = age     #instance attribute
        self.height = height    #instance attribute

#creating an objects 
dog1 = Dog("falz", 2, 3.12)
dog2 = Dog("shell", 3, 2.3)
print(dog1.name)
print(dog1.species)