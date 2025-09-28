"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
write a function to group items in a list by a specific attribute or property into a dictionary.


sample input:
fruits = {"red": "apple", "yellow": "banana", "red": "cherry", "purple": "grape"}


Sample Output:
{'red': ['apple', 'cherry'], 'yellow': ['banana'], 'purple': ['grape']}

"""

def group_by_property(fruits):

    fruits_list = {}

    for colour, fruit in fruits.items():
        if colour not in fruits_list:
            fruits_list[colour] = [fruit]
        else:
            fruits_list[colour].append(fruit)

    return fruits_list

fruits = {"red": "apple", "yellow": "banana", "red": "cherry", "purple": "grape"}

res = group_by_property(fruits)
print(res)
