#exception Handling
# Syntax Error (Error)
print("Hello world")  # Missing closing parenthesis
# ZeroDivisionError (Exception)
n = 10
res = n / 0
#ex2 handling the zero dividion runtime error
try:
    n = 0
    res = 100 / n
except ZeroDivisionError:
    print("You cant divide by zero")
except ValueError:
    print("Enter a valid number")
else:
    print("Result is:", n)
finally:
    print("Exception complete")
#ex3
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
except (ValueError, TypeError) as e:
    print("Error", e)
except IndexError:
    print("Index out of range.")
    #ex4
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)