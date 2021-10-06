
# 행 합계 계산하기

s = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
cols = len(s[0])

sum = 0;
for c in range(cols):
    sum = sum + s[1][c]   # 2번째 행의 합을 계산

print(sum)


# 2차원 리스트와 함수

table = [ ]

# 2차원 리스트를 화면에 출력한다.

def printList(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist)):
            print(mylist[row][col], end = " ")
        print()

# 2차원 리스트를 체커보드 형태로 초기화한다.

def init(mylist):
    for row in ramge(len(mylist)):
        for col in range(len(mylist[0])):
            if (row+col)%2 == 0:         # row + col = 짝수면, 1 저장
                table[row][col] = 1

# 2차원 리스트를 생성한다.

for row in range(10):
    table += [[0]*10]                   # 0으로 초기화 된 2차원 리스트

init(table)
printList(table)

