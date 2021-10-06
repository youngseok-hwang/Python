shopping_list = ["두부", "양배추", "딸기", "사과", "토마토"]
print(shopping_list[0])

item = shopping_list[1]
print(item)

item = shopping_list[-1]  # -1은 제일 마지막, -len(shopping_list) = -5는 제일 처음 요소를 지칭
print(item)

print(shopping_list[-len(shopping_list)])


squares = [0, 1, 4, 9, 16, 25, 36, 48]
a = squares[1:6]  # 슬라이싱은 새로운 리스트를 반환한다.
print(a)          # 인덱스는 0부터 순서를 센다. 0 1 2 3 4 5 6 7

b = squares[:3]   # 끝에 인덱스 2를 부르고 싶으면 해당 인덱스에 +1하여 지정한다.
c = squares[3:]
print(b)
print(c)

d = squares[0:len(squares)] # 처음과 끝의 인덱스는 0과 리스트의 크기와 같다.
print(d)

squares = [0, 1, 4, 9, 16, 25, 36, 48]
e = 7**2
squares[7] = e              # 리스트는 언제든지 변경 가능하다.
print(squares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E'] # 리스트 일부를 변경
print(letters)
letters[2:5] = []              # 리스트 일부를 삭제
print(letters)

marvel_heroes = ["스파이더맨", "헐크", "아이언맨"]
dc_heroes = ["슈퍼맨", "배트맨", "원더우먼"]
heroes = marvel_heroes+dc_heroes    # 두 개의 리스트 합병시 + 연산자 사용
print(heroes)

value = [1, 2, 3] * 3               # 리스트 반복시 * 연산자 사용
print(value)
value = 3 * [1, 2, 3]               # 반대로 곱해도 결과값은 같다.
print(value)

letters = ['a', 'b', 'c', 'd']      # 리스트 길이
f = len(letters)
print(f)

shopping_list = []                  # 새로운 항목을 끝에 추가
shopping_list.append("두부")
shopping_list.append("양배추")
shopping_list.append("딸기")
print(shopping_list)

shopping_list.insert(1, "생수")     # 특정 인덱스 위치에 추가하는 메소드 .insert()
print(shopping_list)               # 추가될 때 지정한 인덱스의 뒤에 있던 목록은 뒤로 밀린다.

heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
if "배트맨" in heroes:              # 리스트에 요소가 있는지 확인하는 방법 in
    print("영웅 중에는 배트맨도 있습니다.")

index = heroes.index("슈퍼맨")      # 특정 요소의 인덱스를 알고자 할 때
print(index)

if "배트맨" in heroes:              # 특정 요소가 있는지 확인 후 인덱스 번호를 알아낸다.
    index = heroes.index("배트맨")  # 있는지 없는지 확인하지 않았을 때 만약 없다면 오류가 발생한다.
    print(heroes[index])

print(heroes)
heroes.pop(1)                      # 특정위치의 요소를 삭제한다.
print(heroes)

heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이펀맨", "조커"]
heroes.remove("조커")              # pop()은 인덱스로 항목을 정하는 반면, remove()는 직접 항목을 정하는 점에서 다르다.
print(heroes)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
a = list1 == list2    # ==는 같은지 확인하는 연산자이다.
print(a)              # 리스트 길이가 다르거나 리스트 항목이 다를 경우 False가 뜬다.

list3 = [4, 5, 6]
b = list1 < list3
print(b)              # 각 항목이 큰지 작은지 비교하여 맞는 명제면 True가 뜬다.

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = min(values)
d = max(values)
print(c)
print(d)

a = [3, 5, 1, 4, 2]
a.sort()
print(a)

a = [3, 5, 1, 4, 2]
b = sorted(a)
print(a)
print(b)

e = sorted("A picture is worth a thousand words.".split(), key=str.lower)     # 대 소문자 가리는 것없이 배열하는 것
print(e)

f = sorted([3, 5, 1, 4, 2], reverse=False)      # False는 역순을 부정한다는 뜻으로로 순서대로 나열된다.
g = sorted([3, 5, 1, 4, 2], reverse=True)       # True는 역순 그대로 나열한다.
print(f)
print(g)

str = "Where there is a will, there is a way."
h = str.split()                                 # 문자열 쪼개기
print(h)



