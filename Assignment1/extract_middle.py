"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Input a string and print its middle character(s). If the length is even, print the two middle characters; if odd, print one.

sample input:
Enter a string: hello

sample output:
Middle character: l

"""

str = input("Enter a string: ")

length = len(str)

if length % 2 == 0:
    midd1 = length // 2 - 1
    midd2 = length // 2
    print(f"Middle character is: {str[midd1]}{str[midd2]}")
else :
    midd = length // 2
    print(f"Middle character is {str[midd]}")

    