#Aruthemetic Operator
a = 15
b = 4
c = a
print("Addition:", a+b)
print("Substraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus:", a%b)
print("Exponention:", a**b)

print("-------")
#comparison Operators
print("Less Than:",a < b)
print("Less Than or Equal to:",a <= b)
print("Greater Than oe Equal to:",a >= b)
print("Greater Than:",a > b)
print("Equal:",a == b)
print("Not Equal:",a != b)

print("----")
#logical Operator
aa = True
bb = False
print(aa and bb)
print(aa or bb)
print (not aa)

print("-----")
#Bitwise Operator
aaa = 10
bbb = 4

print(aaa & bbb)
print(aaa | bbb)
print(~aaa)
print(aaa ^ bbb)
print(aaa >> 2)
print(aaa << 2)

#identity Operator
print("identity operator")

print (a is not b)
print (a is c)

#memebersip operator
print("memebership operator")

x = 24
y = 20
list = [20,30,40,50,60]
if (x not in list):
    print("x is NOT in the list")
else:
    print("x is present")
if (y in list):
    print("y is present")
else:
   print("y is Not present in the list")



#Conditional sttaement
marks = 25
if marks <=30:
    print("Pass")
else :
    print("fail")
#Shorthand Ternanry Operator way
mark = 25
total = "pass" if mark <=30 else "fail"
print(total)

#elif condition
age = 25
if age <= 12:
    print("child")
elif age <=19:
    print("Teenager")
elif age <= 25:
    print("Young Adult")
else:
    print("Adult")

#Nested if sttsement
age1 = 70
is_member = True

if age1 >= 60:
    if is_member:
        print("30% Senior Discount")
    else:
        print("20% Senior Discount")
else:
 print("Not Eligible for Senior Discount")

 #ex2
mark2 = 85
if mark2 >= 50:
    if mark2 >= 90:
        print("A+")
    elif mark2 >= 75:
        print("A")
    else:
        print("B")
else:
     print("Fail")

#ex3
age2 =  20
citizen = True
voter = True
if age >= 18:
    if citizen:
        if voter:
            print("eligible to vote")
        else:
            print("Need voter card")
    else:
        print("not a citizen")
else:
    print("Too young")

#ex4
n = -4
if n >= 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")

#Check if user have balanmce to buy an item
balance = float(input("Enter Your Bslance: "))
price = float(input("Enter item Price: "))
if balance > price:
    print("Purchase Successful")
else:
    print("Insufficient Funds")
"""EXCERCISE FROM GFG

     class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if flag == False:
            if (a>= 0 and b <0) or (a <0 and b>= 0):
             return True
        if flag == True:
            if  a < 0 and b < 0:
             return True
        return False
        """
#Control Loop
nn = 4
for i in range(0, nn):
    print(i)
#2
s = "geeks"
for i in s:
    print(i)
#3
li = ["geek", 1, "here"]
for i in li:
    print(i)
    #or we can iterate with index, bt first knowing it lenght
for index in range(len(li)):
    print(li[index])
#4 Same thing for set{1,2,3,4,5} and tup("cup","spoon")
#5
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i])) 

# using else statement with for loop
for i in range(5):
    print(i)
else:
    print("Loop successfully")
    # this will print o-4 and still print the else blocck ststemrnt
# else for loop with break
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("looped successfully")
# Hee the break ststement will stop the loop once i = 2, and break the loop that way the else won't print

#WHILE LOOP
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Helllo Woeld")
#2
count = 1
while(count <= 5):
    print("Count is:", count)
    count += 1
#using else statement with While loop
#nested loop (in python can have a for loop in while loop and vice versa)

for i in range(1, 4):          # outer loop
    for j in range(1, 4):      # inner loop
        print(i, "*", j, "=", i * j)
    print("-----")  # separates each row
#2
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
#CONTROL STATEMENT
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
#2
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)
