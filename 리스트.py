# scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

# scores = []
# for i in range(10):
#    scores.append(int(input("성적을 입력하라:")))
# print(scores)

# scores[0] = 80
# scores[1] = scores[0]

# i = 3

# if i >= 0 and i < len(scores) :
#    scores[i] = number = 10

# scores[i] = 10         # i는 정수 변수
# scores[i+2] = 20       # 수식이 인덱스가 된다.

# print(scores[i])
# print(i)
# print(number)
# print(scores[i+2])


scores = []

#i = 10
#for i in range(i+10):           # range의 범위를 미리 정해놓았다면, 처음 i를 10으로 정의했을 때 i는 0부터 시작한다.
#    scores.append((i+1)*10)

#for i in range(len(scores)):
#    print(i, scores[i])

                                # range가 정해져있고 i가 정의되어있지 않다면, i = 0부터 시작한다. i는 지역변수이자 인덱스가 된다.
#for i in range(10):
#    scores.append((i+1)*10)

#for i in range(len(scores)):
#    print(i, scores[i])


# scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


#for element in scores:
#    print(element)

list1 = list()            # 공백리스트 생성
list2 = list("Hello")     # 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
list3 = list(range(0, 5)) # 0, 1, 2, 3, 4를 요소로 가지는 리스트 생성
print(list1, list2, list3)

list1 = []
list2 = ["H", "e", "l", "l", "o"]
list3 = [0, 1, 2, 3, 4]
print(list1, list2, list3)

list1 = [12, "dog", 180.14]                             # 혼합 자료형
list2 = [["Seoul", 10], ["Paris", 12], ["London", 50]]  # 내장리스트
list3 = ["aaa", ["bbb",["ccc", ["ddd", "eee", 45]]]]    # 내장리스트
print(list1, list2, list3)
