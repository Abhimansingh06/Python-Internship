class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is__borrowed = False

    def get_info(self):
        print(f"Title : {self.__title}, Author : {self.__author}")
    
    def borrow(self):
        self.__is__borrowed = True

    def is_borrowed(self):
        return self.__is__borrowed
    
class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.__genre = genre

    def get_genre(self):
        return self.__genre
    
class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author,)
        self.__subject = subject

    def get_subject(self):
        return self.__subject
    
class Member:
    def __init__(self, name, mem_id):
        self.name = name
        self.mem_id = mem_id

    def details(self):
        print(f"Name - {self.name}, Member_id - {self.mem_id}")


fictionbook = FictionBook("Harry Potter", "J.K Rowling", "Fantasy")

nonfictionbook = NonFictionBook("A brief story of time", "Stephen Hawkings", "Science")

member = Member("Rahul", "M102")

print("Before borrowing: ")
fictionbook.get_info()
print(f" Genre - {fictionbook.get_genre()}")
print(f"Is Borrowed - {fictionbook.is_borrowed()}")

fictionbook.borrow()
print("After Borrowing: ")
fictionbook.get_info()
print(f" Genre - {fictionbook.get_genre()}")
print(f"Is Borrowed - {fictionbook.is_borrowed()}")