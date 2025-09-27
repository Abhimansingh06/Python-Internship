"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Given a number n, find the sum of all numbers between 1 and n which are divisible by 3 or 5.


sample input:
Enter value of n: 10


sample output:
sum of numbers divisible by 3 or 5: 33  # 3+5+6+9+10 = 33
"""

n = int(input("Enter a number: "))

add = 0
for i in range(1,n):
    if i % 3 == 0 or i % 5 == 0:
        add += i

print(f"sum of number divisisble by 3 or 5 is: {add}")
