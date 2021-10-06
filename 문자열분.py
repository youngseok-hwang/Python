
sentence = input("문자열을 입력하시오: ")

table = {"Alphabet": 0, "Digits": 0, "Spaces": 0}

for i in sentence:
    if i.isalpha():
        table["Alphabet"] += 1
    if i.isdigit():
        table["Digits"] += 1
    if i.isspace():
        table["Spaces"] += 1

print(table)