
# 특수 메소드를 넣었을 때 특수 연산자로 비교가능하다.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return Vector2D(self.x == other.x, self.y == other.y)

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
b = u + w
c = v + w
print(a)
print(b)
print(c)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "제목: %s, 저자: %s, 쪽수: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

book = Book("Data Structure", "Chun", 650)
print(book)
print("책의 쪽수는", len(book))