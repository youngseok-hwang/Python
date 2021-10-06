colors = ("red", "green", "blue")  # 색깔 튜플
print(colors)

numbers =(1, 2, 3, 4, 5)  # 정수 튜플
print(numbers)

t = (1, 2, "hello!")     # 여러 자료형 섞어서 튜플 만들기 가능
print(t)

t = ()  # 공백 튜플
print(t)

t = (10, )   # 하나의 값만을 가진 튜플 생성, ','이 없으면 정수로 처리
print(t)

t = tuple ([1, 2, 3, 4, 5])  # 리스트로부터 튜플 생성 가능
print(t)

t = (1, 2, "hello!")
u = t, (1, 2, 3, 4, 5)
print(u)                    # 튜플 내부에 튜플 가지기 가능

numbers = (1, 2, 3, 4, 5)
a = len(numbers)
b = max(numbers)
c = min(numbers)
print(a, b, c)

numbers = (1, 2, 3, 4, 5)
colors = ("red", "green", "blue")
t = numbers + colors
print(t)                  # 튜플은 요소 변경이 불가능하지만 2개를 더해서 만드는 건 가능

a = len((1, 2, 3))  # 튜플 길이
print(a)
b = (1, 2, 3) + (4, 5, 6)  # 접합
print(b)
c = ("Hi!") * 4      # 해당 튜플 곱해서 접합
print(c)
d = 3 in (1, 2, 3)   # 3이 튜플 속에 있냐?
print(d)             # 있다.
for x in (1, 2, 3):  # 차례대로 끝날 때까지 반복
    print(x)

L = ("apple", "banana", "strawberry")
print(L[1])   # 인덱스 왼쪽에서부터 2번째 (인덱스는 0부터 시작)
print(L[-2])  # 인덱스 오른쪽에서부터 2번째
print(L[1:])  # 인덱스 1부터 끝까지

t1 = "physics", "chemistry", "c language"
t2 = 1, 2, 3, 4, 5
t3 = "a", "b", "c", "d"
t4 = [1, 2, 3, 4, 5]
t5 = 2, 3, 4, 5, 6
t6 = 0, 2, 5, 4, 5

def cmp(x, y):
    if x > y:
        print(-1)
    elif x == y:
        print(0)
    elif x < y:
        print(1)
    else:
        print("CAN'T CALC")

a = cmp(4, 5)
c = cmp(t2, t6)
len(t1)
b = tuple(t4)
print(b)
b = list(b)
print(b)

student1 = ("철수", 19, "CS")      # 튜플 대입 연산
(name, age, major) = student1
print(name)
print(age)
print(major)

Jururu = ("주르르", "97년생", "아마도 여자", "학생이자 방송인", "발로란트")
(name, birth_year, gender, job, favorite_game) = Jururu
print("기미노나마에와?", name)
print("태어난 연도는?", birth_year)
print("성별은?", gender)
print("직업은?", job)
print("가장 좋아하는 게임은?", favorite_game)

temp = x = 0
print(x)
y = 1
x = y
print(x)
y = temp
print(y)

b = (x, y)
print(b)
a = (x, y) = (y, x)    # 위치 바꿔치기
print(a)


