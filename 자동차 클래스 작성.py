
class Car:
    def __init__(self, speed=0, gear=1, color="white", fuelratio=0):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
        self.__fuelratio = fuelratio

    def setSpeed(self, speed):
        self.__speed = speed;

    def setGear(self, gear):
        self.__gear = gear;

    def setColor(self, color):
        self.__color = color;

    def setFuelratio(self, fuelratio):
        self.__fuelratio = fuelratio;

    def __str__(self):
        return '(%d, %d, %s, %d)' %(self.__speed, self.__gear, self.__color, self.__fuelratio)

    def calcFuel(self, distance):
        self.__distance = distance
        return self.__distance / self.__fuelratio

myCar = Car()
myCar.setSpeed(3);
myCar.setGear(100);
myCar.setColor('Black')
myCar.setFuelratio(10)
print(myCar, " 사용하는 연료량은", myCar.calcFuel(100),"임")

