"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 12 **********************************

Problem statement: 
Implement a function that returns the index of an element in a sorted list using binary search. If not found, return -1.


sample input:
arr = [1, 3, 5, 7, 9]
target=7

sample output:
3

"""

def find_target(arr,target):
    right = len(arr) - 1
    left = 0

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] > target:
            right = middle - 1

        else:
            left = middle + 1

    return -1

arr = list(map(int, input("Enter elements: ").split())) 
target  = int(input("Enter target: "))

result = find_target(arr, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")
    