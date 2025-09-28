"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
Given a list of products where each product is represented as a dictionary with keys "name" and "price",
write a Python function to print the names of all products that have a price greater than 10.

sample input:
products = [
    {'name': 'orange', 'price': 20},
    {'name': 'apple', 'price': 8},
    {'name': 'banana', 'price': 10},
    {'name': 'kiwi', 'price': 30}
]

sample output:
kiwi
orange
"""

def expensive_products(products):
    for i in products:
        if i['price'] > 10:
            print(i['name'])

products = [
    {'name': 'orange', 'price': 20},
    {'name': 'apple', 'price': 8},
    {'name': 'banana', 'price': 10},
    {'name': 'kiwi', 'price': 30}
]
expensive_products(products)
