scores = [10, 20, 30, 40, 50]
values = scores              # values와 scores 둘 다 같은 객체를 가르킨다.
                             # 이걸 얕은 복사라고 부른다.
print(values)
print(scores)

values[2] = 200
print(scores)

for element in scores:
    print(element, end=" ")

for element in values:
    print(element, end=" ")

scores = [10, 20, 30, 40, 50]
values = list(scores)       # list()를 통해서 복사를 할 수 있다.
                            # 이걸 깊은 복사라고 부른다.
values[3] = 100
for element in scores:
    print(element, end = ",")
for element in values:
    print(element, end = ",")

from copy import deepcopy   # 내장함수 deepcopy를 이용한 복사 방법이다.
scores = [10, 20, 30, 40, 50]
values = deepcopy(scores)
values[4] = 60
print(values)

