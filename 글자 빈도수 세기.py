
string = input("문자열을 입력하시오: ")

countTable = {}
for letter in string:
    countTable[letter] = countTable.get(letter, 0) + 1
    letter_items = list(countTable.items())  # 키, 값 쌍으로 추출하기
    print(letter_items)
    letter_items.sort()

