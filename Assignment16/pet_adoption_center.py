class Pet:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__adopted = False

    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def adopt_pet(self):
        self.__adopted = True

    def is_adopted(self):
        return self.__adopted
    
    def get_name(self):
        return self.__name


class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print("Woof")


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self):
        print("Meow")


class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_details(self):
        print(f"Name: {self.name}, Phone: {self.phone_number}")


dog = Dog("Buddy", 3)
cat = Cat("Luna", 2)

person1 = Person("Anita", "9999999210")
dog.get_info()
cat.get_info()

dog.adopt_pet()
print(f"Is {dog.get_name()} adopted? {dog.is_adopted()}")
print(f"Is {cat.get_name()} adopted? {cat.is_adopted()}")