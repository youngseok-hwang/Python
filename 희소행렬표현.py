matrix = {(1, 2): 1, (2, 2,): 2, (3, 2): 3}      # (행:열)의 위치 좌료를 '키'로 지정하고 '값'을 표현한 방식
for y in range(5):
    for x in range(5):
        print(matrix.get((y,x), 0), end = " ")   # 행렬의 크기를 정하고 위치좌표가 지정되지 않은 '키' 는 '값'을 '0'으로 표현
    print()
