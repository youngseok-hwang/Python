import random

menu = int(input("버튼을 누르세요 초급은 1, 중급은 2, 고급은 3, 종료는 0: "))
if menu == 1:
    board = [[False for x in range(10)] for y in range(10)]   # 부울형의 2차원 리스트 형성

    for r in range(10):
        for c in range(10):
            if (random.random() < 0.25):                      # 난수 발생 25% 확률로 지뢰 저장
                board[r][c] = True

    for r in range(10):                                       # 게임판 출력
        for c in range(10):
            if board[r][c]:
                print("# ", end="")
            else:
                print(". ", end="")
        print()

elif menu == 2:
    board = [[False for x in range(15)] for y in range(15)]

    for r in range(15):
        for c in range(15):
            if (random.random() < 0.3):
                board[r][c] = True

    for r in range(15):
        for c in range(15):
            if board[r][c]:
                print("# ", end="")
            else:
                print(". ", end="")
        print()

elif menu == 3:
    board = [[False for x in range(20)] for y in range(20)]

    for r in range(20):
        for c in range(20):
            if (random.random() < 0.3):
                board[r][c] = True

    for r in range(20):
        for c in range(20):
            if board[r][c]:
                print("# ", end="")
            else:
                print(". ", end="")
        print()

else:
    print("종료")