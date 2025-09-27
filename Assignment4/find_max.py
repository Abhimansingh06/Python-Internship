"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Take a list of integers as input. Using a loop, find and print the maximum element (don’t use max() function).


sample input:
5
10
15
20
25
30

sample output:
30
"""

n = int(input("Enter the size of list: "))
l = []

for i in range(n):
    num = int(input("Enter list elements: "))
    l.append(num)

print("Your list is: ", l)

max = l[0]

for i in range(1,n):
    if max < l[i]:
        max = l[i]

print(f"{max} is maximum among list")
