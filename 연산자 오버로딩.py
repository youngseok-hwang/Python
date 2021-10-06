# 연산자 오버로딩

# + 연산자 => __add__(self, other)
# == 연산자 => __eq__(self, other)

s1 = "Impossible "
s2 = "Dream"
s3 = s1.__add__(s2)
print(s3)

# 2차원 상 한 점을 클래스로 지정하고, 점과 점을 + 연산으로 합하기

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

p1 = Point(1, 2)
p2 = Point(3, 4)
a = p1 + p2
print(a)

