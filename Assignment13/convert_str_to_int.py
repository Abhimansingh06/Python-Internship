"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
Write a function that converts a list of strings to integers using map(). 
Handle conversion errors using try inside a helper function.


sample input:
["10", "abc", "25", "4.5"]


sample output:
[10, 'error', 25, 'error']

"""

def convert_str_to_int(s):
    try:
        return int(s)
    except:
        return "error"
    
s = ["10", "abc", "25", "4.5"]
result = list(map(convert_str_to_int, s))
print(result)
