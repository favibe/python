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
