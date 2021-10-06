class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue
    def __iter__(self):
        return self
    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
        self.a = self.b    # a를 b로 정의
        self.b = n         # b를 n으로 정의
        return n           # a -> b, b -> n => 계속해서 결과값에 다음 수를 더할 수 있게 된다.

c = FibIterator()
for i in c:
    print(i, end=" ")
