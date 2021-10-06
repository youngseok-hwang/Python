
# 피보나치 수열

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)
#print(fib(int(input("피보나치에 들어갈 변수 n을 입력하시오: "))))


# 미리 값 0, 1을 지정해두어 값이 - 되는 상황을 방지하고 시작한다.
# 그 후에 딕셔너리를 만들어서 반복작업하는 경우 없이 한 번 수행했던 것은 저장하여 불러올 수 있도록 만든다.
table = {0:0, 1:1}

def fib(n):
    if n not in table:
        value = fib(n-1) + fib(n-2)
        table[n] = value
    return table[n]
print(fib(100))

