"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to find all common elements between two lists.
Don't set functions

sample input:
["apple", "banana", "cherry"]
["banana", "cherry", "date"]

sample output:
["banana", "cherry"]
"""

def find_common(l1, l2):
    common = []
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return common

l1 = input("Enter words seperated by space: ").split()
l2 = input("Enter words seperated by space: ").split()

res = find_common(l1,l2)
print("Common list is: ",res)
