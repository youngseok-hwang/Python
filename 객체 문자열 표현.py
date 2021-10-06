class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn
    def __repr__(self):
        return "ISBN: " + self.__isbn + "; TITLE: " + self.__title

book = Book("The Python Tutorial", "0123456")
print(book)

# 클래스 관계

class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

dog1 = Dog("DOG1")
person1 = Person("홍길동")
person1.pet = dog1
