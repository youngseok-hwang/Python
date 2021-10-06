for i in [1, 2, 3, 4]:
    print(i, end=" ")

for c in "python":
    print(c, end=" ")

class MyCounter(object):
    # 생성자 메소드를 정의한다.
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # 이터레이터 객체로서 자신을 반환한다.
    def __iter__(self):
        return self

    def __next__(self):
        # current가 high 보다 크면 StopIteration 예외를 발생한다.
        # currnet가 high 보다 작으면 다음 값을 반환한다.
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

c = MyCounter(1, 10)
for i in c:
    print(i, end=" ")

def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'

for word in myGenerator():
    print(word)

def MyCounterGen(low, high):
    while low <= high:
        yield low
        low += 1
for i in MyCounterGen(1, 10):
    print(i, end = ' ')

def addNumber(fixedNum):
    def add(number):
        return fixedNum + number
    return add

func = addNumber(10)  # 10을 고정된 숫자로 지정
print(func(30))       # 해당하는 함수에 또 다른 함수 add로 숫자를 추가하여 더함


