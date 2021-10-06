
# 첫 번째 요소를 최소값 minimum이라고 가정

# for i in range(1, 리스트 크기):
#     if (s[i] < minimum)
#         minimum = s[i]
# 반복이 종료되면 minimum에 최소값이 저장된다.

prices = [100, 10, 9, 2, 3, 5, 99]               # 가장 싼 가격 찾기
cheapest = prices[0]
for i in range(1, len(prices)):
    if prices[i] < cheapest:
        cheapest = prices[i]
print("가장 싼 가격은", cheapest)

words = ["cat", "mouse", "tiger", "lion"]        # 가장 짧은 단어 찾기
shortest = words[0]
for i in range(1, len(words)):
    if len(words[i]) < len(shortest):
        shortest = words[i]
print("가장 짧은 단어", shortest)

list1 = ["white", "silver", "blue", "red", "black"] # index 메소드를 사용한 항목 찾기: 탐색
print(list1.index("red"))

# def linearSearch(aList, key):                     # 탐색 알고리즘
#     for i in range(len(aList)):
#         if key == aList[i]
#                탐색 성공이고 복귀한다.
#      복귀하지 않고 반복 루프가 종료되었으면 탐색실패이다.

def linearSearch(aList, key):
    for i in range(len(aList)):          # 리스트의 길이만큼 반복한다.
        if key == aList[i]:              # 키가 발견되면 i를 반환하고 종료한다.
                    return i
    return -1                            # 키가 발견되지 않고 반복이 종료되었으면 -1을 반환한다.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

position = linearSearch(numbers, 80)

if position != -1:
    print("탐색 성공 위치 =", position)
else:
    print("탐색실패!")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]  # 50 넘는 숫자 전부 result에 넣고 출력하기
result = [ ]
for value in numbers:
    if value > 50:
        result.append(value)
print(result)


data = [ ]
f = open("C:\Temp\data.txt", "r")

# 파일에 저장된 모든 줄을 읽는다.
for line in f.readlines():
    # 줄바꿈 문자를 삭제한 후에 리스트에 추가한다.
    data.append(line.strip())

print(data)


a = [3, 2, 1, 5, 4]
a.sort()
print(a)

# 선택 정렬을 구현하는 함수
def selectionSort(aList):
    for i in range(len(aList)): # 리스트의 모든 요소에 대하여 반복
        least = i               # i번째 요소를 최소값이라고 가정
        leastValue = aList[i]

        for k in range(i+1, len(aList)):
            if aList[k] < leastValue:     # k번째 요소가 현재의 최소값보다 작으면
                least = k
                leastValue = aList[k]
        tmp = aList[i]                    # 1번째 요소와 최소값을 교환한다.
        aList[i] = aList[least]           # tmp 등 여러 가지 할당할 필요가 없다. 지워도 무방하다.
        aList[least] = tmp                # 지워도 무방하다.

    list1 = [7, 9, 5, 1, 8]
    selectionSort(list1)
    print(list1)



