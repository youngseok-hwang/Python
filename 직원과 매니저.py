class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def getSalary(self):                    # 부모 클래스의 메소드를 오버라이드한다
        salary = super().getSalary()
        return salary + self.bonus

    def __repr__(self):
        return "이름: " + self.name + "; 월급: " + str(self.salary) + "; 보너스: " + str(self.bonus)
                                            # 객체를 문자열로 표현하여 반환하는 메소드이다

kim = Manager("김철수", 2000000, 1000000)
print(kim)                                  # __repr__()이 호출된다

