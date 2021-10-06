
list = [(x, y, z) for x in range(1,30) for y in range(1, 30) for z in range(1, 30) if x**2 + y**2 == z**2]  # x^2 + y^2 = z^2라면 x, y, z 성분 뽑아내기
for element in list:
    print(element, end = " ")

new_list = []
for x in range(1, 30):
    for y in range(1, 30):
        for z in range(1, 30):
            if x**2 + y**2 == z**2:
                new_list.append((x, y, z))                                                                 # 위와 동일한 내용

print(new_list)

