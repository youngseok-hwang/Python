# 파일 열기

infile = open('phones.txt', 'rt', encoding='UTF8')

s = infile.readline()
print(s);
s = infile.readline()
print(s);
s = infile.readline()
print(s);

infile = open('phones.txt', 'rt', encoding='UTF8')

line = infile.readline()
while line != "":
    print(line);
    line = infile.readline()

infile = open("phones.txt", 'rt', encoding='UTF8')
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()

outfile = open("phones.txt", "w", encoding='UTF8')

outfile.write("홍길동 011-8820-2929 \n")
outfile.write("김철수 012-8823-3838 \n")
outfile.write("김영희 013-8890-0001 \n")
outfile.close()

infile = open('phones.txt', 'rt', encoding="UTF8")
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()

import os.path

outfile = open("phones.txt", "w", encoding="UTF8")

if os.path.isfile("phones.txt"):
    print("동일한 이름의 파일이 이미 존재합니다. ")
else:
    outfile.write("홍길동 010-1234-5678")
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010-1234-5680")
outfile.close()

