"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given a tuple of integers, convert it to a tuple without duplicates (preserve order).


sample input:
(1, 2, 2, 3, 4, 4, 5)

sample output:
(1, 2, 3, 4, 5)

"""
"""
Problem statement:
Given a tuple of integers, convert it to a tuple without duplicates (preserve order).
"""

t1 = (1, 2, 2, 3, 4, 4, 5)

unique_list = []
for i in t1:
    if i not in unique_list:
        unique_list.append(i)

res = tuple(unique_list)
print(unique_list)
