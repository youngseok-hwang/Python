Puppylist = []
while True:
    name = input("강아지의 이름을 입력하시오(종료는 엔터키): ")
    if name == '' \
               '':
        break
    Puppylist.append(name)


print("강아지들의 이름:")
for name in Puppylist:
    print(name, end = ", ")