
fname = input("파일 위치: ")
file = open(fname, "r")

table = dict()
for line in file:
    words = line.split()       # 각 줄을 단어들의 리스트로 분리
    for word in words:
        if word not in table:  # 단어가 딕셔너리에 없으면 +1 추가
            table[word] = 1
        else:
            table[word] += 1   # 단어가 이미 딕셔너리에 있으면 +1씩 추가
print(table)

