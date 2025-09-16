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


#OOP
#Inheritance
#Using super()function
class Animal:
  def __init__(self, name):
    self.name = name

  def info(self):
    print(f"Animal name is: {self.name}")
#Child Class
class Dog(Animal):
  def __init__(self, name, breed):
    super(). __init__(name) #calling the parent constructor
    self.breed = breed

  def detail(self):
   print(self.name, "is a", self.breed) 

d = Dog("Puppy", "Bulldog")
d.info() #parent method
d.detail() #child method

#Types of inheritance
#1. Single inheritance
#A class inherit from one parent class
class Person:
  def __init__(self, name):
    self.name = name
class employee(Person):
  
  def show_role(self):
    print(self.name, " is an employee")
    
emp = employee("Don")
emp.show_role()
print("Name is:", emp.name)

#Multiple Inheritance
#A class inherit from more than one parent class
print ("--Multiple Inheritance--")

class Persons: 
  def __init__(self, name):
    self.name = name
    
class Job:
  def __init__(self, job):
    self.job = job
    
class employees(Persons, Job):
  def __init__(self, name, job):
    Persons.__init__(self, name) 
    Job.__init__(self, job)

  def details(self):
    print(self.name, "is a", self.job)

emp1 = employees("Favour", "Full Stack Developer")
emp1.details()

#Multilevel inheritance
# A class inherit from another class which also inherit from another class. 
print("_Multilevel inheritance_")

class person:
  def __init__(self,name):
    self.name = name

class Employee(person):
  def show_role(self):
    print(self.name, " is an employee")
class Manager(Employee):  # Manager inherits from Employee
  def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")

#Hierarchical Inheritance 
#more than one child class inherit from one parent class
print(" Hierarchical Inheritance")
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "works as an employee")

class Intern(Person):  
    def role(self):
        print(self.name, "is an intern")

emp = Employee("David")
emp.role()

intern = Intern("Eva")
intern.role()


#Hybrid inheritance 
# A combination of more than one type of inheritance. 

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)

lead = TeamLead("Sophia", "AI Development")
lead.role()
lead.details()
"""Here TeamLead inherits from Employee (which already inherits Person) and also from Project. This combines single, multilevel and multiple inheritance -> hybrid.

it combines single, multilevel (employee inherit person), and mutiple(team leader inherit employee and project) inheritance. Gives us Hybrid Inheritance."""



