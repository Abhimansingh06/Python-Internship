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
20
20
30
10


sample output:
5
10
15
20
25
30
"""

n = int(input("Enter the size of list: "))

l = []

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)

unique_list = [0] * n
k = 0

for i in range(n):
    is_duplicate = False
    for j in range(k):
        if l[i] == unique_list[j]:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_list[k] = l[i]
        k += 1

print("Unique list is:", unique_list[:k])
