"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to return a dictionary with the count of each character in the given sentence.

sample input:
"apple"

sample output:
{
    'a': 1,
    'p': 2,
    'l': 1,
    'e': 1
}
"""

def count_character(sentence):
    word = {}
    for i in sentence:
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    return word

sentence = input("Enter sentence: ")
res = count_character(sentence)
print(res)
