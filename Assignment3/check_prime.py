"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take an integer input. Check whether the number is prime or not.
Print "Prime" or "Not Prime".

sample input:
Enter an integer: 7
Enter an integer: 10

sample output:
Prime
Not Prime
"""


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2 , num):
        if num % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

    