"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
You are given a list of votes (each vote is represented by a candidate's name). 
Each element in the list represents a vote cast for a candidate.
Write a Python function to determine the winner, i.e., the candidate who received the most votes.

sample input:
votes = [
    "Alice",
    "Bob",
    "Alice",
    "Charlie",
    "Bob",
    "Alice"
]

sample output:
Alice # because she received the most votes
"""

def find_winner(votes):

    vote_count = {}
    for i in votes:
        if i in vote_count:
            vote_count[i] += 1
        else:
            vote_count[i] = 1

    max_votes = 0
    
    for i in vote_count:
        if vote_count[i] > max_votes:
            max_votes = vote_count[i]
            winner = i

    print("winner is", winner)
votes = ["Alice","Bob","Alice","Charlie","Bob","Alice"]

find_winner(votes)
