"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take three numbers and print the largest one using only if-else (no built-in functions like max()).

sample input:
Enter numbers: 12, 45, 33  

sample output:
Largest number is: 45  

"""

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2:
    if n1 < n3:
        print(f"{n3} is greater")
    else:
        print(f"{n1} is greater")
else:
    print(f"{n2} is greater")
    