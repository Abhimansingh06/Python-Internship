"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to convert a given list to a dictionary.

sample input:
["name=Akasha", "age=30", "city=Hyderabad"], 

sample output:
{
    'name': 'Akasha',
    'age': 30,
    'city': 'Hyderabad'
}
"""

def convert_list_to_dict(l):
    dictionary = {}
    for i in l:
        key, value = i.split("=")
        dictionary[key] = value
    return dictionary

l = input("Enter words seperated by space: ").split()
res = convert_list_to_dict(l)
print(res)
