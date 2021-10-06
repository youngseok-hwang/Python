# copy 모듈

# 얇은 복사(shallow copy): 객체의 참조값만 복사하고 객체 자체는 공유 => 객체(참조값1 = 참조값2)
# 깊은 복사(deep copy): 객체까지 복사 => 객체1 참조값1, 객체2 참조값2
import sys

colors = ['red', 'blue', 'green']
clone = colors
clone[0] = 'white'
print(colors)
print(clone)
# clone의 리스트 항목을 white로 바꾸니 colors의 항목도 변경되었다.
# 따라서 얇은 복사에 해당된다.

import copy

colors = ['red', 'blue', 'green']
clone = copy.deepcopy(colors)

clone[0] = 'white'
print(clone)
print(colors)
# 객체1(colors) 참조값1('red', 'blue', 'green'), 객체2(clone) 참조값2('white', 'blue', 'green')
# 로 복사된 객체를 수정하여도 참조값이 서로 영향을 받지 않고 독립적으로 작용한다.
# 따라서 깊은 복사에 해당된다.

# keyword 모듈
import keyword

name = input("변수 이름을 입력하시오: ")

if keyword.iskeyword(name):
    print(name, "은 예약어입니다.")
    print("아래는 키워드의 전체 리스트입니다.")
    print(keyword.kwlist)
else:
    print(name, "은 사용가능한 변수 이름입니다.")

# 랜덤 모듈

import random
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))

print(random.random()*100)

myList = ["red", "green", "blue"]
print(random.choice(myList))

# shuffle() 리스트의 항목을 랜덤하게 섞음

myList = [[x] for x in range(10)]
random.shuffle(myList)
print(myList)

# randrange(start, stop[, step]) - range(start, stop, step) 구간으로 랜덤하게 요소를 생성

for i in range(3):
    print(random.randrange(0, 101, 3))
# 3의 배수 중 아무거나 0~101 사이 1가지 고르는 것을 3번 반복

# OS 모듈, 운영체제에 관계없이 운영체제의 기본적인 기능들을 다룰 수 있게 해주는 모듈

import os
os.system("calc")
# 계산기 실행

# os.getcwd(), os.chdir(path - 바꾸려는 경로)는 현재 작업 디렉터리 위치를 변경하거나 가져올 때 사용

# os.listdir(path)는 해당 경로에 존재하는 파일과 디렉터리들을 리스트로 만들어서 반환
# os.mkdir(path)는 path에 들어가는 이름으로 디렉터리를 생성

# sys 모듈, 파이썬 인터프리터에 대한 다양한 정보를 제공

# sys.prefix 파이썬이 설치된 경로 확인
# sys.modules 설치되어있는 모듈을 확인
# sys.exit() 인터프리터 종료
# sys.path 모듈을 참조할 때 사용하는 경로를 확인
# sys.version 설치된 파이썬의 버전 확인

import time
print(time.time())

# 프로그램이 실행되는데 걸리는 시간 측정
start = time.time()
end = time.time()
print(end-start)

# 피보나치 수열을 계산하는데 걸리는 시간
import time
def fib(n):  # 피보나치 수열 출력
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()

start = time.time()
fib(1000)
end = time.time()
print(end - start)

import time

a = time.asctime()
print(a)
# 현재 날짜와 시간 출력

t = (2021, 7, 11, 2, 20, 59, 6, 0, 0)
b = time.asctime(t)
print(b)
# 특정 날짜와 시간 출력
# 연도 월 일 시 분 초 요일(0~6까지 월~일을 담당)

c = time.localtime()
print(c)
# 현재 날짜와 시간을 튜플 객체 형태로 반환
# 따라서, 각 튜플을 추출하여 사용 가능하다.

localt = time.localtime()
year = localt[0]
month = localt[1]
day = localt[2]
hour = localt[3]
min = localt[4]
sec = localt[5]
DoW = localt[6]
print(hour, ":", min)

# sleep()은 동작 중인 프로세스를 지정된 시간(초)만큼 정지 시킨다. 프로그램을 천천히 실행하고자 할 때 사용

import time
for i in range(10, 0, -1):
    print(i, end="\n")
    time.sleep(1)
print("발사!")

# calendar 모듈, 여러 가지 형태의 달력을 출력할 수 있다.
import calendar

cal = calendar.month(2021, 7)
print(cal)