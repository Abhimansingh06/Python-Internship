
"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Given a list of integers, count how many even and odd numbers are there.
Print the count of even and odd numbers.


sample input:
5
10
15
20
30
10


sample output:
Number of even numbers: 4
Number of odd numbers: 2
"""

l = [5, 10, 15, 20, 30, 10]

even_count = 0
odd_count = 0

for i in l:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even is {even_count}")
print(f"Number of odd is {odd_count}")
