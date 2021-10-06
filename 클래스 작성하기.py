
class Counter:           # Counter는 클래스의 이름
    def reset(self):     # 메소드 정의
        self.count = 0   # 인스턴스 변수 생성
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

a = Counter()
b = Counter()

a.reset()
b.reset()
a.increment()
b.increment()

print("카운터 a의 값은", a.get())
print("카운터 b의 값은", b.get())



