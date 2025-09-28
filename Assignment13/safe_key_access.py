"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
write a function that takes a list of keys, retrieve values from a given dictionary. 
Use exception handling to return 'key error' if key is missing.


sample input:
keys: ['a', 'b', 'x']
dictionary: {'a': 1, 'b': 2}


sample output:
[1, 2, 'key error']

"""

def safe_key_access(keys):
    try:
        return data[keys]
    except KeyError:
        return 'key error'

keys = ['a', 'b', 'x']
data = {'a': 1, 'b': 2}

res = list(map(safe_key_access, keys))

print(res)
