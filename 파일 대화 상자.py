# 파일 대화 상자

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if(readFile != None):
    infile = open(readFile, "r")

for line in infile.readlines():
    line = line.strip()
    print(line)

infile.close()

# 스페이스 세기

def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    for line in infile:
        spaces += line.count(' ')
        tabs += line.count('\t')
    infile.close()

    return spaces, tabs

filename = input("파일 이름을 입력하시오: ");
spaces, tabs = parse_file(filename)
print("스페이스 수 = %d, 탭의 수 = %d" % (spaces, tabs))

# 줄 앞에 번호붙이기

infile = open("proverbs.txt")
outfile = open("output.txt","w")
i = 1
for line in infile:
    outfile.write(str(i) + ": " + line)
    i = i + 1
infile.close()
outfile.close()

# 각 문자 횟수 세기

filename = input("파일명을 입력하시오: ").strip()
infile = open(filename, "r") # 파일을 연다

freqs = {}

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다.
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print(freqs)
infile.close()

# 파일을 연다.
f = open("C:\\test.csv", "r")

# 파일 안의 각 줄을 처리한다.
for line in f.readlines():

    # 공백 문자를 없앤다.
    line = line.strip()

    # 줄을 출력한다.
    print(line)

    # 줄을 쉼표로 분리한다.
    parts = line.split(",")

    # 각 줄의 필드를 출력한다.
    for part in parts:
        print("   ", part)