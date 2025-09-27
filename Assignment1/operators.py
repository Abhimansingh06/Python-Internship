"""
************************* Python internship 2025 *****************************
************************* Assignment Day-1 ***********************************

Problem statement: Take two numbers and an operator (+, -, , /) as input. Perform the operation and print the result.

sample input:
Enter first number: 8  
Enter second number: 2  
Enter operator (+, -, *, /): *

sample output:
The result is: 16

"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    print(f"The result is {num1 + num2}")
elif operator == '-':
    print(f"The result is {num1 - num2}")
elif operator ==  '*':
    print(f"The result is {num1 * num2}")
elif operator == '/':
    print(f"The result is {num1 / num2}")
else :
    print("Invalid operator")

    