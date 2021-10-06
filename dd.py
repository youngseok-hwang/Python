from random import *

kind = [" ", "가위", "바위", "보"]
man = int(input("<1.가위 2.바위 3.보>:"))
computer = choice([1, 2, 3])

print("사람:", kind[man], "컴퓨터:", kind[computer])

if man - computer == 0:
    print("서로 비겼습니다")
elif man - computer in [-2, 1]:
    print("사람이 이겼습니다.")
else:
    print("컴퓨터가 이겼습니다")
