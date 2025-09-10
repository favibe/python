"""Prcticing String, list and their methods"""
s = "GeeksforGeeks"
print(s[0])   # first character
print(s[4])   # 5th character
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string
s0 = "hello geeks"
s1 = "H" + s0[1:]                   # update first character
s2 = s0.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)
print(len(s))
print(s.upper())
print(s.lower())
print(s * 3) # for repaeating strings
"""List and its method"""
print("----List and its methods--")
print("\n List---")
#can create list for iterable like tuple,stinfgs
a = list((1,2,3,"apple",4.5))
b = list(("GFG"))
print(a)
print(b)
#reparting a string
print(b * 2)
c = []

c.append(10)  
print("After append(10):", c)  

c.insert(0, 5)
print("After insert(0, 5):", c) 

c.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", c) 

c.clear()
print("After clear():", c)
#remove elemnt

d = [10, 20, 30, 40, 50]

d.remove(30)  
print("After remove(30):", d)

popped_val = d.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", d) 

del d[0]  
print("After del a[0]:", d)
#Nested List
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])
#tuple
# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)
my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[0])   # first element → 10
print(my_tuple[2])   # third element → 30
print(my_tuple[-1])  # last element → 50

#concatinating a tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)
#slicing a tuple
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])   # elements from index 1 to 3 → (20, 30, 40)
print(my_tuple[:3])    # first 3 elements → (10, 20, 30)
print(my_tuple[2:])    # from index 2 onwards → (30, 40, 50)
#dictionary (iterating through it)
d = {1: 'Geeks', 2: 'For', 'age':22}
# Iterate over keys
for key in d:
    print(key)
# Iterate over values
for value in d.values():
    print(value)
# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
#sett
set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))
#
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)
#pop removes but you dont know which elemnt as it is unorderd.
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Using pop on an empty set
set1.clear()  # Clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)
#typecasting other datattype in set with set() constructor

# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)
# Typecasting string into set
s = "GeeksforGeeks"
set1 = set(s)
print(set1)
# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)
"""Python Arrsy
numpy array
python array"""
"""# In Python, arrays are created using array.array(typecode, initializer).  
# typecode decides the data type (e.g., 'i' for int, 'f' for float), and initializer provides the values.  
"""
print("__ARRAY__")
import array as arr
a = arr.array('i', [1, 2, 3])
# accessing First Araay
print(a[0])
# adding element to array
a.append(5)
print(a)
# insert
import array as arr
a = arr.array('i', [1, 2, 3])
print(*a)
a.insert(1, 4)  # Insert 4 at index 1
print(*a)
#indexing
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print(a[0])
print(a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])
# remove() pop()
import array
a = array.array('i', [1, 2, 3, 1, 5])
# remove first occurance of 1
a.remove(1)
print(a)
# remove item at index 2
a.pop(2)
print(a)
#slicing
import array as arr
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)
res = a[3:8]
print(res)
res = a[5:]
print(res)
res = a[:]
print(res)
#searching element in an array
import array
a = array.array('i', [1, 2, 3, 1, 2, 5])
# index of 1st occurrence of 2
print(a.index(2))
# index of 1st occurrence of 1
print(a.index(1))
#updating elment in an array
import array
a = array.array('i', [1, 2, 3, 1, 2, 5])

# update item at index 2
a[2] = 6
print(a)

# update item at index 4
a[4] = 8
print(a)
#count
import array
a = array.array('i', [1, 2, 3, 4, 2, 5, 2])

count = a.count(2)
print(count)
#extend
import array as arr 
a = arr.array('i', [1, 2, 3,4,5])

a.extend([6,7,8,9,10])
print(a)
#reverse
import array
a = array.array('i', [1, 2, 3, 4, 5])
a.reverse()
print(*a)
#LIST COMPREHENSION
#list comprehension
a = [2, 3, 4, 5]
res = [x**2 for x in a]
print(res)
#using for loop to do this will be:
aa =[1,2,3,4,5]
rest = []
for val in aa:
    rest.append(val * 2)
print(res)
#ex2
res1 = [y for y in aa if y % 2 == 0]
print(res1)
#ex3 creating a list from range
list = [a for a in range(10)]
print(list)
#ex4 nested list
d = [(x,y) for x in range(3) for y in range(3)]
print(d)
#ex5 flatten a list
mat = [[1,2,3], [4,5,6],[7,8,9]]
res2 = [val for row in  mat for val in row]
print(res2)
