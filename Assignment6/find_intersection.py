"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given two lists (not set) of integers, print the common elements.

sample input:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

sample output:
[3, 4]

"""
"""
Problem statement:
Given two lists (not set) of integers, print the common elements.
"""
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []
for i in list1:
    if i in list2:
        common.append(i)

print(common)

