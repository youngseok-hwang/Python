
class Counter:
    def __init__(self):
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count


class Counter:
    def __init__(self, initValue=0):
        self.count = initValue

a = Counter(100)  # 카운터 초기값 100
b = Counter()     # 카운터 초기값 0


