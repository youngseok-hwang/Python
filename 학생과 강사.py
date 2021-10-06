# Person 클래스를 이어받는 Student 클래스와 Teacher 클래스 정의

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 1

    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa=0
        self.classes = []
    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return "\n이름="+self.name+"\n주민번호="+self.number+\
            "\n수강과목="+str(self.classes)+"\n평점="+str(self.gpa)

class Teacher(Person):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.courses=[]
        self.salary=3000000

    def assignTeaching(self, course):
        self.courses.append(course)

    def __str__(self):
        return "\n이름="+self.name+"\n주민번호="+self.number+\
            "\n강의과목="+str(self.courses)+"\n월급="+str(self.salary)

hong = Student("홍길동", "12345678", Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수", "987654321")
kim.assignTeaching("Python")
print(kim)

