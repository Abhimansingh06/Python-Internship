"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
Write a function that takes a dictionary of student names and scores, and returns a list of names sorted by their scores.

sample input:
{"Akasha": 85, "Rahul": 90, "Priya": 78}

sample output:
['Priya', 'Akasha', 'Rahul']
"""

def sort_dictionary(student_details):
    sorted_items = sorted(student_details.items(), key = lambda x : x[1])
    sorted_names = []

    for item in sorted_items:
        name = item[0]
        sorted_names.append(name)

    return sorted_names

student_details = {"Akasha": 85, "Rahul": 90, "Priya": 78}
res = sort_dictionary(student_details)
print(res)
