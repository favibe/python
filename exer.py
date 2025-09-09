#2 print the number of saquare from number 1, to number provodee
n = 6
for i in range(1, n+1):
    print("square of", i, "is", i**2)
#function
#default argumment
def profile(name, age=23):
    print(f"Name: {name}, Age: {age}")
profile("John")
profile("Mary", 25)
# profile() #would throw an error
#Keyword argument
def student(fname, lname):
    print(fname, lname)
student(fname="Sherk", lname="Bob")
student(lname="Bill", fname="Sherk")

#Positional Argument
#here the argument must come in order
def nameAge(name, age):
    print("my name is: ", name)
    print("my age is ", age)
print("case-1")
nameAge("Suraj", 27)
print("\n case-2")
nameAge(25,"Suraj")
#in this argument position/order matter
#ARGS AND KWARGS
def add(*args):
    return sum(args)
print(add(1,3,4))
print(add(2,3))
#kwargs
def show_info(**kwargs):
    print(kwargs)
show_info(name="Alice", age=23, city="London")
#INNER/NESTED FUNCTIONS
def fun1():
    s = "I love coding"
    def fun2():
        print(s)
    fun2()
fun1()
#Anonymous Functions
square = lambda n: n*n
print(square(4))
#2
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))
#3
add = lambda x, y: x + y
print(add(2,4))
#passs by onject reference
# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified
#Recursive Function
def factorial(n):
    if n == 0:   # base case
        return 1
    else:        # recursive case
        return n * factorial(n - 1)

print(factorial(5))  # 120
