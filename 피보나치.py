def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("정수를 입력하시오: "))
print(n, "번째 피보나치 수는 ", fib(n))

fiboList = {0:0, 1:1}

def fibm(n):
    if not n in fiboList:
        fiboList[n] = fibm(n-1) + fibm(n-2)
    return fiboList[n]
n = int(input("정수를 입력하시오: "))
print(n, "번째 피보나치 수는 ", fibm(n))


# 에라스토스의 체

def eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
print(list(eratosthenes(100)))


# 디텍터리 크기 계산

import os

def calcDirSize(name):
    totalsize = 0

    if os.path.isfile(name):
        totalsize += os.path.getsize(name)
    else:
        fileList = os.listdir(name)
        # 서브 디텍터리의 용량을 계산하여 모두 합
        for subDir in fileList:
            totalsize += calcDirSize(name + "\\" + subDir)

    return totalSize

name = input("디텍터리 이름을 입력하시오: ")
print(calcDirSize(name))
