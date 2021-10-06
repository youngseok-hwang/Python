# 정렬

a = [1, 4, 5, 6, 2, 3]   # sorted()는 리스트를 변경하지 않는다.
print(sorted(a))

a.sort()   # sort() 내장함수는 리스트 자체를 변경한다.
print(a)

b = sorted({3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'})
print(b)

# key 매개변수

c = sorted("The health know not of their health, but only the sick".split(), key=str.lower)
print(c)
# 정렬하기 전에 각 요소에 대해 적용되는 함수를 지정할 수 있다.
# 정렬하기 전에(순서를 비교하기 전에) lower() 함수가 호출되어 소문자로 변경한다.

students = [('홍길동', 3.9, 20160303), ('김철수', 3.0, 20160302), ('최자영', 4.3, 20160301)]
d = sorted(students, key=lambda student: student[2]) # 학번을 기준으로 정렬된다.
print(d)

class Student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number
    def __repr__(self):
        return repr((self.name, self.grade, self.number))

students = [Student('홍길동', 3.9, 20160303), Student('김철수', 3.0, 20160302), Student('최자영', 4.3, 20160301)]
e = sorted(students, key=lambda student: student.number)
print(e)
# 클래스로 표현하고 클래스의 인스턴스 변수를 정렬의 기준으로 지정

# 오름차순 정렬과 내림차순 정렬
f = sorted(students, key=lambda Student: Student.grade, reverse=True)
print(f)

# 정렬의 안정성
data = [(1, 100), (1, 200), (2, 300), (2, 400)]
g = sorted(data, key=lambda item: item[0])
# 안정성: 매개변수 key를 이용하여 특정 부분을 정렬하였을 때 나머지 부분은 그대로 유지되는 것을 의미

