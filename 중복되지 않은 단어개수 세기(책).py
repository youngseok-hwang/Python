# 단어에서 구두점을 제거하고 소문자로 만든다.
def process(w):
    output = ""
    for ch in w:
        if ch.isalpha():  # isalpha()는 영문자인지 판별하는 메소드
            output += ch    # 오류 발생

        return output.lower()

words = set()

# 파일을 연다.
fname = input("입력 파일 이름: ")
file = open(fname, "r")

# 파일의 모든 줄에 대해 반복한다.
for line in file:
    lineWords = line.split()
    for word in lineWords:
        print(process(word))
        words.add(process(word))  # 단어를 세트에 추가한다.
a = len(words)
print("사용된 단어의 개수 = %d" %a)
print(words)