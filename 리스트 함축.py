S = [x**2 for x in range(10)]       # 리스트 함축은 수학 집합과 비슷하다.

for element in S:
    print(element, end=" ")

squares = []                        # 위 함수와 동일하게 만들기
for x in range(10):
    squares.append(x**2)
for element in squares:
    print(element, end=" ")


#old_list = [1]
#new_list = []
#for i in old_list:
#   if filter(i):
#       new_list.append(expression(i))


list1 = [3, 4, 5]                   # 새로운 리스트 만들기
list2 = [x*2 for x in list1]
print(list2)
list3 = [x**2 for x in list2]
print(list3)
list4 = [x**2 for x in list3]
print(list4)


M = [x for x in range(1, 13) if x % 2 == 0] # 조건식을 추가한 리스트 함축 - 2로 나눴을 때 0이 되는 숫자 -> 2의 배수
print(M)

list1 = ["All", "good", "things", "must", "come", "to", "an", "end."]  # 각 리스트 요소 글자의 첫 문자 추출하기
items = [word[0] for word in list1]
print(items)

word_list = 'Doncount your chickens before they are hatched'.split()  # 각 요소의 문자의 개수를 len()을 통해서 구했다.
result_list = [len(w) for w in word_list]
print(result_list)                                                    # 각 요소의 숫자를 자동으로 계산하는 방법은 없을까?

colors = ["white", "silver", "black"]                                 # 리스트 짝지어서 튜플 만들기
cars = ["bmw5", "sonata", "malibu", "sm6"]
colored_cars = [(x, y) for x in colors for y in cars]
for car in colored_cars:
    print(car, end=" ")