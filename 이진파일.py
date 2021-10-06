# 이진 파일에서 데이터를 읽으려면 다음과 같이 파일을 연다.
# infile = open(filename, "rb")

# 입력 파일에서 8바이트를 읽으려면
# bytesArray = infile.read(8)

# bytesArray 는 바이트형의 시퀀스로서 0부터 255까지의 값들의 모임
# byte1 = bytesArray[0]

# 이진 파일에 바이트들을 저장하려면
# outfile = open(filename, "wb")
# bytesArray = bytes([255, 128, 0, 1])
# outfile.write(bytesArray)


