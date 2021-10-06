# 데이터 추가하기

outfile = open("phones.txt", "a")  # "a"는 append의 약자

outfile.write("최무선 010-1111-2222")
outfile.write("정중부 010-2222-3333")

outfile.close()

# 줄바꿈 기호 삭제하기

infile = open("proverbs.txt", "r")
for line in infile:
    line = line.rstrip()  # rstrip()은 줄바꿈 문자 \n뿐만 아니라 공백문자 space도 제거
    print(line);
infile.close()

# 파일에서 텍스트 읽기

infile = open("proverbs.txt", "r")
for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);
infile.close()

line = "Bad: news: travels: fast."
word_list = line.split(":")  # :를 사용하여 분리
print(word_list)

# 숫자 데이터

outfile = open("numbers.txt", "w")

for i in range(10):
    outfile.write(str(i)+" ")

outfile.close()

