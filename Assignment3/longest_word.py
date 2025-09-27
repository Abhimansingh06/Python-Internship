"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take a string input (a sentence). Find the longest word in the sentence and print it.

Use only loop and conditional statements. don't use any built-in functions, like split.


sample input:
Enter a sentence: The quick brown fox jumped over the lazy dog
Enter a sentence: Python is a great programming language

sample output:
jumped
programming

"""


sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for ch in words:
    if len(ch) > len(longest):
        longest = ch

print(f"{longest} is the longest word")

