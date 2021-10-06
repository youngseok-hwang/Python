
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add2(self, x):
        self.add(x)
        self.add(x)

bag = Bag()
a = bag.add(10)
b = bag.add2(100)

print(a)
print(b)