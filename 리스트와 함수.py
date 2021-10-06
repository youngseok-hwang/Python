def func1(x):                       # 변경 불가능한 객체들은 객체를 변경하면 참조값이 바뀐다. 새로운 객체가 생기기 때문이다.
    print("x=", x, "id=", id(x))
    x = 42
    print("x=", x, "id=", id(x))

y = 10                              # y는 전역변수라 함수 내에서만 지역변수로 쓰였다가 함수가 끝나면 다시 전역변수 값으로 돌아온다.

print("y=", y, "id=", id(y))
func1(y)
print("y=", y, "id=", id(y))

def func2(list):                    # 변경 가능한 객체인 리스트를 함수에 전달하면, 함수 내에서 리스트 요소를 변경할 수 있다.
    list[0] = 90

values = [0, 1, 1, 2, 3, 5, 8]
print(values)
func2(values)
print(values)

