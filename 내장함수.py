a = abs(-3)
b = abs(3 + 4j)

print(a, b)

def all(iterable):
    for element in iterable:
        if not element:   # 요소가 참이 아닌 것이 있다면
            return False  # 결과값은 거짓
    return True           # 거짓이 아니라면 참

def any(iterable):
    for element in iterable:
        if element:      # 요소가 참인 것이 있다면
            return True  # 결과값은 참
    return False         # 참이 아니라면 거짓

items = ["", "a string", 0, 1, [], {}]
for i in items:
    print(i, bool(i))

# 값이 비어있으면 거짓, 값이 있으면 참, 0은 거짓, 1은 참, None은 거짓

c = chr(65)  # 아스키코드(0 ~ 255)를 문자열로 변환
print(c)

d = ord('A') # 문자열을 아스키코드 값으로 변환
print(d)

x = complex(4, 2)
print(x)

e = dir([1, 2, 3])
print(e)

f = help([1, 2, 3].append)

g = divmod(10, 3)
print(g)

h = 10//3
i = 10%3
print((h, i))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
j = list(enumerate(seasons))
print(j)

for i, str in enumerate(["aaa", "bbb", "ccc"]):
    print(i, str)

k = eval("1+2");
print(k)
eval("print('Hi!')")

exp = input("파이썬의 수식을 입력하시오: ")
print(eval(exp))

x = 10
y = 5
print(eval('x+y'))

exec('y=2+3')  # 값을 반환하지 않음
print(y)

statements = '''
import math
def area_of_circle(radius):
    return math.pi * radius**2
'''

exec(statements)
print(area_of_circle(5))

code_obj = compile("print(x)", "<string>", "exec")

str = input("실수를 입력하시오: ")

value = float(str)
print(value)

l = len([1, 2, 3, 4, 5, 6, 0])
print(l)

m = list("python")
print(m)

values = [1, 2, 3, 4, 5]
n = max(values)
o = min(values)
print(o, n)

p = max('abc', 'def', 'ghi', 'jkl')
print(p)

q = list(range(5))
print(q)

r = sorted([5, 2, 3, 1, 4])
print(r)

s = sum(r)
print(s)