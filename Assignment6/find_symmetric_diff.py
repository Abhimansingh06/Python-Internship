"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given two sets, find elements that are present in either set but not in both.

sample input:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sample output:
(1, 2, 5, 6)

"""
"""
Problem statement:
Given two sets, find elements that are present in either set but not in both.
"""

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}

s1 = set_1 - set_2
s2 = set_2 - set_1

res = s1.union(s2)
print(res)
