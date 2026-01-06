from add import add
from subtract import subtract
from multiply import multiply
from divide import divide   

print("This is a calculator ")

num1 = float(input("Enter first number:"))
num2 = float (input("Enter second number:"))

print("Addition of 2 numbers:", add(num1,num2))
print("Subtraction of 2 numbers:", subtract(num1,num2))
print("Multiplication of 2 numbers:", multiply(num1,num2))      
print("Division of 2 numbers:", divide(num1,num2))