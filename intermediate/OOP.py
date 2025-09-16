class Dog:
    species = "Canine" # class atribute
    def __init__(self, name, age, height): 
        self.name = name  #instance attribute
        self.age = age     #instance attribute
        self.height = height    #instance attribute

#creating an objects 
dog1 = Dog("falz", 2, 3.12)
dog2 = Dog("shell", 3, 2.3)
Dog.species = "Feline" #can be modified 
dog1.name = "balz"    #can be modified 
print(dog1.name)
print(dog1.height)
print(dog1.species)

#Encapsulation
"""Encapsulation means hiding internal details of a class and only exposing what's necessary.
 It helps to protect important data from being changed directly and keeps the code secure and organized."""

class Employee:
    def __init__(self, name, salary):
        self.name = name  #public attribute
        self.__salary = salary  #private attribute (cannot be accessed directly)
emp = Employee("Leo", 500)
print(emp.name)
#print(emp.__salary)     #will throw an error

print("---encapsulation public memebers---")
#Acess Modifier
#1. Public Memebers
class Employee:
    def __init__(self, name, age):
        self.name = name # public attribute
        self.age = age

    def display_name(self): 
        print(self.name)
    def birthday(self):
        self.age +=1
        #return f"Happy Birthday {self.name}, you are now {self.age} old"   
        print(f"Happy Birthday {self.name}, you are now {self.age} old" ) 

emp = Employee("John", 30)   
emp.display_name()
emp.birthday()
print(emp.name)

print("---encapsulation protected memebers---")
#2. Protected Member
class Empolyees:
    def __init__(self,name,age):
        self.name = name #public attribute
        self._age = age   #protected attribute (using a single underscore(can be acces within the class &subclass))
class SubEmpolyee(Empolyees):
    def show_age(self):
        print("Age:",self._age)      #acessible in subclass

emp = SubEmpolyee("Cakes",23)
print(emp.name)
emp.show_age()           

print("---encapsulation Private memebers---")
#private Members
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly

print("---protected and private method---")
#Declaring Protected and Private Methods
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def _show_balance(self):
        print(f"Balance: ${self.balance}") # protected Balance

    def __update_balance(self, amount):
        self.balance += amount   #private method
        
    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount) #Acessing private Method internally
            self._show_balance() #Acessing Protected    method
        else:
            print("Invalid amount deposit")
account = BankAccount(1000)
account._show_balance()      # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally


print("--Getter and Setter Mehods---")
#Getter and Setter Methods
class employyeeX:
    def __init__(self):
        self.__salary = 1000  # private attribute

    def get_salary(self):    # getter method
        return self.__salary
    
    def set_salary(self, amount):  # setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

# create an object
emp = employyeeX()

# update using setter
emp.set_salary(6000)

# access using getter
print(emp.get_salary())

