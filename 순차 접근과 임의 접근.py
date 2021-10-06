infile = open("proverbs.txt", "r+")
str = infile.read(10);
print("읽은 문자열: ", str)
position = infile.tell();
print("현재 위치: ", position)

position = infile.seek(0, 0);  # 파일의 처음으로 이동
str = infile.read(10);
print("다시 읽은 문자열: ", str)
infile.close()

# 객체 입출력

import pickle

myMovie = { "Superman vs Batman ": 9.8, "Ironman": "9.6"}
        # 딕셔너리 피클 파일에 저장
        picle.dump(myMovie, open("save.p", "wb"))

# 피클 파일에 딕셔너리률 로딩

'Superman VS Batman' : 9.8
'Ironman' : '우와 점'