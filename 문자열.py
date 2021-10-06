
s1 = str("Hello!")
s2 = "Hello "
s3 = "World!"
print(s2 + s3)

# 0 1 2 3 4 5 각 해당 문자에 인덱스가 부여된다. -6 -5 -4 -3 -2 -1 거꾸로 뒤에서부터 세고 싶을 때는 -를 이용한다.

word = 'abcdef'
a = word[0]
b = word[5]
print(a)
print(b)

c = word[-1]
d = word[-6]
print(c)
print(d)

s = "Hello World"
e = s[0:5]  # Hello를 0부터 추출하고 싶은 단어의 개수까지
print(e)
f = s[-11:-6]  # 띄어쓰기도 포함하여 센다. 따라서 총 11자이기 때문에 처음 숫자가 -11이 된다.
print(f)

word = "Python"
g = word[0:2]
h = word[2:5]
print(g)
print(h)

i = word[:2]
j = word[4:]
print(i)
print(j)

k = word[:1]
l = word[1:]
print(k + l)  # s[:i] + s[i:]는 s와 같다.

m = word[:]  # 모두 생략되면 처음부터 끝까지 불러온다.
print(m)

message = 'See you at noon'
low = message[:5]
high = message[5:]
print(low)
print(high)

reg = "980326"
print(reg[:2], "년")
print(reg[2:4], "월")
print(reg[4:], "일")

word = "Python"
n = word[4:42]
o = word[42:]
print(n)
print(o)

p = 'J' + word[1:]
print(p)
q = word[:2] + 'py'
print(q)

r = "A sound mind in a sound body."
s = len(r)   # 띄어쓰기와 특수기호를 포함하여 센다.
print(s)

s = "Love will find a way"
t = "Love" in s
u = "love" in s
print(t)
print(u)

s = input("문자열을 입력하시오: ")
if 'c' in s:
    print("c가 포함되어 있음")
else:
    print("c가 포함되어 있지 않음")

v = "apple" < "banana"  # apple이 banana보다 알파벳이 사전적으로 앞에 가있기 때문에 apple < banana 형태가 됐을 때 true가 된다.
print(v)

a = input("문자열을 입력하시오: ")
b = input("문자열을 입력하시오: ")
if (a < b):
    print(a, "이 앞에 있음")
elif (a > b):
    print(b, "이 앞에 있음")
else:
    print("동일한 문자")

# 사전적으로 알파벳 순서가 앞에 있는 문자열을 추려낼 수 있다.

s = input("문자열을 입력하시오: ")
for c in s:
    print(c)

s = input("문자열을 입력하시오: ")  # 0이 아닌 1부터 시작해서 2간격씩 띄우고 반복하여 문자를 추출(홀수 번째만 추출)
for i in range(1, len(s), 2):
    print(s[i])
s = "Never put off till tomorrow what you can do today."
c = s.split()
print(c)

s = 'Mississippi'
d = s.split('i')
print(d)

s = "abcdef"    # 문자열이 알파벳으로만 구성되어있는지
e = s.isalpha()
s = "123456"
f = s.isdigit() # 문자열이 숫자로만 구성되어있는지
print(e)
print(f)

s = "abcedf"
g = s.islower()  # 소문자만 있는지 확인
print(g)

s = "ABCDEF"
h = s.isupper()  # 대문자만 있는지 확인
print(h)

s = " "
i = s.isspace()  # 공백만 있는지 확인
print(i)

s = "00000"
j = s.isalnum()  # 숫자 0만 있는지 확인
print(j)

s = input("연도를 입력하시오: ")
if not s.isdigit():
    print("숫자만을 입력해주세요.")
elif len(s) >= 5:
    print("4개의 숫자를 입력해주세요.")
elif len(s) <= 3:
    print("4개의 숫자를 입력해주세요.")

s = input("파이썬 소스 파일 이름을 입력하시오: ")
if s.endswith(".py"):
    print("올바른 파일 이름입니다.")
else:
    print("올바른 파일 이름이 아닙니다.")


