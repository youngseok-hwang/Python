
# 2차원 리스트를 생성한다.

s = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print(s)


rows = 3
cols = 5

s = [ ]

for row in range(rows):        # rows = 3 이기 때문에 0부터 2까지 3번 반복
    s += [[0]*cols]            # [0]*cols는 여기서 [0]*5의 의미와 같아서 [0, 0, 0, 0, 0]을 표현

print("s =", s)


rows = 3
cols = 5
s = [([0] * cols) for row in range(rows)]  # 위와 동일

print(" s =", s)


score = s[2][1]


s = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# 행과 열의 개수를 구한다.

rows = len(s)                    # 행의 개수
cols = len(s[0])                 # 열의 개수

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=",")  # [r]은 행 [c]는 열
    print()

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]           # 리스트 x 안에 리스트 a와 n이 들어있다.

print(x)