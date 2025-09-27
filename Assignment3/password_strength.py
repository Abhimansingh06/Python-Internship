"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take a string input as password. Check for the following conditions using loop and conditional:

1. Must be at least 8 characters.
2. Must contain at least 1 uppercase letter.
3. Must contain at least 1 digit.
4. Must contain at least 1 special character (@, #, $, %, etc.)

use only loop and conditional statements, and string and it's methods.

sample input:
Enter a password: Abcdef1@
Enter a password: abcdefgh

sample output:
Valid Password
Invalid Password
"""


word = input("Enter a password: ")

is_upper = 0
is_digit = 0
is_special = 0
special_char = "!@#$%&*"

for i in word:
    if i >= 'A' and i <= 'Z':
        is_upper += 1
    elif i >= '0' and i <= '9':
        is_digit += 1
    elif i in special_char:
        is_special += 1

if len(word) >= 8 and is_upper > 0 and is_digit > 0 and is_special > 0:
    print("Valid password")
else:
    print("Invalid password")

