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
