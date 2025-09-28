"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
Write a program that performs various set operations (union, intersection, difference) on two sets based on a specified operation parameter.


sample input:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
operation = "symmetric_difference"

Sample Output:
{1, 2, 5, 6}

"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

operation = input("Enter operation (eg. union, intersection, difference, symmetric_diifference): ")

if operation == "union":
    result = set1.union(set2)
elif operation == "intersection":
    result = set1.intersection(set2)
elif operation == "difference":
    result = set1.difference(set2)
elif operation == "symmetric_difference":
    result = set1.symmetric_difference(set2)
else:
    result = "Invalid opeartion"

print(result)
