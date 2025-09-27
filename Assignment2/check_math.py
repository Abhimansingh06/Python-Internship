"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take two integer inputs and check if they have the same last digit. Print "Match" if they do, otherwise print "No Match".
don't use loop or any built-in functions.

sample input:
Enter first number: 123  
Enter second number: 93 

sample output:
Match
"""

Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))

if Num1 % 10 == Num2 % 10:
    print("Match")
else:
    print("No Match")
    