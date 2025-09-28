"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 11 **********************************

Problem statement:
Write a function to find the Greatest Common Divisor (GCD) of two positive integers.

Note: The GCD of two numbers is the largest number that divides both of them without leaving a remainder.


sample input:
n1 = 24
n2 = 36

sample output:
output: 12

"""

def find_gcd(n1 , n2):

    gcd = 1
    for i in range(1, min(n1,n2)):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i

    return gcd

n1 = int(input(("Enter num1: ")))
n2 = int(input(("Enter num 2: ")))

res = find_gcd(n1, n2)
print(res)
