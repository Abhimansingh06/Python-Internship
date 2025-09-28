"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Create a class called Student with the following requirements:
- data members (attributes) (Initialized using __init__)
    name (str)
    roll_no (int)
    marks (dict): A dictionary where keys are subject names and values are marks (e.g., {"Math": 85, "English": 78})

    
- Methods to Implement
    1. display_info(self): Prints the student's name and roll number.
    2. add_mark(self, subject: str, mark: int): Adds or updates the mark for a given subject.
    3. calculate_average(self): Returns the average of all subject marks.
    4. get_grade(self): Returns the grade based on the average mark:
        90+ → "A"
        75-89 → "B"
        60-74 → "C"
        Below 60 → "D"
"""

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")

    def add_mark(self, subject, mark):
        self.marks[subject] = mark
        print(f"Mark added for {subject}: {mark}")

    def calculate_average(self):
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        else:
            return "D"



student_object = Student("xyz", 1)
student_object.display_info()

student_object.add_mark("Maths", 85)
student_object.add_mark("Physics", 95)
student_object.add_mark("Chemistry", 90)

avg = student_object.calculate_average()
grade = student_object.get_grade()

print(f"Average marks is: {avg}")
print(f"Grade is: {grade}")