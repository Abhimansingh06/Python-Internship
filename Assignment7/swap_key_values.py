"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
Write a program that swaps the keys and values in a dictionary. If there are duplicate values, the last key will be kept.


sample input:
original = {'a': 1, 'b': 2, 'c': 3}

Sample Output:
{1: 'a', 2: 'b', 3: 'c'}

"""
original = {'a' : 1, 'b' : 2, 'c' : 3}

swapped = {}
for key, value in original.items():
    swapped[value] = key

print("Before swapping:", original)
print("After swapping: ", swapped)