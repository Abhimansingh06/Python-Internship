"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Write a function that takes a sentence as input and returns a list of all words that start and end with a vowel.

sample input:
Enter a sentence: apple banana orange avocado
Enter a sentence: umbrella igloo octopus
Enter a sentence: Anna and Eve are outside in India

sample output:
['apple', 'orange', 'avocado']
['umbrella', 'igloo', 'octopus']
['Anna', 'Eve', 'outside', 'in', 'India']
"""

def find_vowel(sentence):
    
    words = sentence.split()
    l = []
    vowels = 'aeiouAEIOU'

    for i in words:
        if i[0] in vowels and i[-1] in vowels and len(words) > 1:
            l.append(i)

    return l

sentence = input("Enter a sentence: ")
res = find_vowel(sentence)
print(f"List of words that start and end with vowels are: {res}")

