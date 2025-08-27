"""
print("Hello World!")
# variables
a = "Soap"
#type casting 
b = 123
cnt = str(b)
bb = 5
fb = float(bb)
bbs = "123"
ibbs = int(bbs)
#take mutiple input
x,y,z = input("Enter three numbers: ").split()
print("The total number of teachers are: ", x)
print("The total number of male teachers are: ", y)
print("The total number of female  teachers are: ", z)
# take an interger input
n = int(input("Enter number of books: "))
print(n)
#for float/ decoimal
j = float(input("Enter the price of books: "))
print(j)
#Finding datatype
c = ("i", "enjoy", "coding")
d = ["i", "enjoy", "coding"]
e = {"i":1, "enjoy":2, "coding":3}
print(type(a))
print(type(b))
print(type(j))
print(type(c))
print(type(d))
print(type(6))


#Output frmatting
#Format()
amount = 156.7890
print("Amount: ${:.2f}".format(amount))
# using sep and end
print ("loading", end="---")
print("Done!")
print("2025", "08", "26", sep="/")  
print('E', 'G', 'G', sep='')
print("Vanessa", "Lucas", sep=" ❤️ ")  
print("Line 1", end="\n---\n")
print("Line 2")
#using f-string
print(f"hello world say {a} and {b}")
#using % operator (old formating style)
# Taking input from the user
num = int(input("Enter a value: "))
add = num + 5
# Output
print("The sum is %d" % add)

"""
#data types
# 1. Numeric Data type

a = 5 #integer
b = 34.13 #float
c = 3 + 5j #complex number

# 2. Sequence Data type

str = "A string" #string
li = [1,2,3] #list 
tup = ("i", "love", "it", "here")  #tuple
print(tup)

#Accessing list items
list = ["book", "power", "success", "win", "growth", "love"]
print(list[0]) #book
print(list[-2]) # growth. # list can be acess with +ve and -ve index.

#Accesssing tuple item
tup1 = ([1, 2, 3, 4, 5])
print(tup1[0]) #1
print(tup1[-3]) #3

# 3. Boolean Data type

tre = True
fls = False
gg = true # an error
print(tre)

# 4. Set Data type



# 5. Dictionary Data type


