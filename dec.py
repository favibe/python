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
    