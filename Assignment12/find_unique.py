"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 12 **********************************

Problem statement: 
Given a list of words, return the kth unique word based on order of first appearance. 
If less than k unique words exist, return None.

hint- dont use set, it will remove the order of the elements.

sample input:
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
k = 2

sample output:
"cherry"
"""

def find_unique(words, k):
    count = {}
    order = []

    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            order.append(i)

    unique = [i for i in order if count[i] == 1]

    if k <= len(unique):
        return unique[k - 1]
    else:
        return None
    

words = ["apple", "banana", "apple", "cherry", "banana", "date"]
k = 2

res = find_unique(words, k)
print(res)