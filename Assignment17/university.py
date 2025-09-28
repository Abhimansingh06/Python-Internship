from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    @abstractmethod
    def display_details(self):
        pass

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

class Student(Person):
    def __init__(self, name, email, roll_no):
        super().__init__(name, email)
        self.__roll_no = roll_no

    def display_details(self):
        print(f"Name - {self.get_name()}, E-mail - {self.get_email()}, Roll No - {self.__roll_no}")

    def get_roll_no(self):
        return self.__roll_no

class Professor(Person):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.__employee_id = employee_id

    def display_details(self):
        print(f"Name - {self.get_name()}, Email - {self.get_email()}, Employee ID - {self.__employee_id}")

    def get_employee_id(self):
        return self.__employee_id


class Course:
    def __init__(self, course_code, title):
        self.__course_code = course_code
        self.__title = title
        self.__students = []
        self.__professor = None

    def add_student(self, student: Student):
        self.__students.append(student)

    def assign_professor(self, professor: Professor):
        self.__professor = professor

    def get_course_summary(self):
        print(f"Course Code: {self.__course_code}")
        print(f"Title: {self.__title}")

        if self.__professor:
            print(f"Professor: {self.__professor.get_name()} ({self.__professor.get_email()})")
        else:
            print("Professor not Assigned")

        print("Enrolled Students:")
        if self.__students:
            for s in self.__students:
                print(f"- {s.get_name()} ({s.get_roll_no()})")
        else:
            print("Students not Enrolled")


class Department:
    def __init__(self, name):
        self.__name = name
        self.__courses = []

    def add_course(self, course: Course):
        self.__courses.append(course)

    def list_courses(self):
        print(f"Department: {self.__name}")
        print("Courses Offered:")
        for c in self.__courses:
            print(f"- {c.Coursetitle} ({c._Course_course_code})")


cs_dept = Department("Computer Science")
std1 = Student("Alice", "alice@gmail.com", "CS101")
std2 = Student("Bob", "bob@gmail.com", "CS102")
p1 = Professor("Dr. Smith", "smith@example.com", "EMP987")

course = Course("CS200", "Data Structure")
cs_dept.add_course(course)

course.assign_professor(p1)
course.add_student(std1)
course.add_student(std2)

course.get_course_summary()
