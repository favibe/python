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
#more lambda functions
li = [lambda arg = x: arg *10 for x in range(1,6)]
for i in li:
    print(i())
#more example 2
cal = lambda x, y: (x + y, x * y)
res = cal(11, 10)
print(res)
#with filter(lambda)
n = [1,2,3,4,5,6,7,8,9]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))
#with map
a = [11,22,32,44]
b = map(lambda x: x *2, a)
print(list(b))
#with reduce
from functools import reduce
c = [2,3,4,5]
d = reduce(lambda x,y: x * y, c)
print(d)
#map() with mutiple iterable
aa = [1,2,3,4]
bb = [5,6,4,7]
res1 = map(lambda x,y: x + y, aa, bb)
print(list(res1))
#more 3
#upper() convert ti uppercase
#strip() removes whitespace from string
#convert to uppercase with map()
fruit = ["apple", "banana","cherry"]
res2 = map(str.upper, fruit)
print(list(res2))
res3 = map(lambda s: s[0],fruit)
print(list(res3)) # extracting  the first charcter
#filter
#filtering falsy value
A =["Apple", "","Banana", 0, "Cherry",None]
L = filter(None, A)
print(list(L))
#filter words greater than 5
aaa = ["apple", "banana", "cherry", "kiwi", "grape"]
bbb= filter(lambda w: len(w) > 5, aaa)
print(list(bbb))
#using filter and map(filter even num, map double it)
a1 = [1, 2, 3, 4, 5, 6]
b1 = filter(lambda x: x % 2 == 0, a1)
c1 = map(lambda x: x * 2, b1)
print(list(c1))
#filter example
def starts_a(w):
    return w.startswith("a")

li1 = ["apple", "banana", "avocado", "cherry", "apricot"]
ress = filter(starts_a, li1)
print(list(ress))
#reduce 
import functools
import operator
list = [1, 3, 5, 6, 2]

print(functools.reduce(operator.add, list))
print(functools.reduce(operator.mul, list)) 
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))
#2 reduce()
from functools import reduce
def add(x, y):
    return x + y

a2 = [1, 2, 3, 4, 5]
res4 = reduce(add, a2)
print(res4)