"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Take a list of integers as input. Create a new list that contains only unique elements (preserving original order).
Use loops and conditionals only — don’t use set().


sample input:
5
10
10
15
25
20
30
10


sample output:
Second maximum number is: 25


"""

n = int(input("Enter the size of list: "))
l = []

for i in range(n):
    num = int(input("Enter list elements: "))
    l.append(num)

print("Your list is: ", l)

max1 = l[0]
max2 = l[0]

for i in l:
    if max1 < i:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i

print(f"Second maximum is {max2}")
