text = "Will is power."
print(text[0], text[3], text[-1])
print(len(text))

flist = ["apple", "banana", "tomato", "peach", "pear"]
print(flist[0], flist[3], flist[-1])
print(len(flist))

a = len([1, 2, 3]) # 리스트 길이
print(a)

b = [1, 2] + [3, 4, 5] # +의 사용새
print(b)

c = ["Welcome!"]*3     # *의 사용새
print(c)

d = [1, 2, 3]          # in, not in의 사용새
print(3 in d)
print(3 not in d)      # 1, 2, 3 중에 3이 들어있지 않다.
                       # 라는 뜻이므로 결과가 False로 나온다.

e = b[1]               # []의 사용새
print(e)

f = min([1, 2, 3])     # 최소값
print(f)

g = max([1, 2, 3])     # 최대값
print(g)

for x in [1, 2, 3]:    # 반복
    print(x)과