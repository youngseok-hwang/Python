numbers = {2, 3, 1}
print(numbers)
print(len(numbers))

fruits = {"Apple", "Banana", "Pineapple"}
mySet = {1.0, 2.0, "Hello World!", (1, 2, 3)}
print(fruits)
print(mySet)

cities = {"Paris", "Seoul", "London", "Berlin", "Paris", "Seoul"}
print(cities)

numbers = set() # 비어있는 세트 만들기

numbers = {2, 3, 1}
n = int(input("확인하고 싶은 숫자를 입력하십시오: "))
if n in numbers:
    print("집합 내에 %d가 존재합니다." %n)
elif n not in numbers:
    print("집합 내에 %d가 존재하지 않습니다." %n)

numbers = {2, 1, 3}
for x in sorted(numbers):
    print(x, end = " ")

a = set([1, 2, 3])
print(a)

b = sorted(set("abcdedfa")) # 순서대로 정렬은 sorted(), 중복은 안되기 때문에 a는 하나만 포함되었다. 정렬하면 리스트로 변한다.
print(b)

for char in set("banana"): # 요소 반복 작업, banana에서 반복되는 요소 뽑아내는 것은 char이다.
    print(char)

numbers = {3, 2, 3, 1}      # 추가
numbers.add(4)
print(numbers)

numbers.update([2, 3, 4, 5])   # 추가
print(numbers)

numbers.discard(5)      # 삭제
print(numbers)

numbers.clear()    # 세트 크기 0 만들기
print(numbers)

A = {1, 2, 3}
B = {1, 2, 3}
a = A == B
b = A != B
print(a)
print(b)

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
a = B < A
print(a)

A = {1, 2, 3, 4, 5}
b = {1, 2, 3}
A.issuperset(B)      # A가 B의 상위집합인지 검사
B.issubset(A)        # B가 A의 부분집합인지 검사

mySet = set("banana")   # 요소 포함되어 있는지 확인
a = 'a' in mySet
print(a)
b = 'p' not in mySet
print(b)

A = {1, 2, 3}
B = {3, 4, 5}

a = A|B   # 합집합
print(a)
b = A.union(B)
print(b)
c = B.union(A)
print(c)

a = A & B   # 교집합
b = A.intersection(B)
print(a)
print(b)

a = A - B   # 차집합
b = A.difference(B)
print(a)
print(b)

