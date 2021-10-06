
class Television:
    serialNumber = 0                  # 클래스 변수
    def __init__(self):
        Television.serialNumber += 1  # 클래스 변수를 하나 증가
        self.number = Television.serialNumber # 클래스 변수는 클래스 이름 뒤에 붙여서 접근한다.

    # 클래스 변수의 값을 TV의 시리얼 번호로 한다.


