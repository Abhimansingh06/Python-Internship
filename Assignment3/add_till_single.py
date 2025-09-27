"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take an large integer input.Keep adding its digits until the sum becomes a single digit.
Print the final single digit.


sample input:
Enter a large integer: 9876543210

sample output:
9

"""

num = int(input("Enter a large number: "))

while num >= 10:
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    num = total

print("sum of single digit is",num)
