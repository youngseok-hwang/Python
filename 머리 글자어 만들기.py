
phrase = input("문자열을 입력하시오: ")

acronym = ""
list = ["by", "in", "the", "of"]
for i in range(len(list)):
    up_list = list[i].upper()

for word in phrase.upper().split():
    if word in up_list:
        del(word)
    else:
        acronym += word[0] + "."

print(acronym)