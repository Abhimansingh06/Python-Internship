"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
Group items in a list by a specific attribute or property into a dictionary.


sample input:
fruits = {"red": "apple", "yellow": "banana", "red": "cherry", "purple": "grape"}


Sample Output:
{'red': ['apple', 'cherry'], 'yellow': ['banana'], 'purple': ['grape']}

"""

fruits = {"red": "apple", "yellow": "banana", "red": "cherry", "purple": "grape"}

fruits_list = {}

for colour, fruit in fruits.items():
    if colour not in fruits_list:
        fruits_list[colour] = [fruit]
    else:
        fruits_list[colour].append(fruit)

print(fruits_list)