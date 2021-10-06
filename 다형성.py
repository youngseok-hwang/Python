# 상속과 다형성

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '알 수 없음'

class Dog(Animal):
    def speak(self):
        return '멍멍!'
# 부모 클래스 오버라이드

class Cat(Animal):
    def speak(self):
        return '야옹!'
# 부모 클래스 오버라이드

animalList = [Dog('dog1'), Dog('dog2'), Cat('cat1')]

for a in animalList:
    print(a.name + ': ' + a.speak())

