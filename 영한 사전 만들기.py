
english_dict = dict()
english_dict["one"] = "하나"   # [] 안에 '키'를 부여하고 키를 집어넣으면 '값' 도출
english_dict["two"] = "둘"
english_dict["three"] = "셋"

word = input("단어를 입력하시오: ");
print(english_dict.get(word, "사전에 존재하지 않음")) # 존재하지 않을 때 "없음"으로 표시

