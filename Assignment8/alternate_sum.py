"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Write a function that takes a list of integers, sum elements alternatively from start and end.


sample input:
Enter the number of element in the list (n): 5
1
2 
3
4
5

sample output:
15  # (1 + 5) + (2 + 4) + 3 = 6 + 6 + 3 = 15

"""

def alternate_sum(n):

    start = 0
    end = n - 1
    add = 0
    while start <= end:
        if start == end:
            add += l[start]
        else:
            add += l[start] + l[end]
        end -= 1
        start += 1

    return add

n = int(input("Enter the number of element in the list: "))

l = []
for i in range(n):
    num = int(input("Enter elements: "))
    l.append(num)

result = alternate_sum(n,l)

print("Alternate sum is", result)

