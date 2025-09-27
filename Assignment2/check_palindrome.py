"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take a string input.
Check if the string is a palindrome (ignore case).
Print "Palindrome" or "Not Palindrome".

sample input:
Enter a string: Madam

sample output:
Palindrome

"""

strng = input("Enter a string: ")

if strng == strng[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    