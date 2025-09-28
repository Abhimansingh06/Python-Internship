"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
Write a function that takes a list of numbers and divides 100 by each. 
Skip any division by zero using exception handling.


sample input:
[25, 0, 10, -5]


sample output:
[4.0, 'error', 10.0, -20.0]

"""

def safe_division(n):
    try:
        return 100 / n
    except ZeroDivisionError:
        return "skip"
    
n = [25, 0, 10, -5]
res = list(map(safe_division, n))
print(res)