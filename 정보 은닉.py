
class Student:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

obj = Student("Hong", 20)
obj.age = 21
print(obj.age)

class Student:
    def __init__(self, name = None, birthday = "20010301"):
        self.name = name
        self.birthday = birthday

class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age

obj = Student()
# print(obj.__age) => private 변수는 클래스 내부에서만 접근 가능하기에 오류 발생

