
table = {"B4": "Before",
         "Tx": "Thanks",
         "BBL": "Be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have a Nice Day"}

message = input("번역할 문장을 입력하시오: ")
words = message.split()
result = ""
for word in words:
    if word in table:   # 단어가 딕셔너리에 있으면 딕셔너리의 내용을 출력한다.
        result += table[word] + " "
    else:
        result += word

print(result)
