(x, y) = (2, 0)
try:
    z = x/y
except ZeroDivisionError:
    print("0으로 나누는 예외")  # 미리 지정한 예외 메시지 출력

# (x, y) = (2, 0)
# try:
#     z = x/y
# except ZeroDivisionError as e:  # 시스템이 내보내는 예외 메시지 출력
#     print(e)

# n = int(input("숫자를 입력하시오: "))
# 정수를 입력해야하는데 실수를 입력하면 오류 발생

while True:   # 실수와 정수 오류처리
    try:
        n = input("숫자를 입력하시오: ")
        n = int(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오.")
print("정수 입력이 성공하였습니다.")

try:
    fname = input("파일 이름을 입력하세오: ")
    infile = open(fname, "r")
except IOError:
    print("파일 " + fname + "을 발견할 수 없습니다.")

try:
    fh = open("phones", "w")
    fh.write("테스트 데이터를 파일에 씁니다!")
except IOError:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
else:
    print("파일에 성공적으로 기록하였습니다.")
    fh.close()

# finally 블록

try:
    f = open("phones.txt", "w")
    f.write("테스트 데이터를 파일에 씁니다!")
    # 파일 연산을 수행
except IOError:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
finally:
    f.close()
