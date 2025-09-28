"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
write a function that takes a number as input and checks the number of prime numbers less than or equal to that number.

sample input:
Enter an integer: 120
Enter an integer: 500

sample output:
30
78
"""

def count_prime(num):
    count = 0

    if num <= 1:
        return 0
    
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
            
    return count

num = int(input("Enter a number: "))
res = count_prime(num)

print(res)