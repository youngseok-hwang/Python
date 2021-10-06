
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel   # 채널 => 인스턴트 변수(객체의 상태 혹은 속성)
        self.volume = volume     # 소리 크기 => 인스턴트 변수(객체의 상태 혹은 속성)
        self.on = on             # 전원 => 인스턴트 변수(객체의 상태 혹은 속성)

    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel

t = Television(9, 10, True)
t.show()
t.setChannel(11)
t.show()

