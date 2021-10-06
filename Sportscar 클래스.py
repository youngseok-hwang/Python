class Car:
    def __init__(self, speed):
        self.speed = speed

    def setSpeed(self, speed):
        self.speed = speed

    def getDesc(self):
        return "차량 =("+str(self.speed)+")"

class SportsCar(Car):
    def __init__(self, speed, turbo):
        super().__init__(speed)  # 부모의 생성자 호출
        self.turbo = turbo

    def setTurbo(self, turbo):
        self.turbo = turbo

obj = SportsCar(100, True)
print(obj.getDesc())
obj.setTurbo(False)
