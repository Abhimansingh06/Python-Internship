"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 11 **********************************

Problem statement:
Write a function that takes three sides of a triangle as input and performs the following tasks:
1. Check if the sides form a valid triangle.
2. Classify the triangle as one of the following types (if valid):
    Equilateral - All sides are equal
    Isosceles - Two sides are equal
    Right angled - Follows the Pythagorean Theorem
    Scalene - All sides are different
3. If the triangle is valid and right-angled, compute and print the radius of the circumcenter.
Otherwise, print -1.


sample input:
a = 3
b = 4
c = 5

sample output:
output:
valid
Rightangled
2.5

"""

def classify_triangles(p,b,h):
    if p > b:
        temp = p
        p = b
        b = temp

    if b > h:
        temp = b
        b = h
        h = temp

    if p + b <= h:
        print("-1")
        return
    else:
        print("Valid")

    if p == b == h:
        print("Equilateral")
    elif p == b or p == h or b == h:
        print("Isoscles")
    else:
        print("Scalene")

    if p * p + b * b == h * h:
        print("Right angled")
        print("Radius of circumcenter is", h/2)

p = int(input("Enter 1st side: "))
b = int(input("Enter 2nd side: "))
h = int(input("Enter 3rd side: "))

classify_triangles(p,b,h)