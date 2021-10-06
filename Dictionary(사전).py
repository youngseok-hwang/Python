d = {1: 'apple', 2:'banana'}

contacts = {'Kim':'01012345678', 'Park':'01012345679', 'Lee':'01012345680'}
print(contacts)

d = {}   # 공백 딕셔너리

print(contacts['Kim'])     # 해당 값은 키를 이용하여 부른다.
print(contacts.get('Kim')) # .get()을 이용하기도 함

number = contacts.get("Choi", "010114")
print(number)

if "Kim" in contacts:
    print("키가 딕셔너리에 있음")

contacts['Choi'] = '01056781234'  # 항목 추가
print(contacts)

contacts.pop("Kim")               # 항목 삭제
print(contacts)

contacts = {'Kim':'01012345678', 'Park':'01012345679', 'Lee':'01012345680'}
del contacts['Kim']               # 항목삭제
print(contacts)

scores = {'Korean': 80, 'Math': 90, 'English': 80}
for item in scores.items():
    print(item)

squares = {1:1, 3:9, 5:25, 7:49, 8:64, 9:81}
1 in squares
2 not in squares

triples = {x:x*3 for x in range(6)} # 0부터 5까지
print(triples)

dic = {"bags": 1, "books": 5, "bottles": 4, "coins": 7, "cups": 2, "pens": 3}
print(dic)
list(dic)
print(list(dic))

a = sorted(dic)  # key(키) 정렬
print(a)

b = sorted(dic.values())  # values(값) 정렬
print(b)

c = sorted(dic, key = dic.__getitem__)
# [1, 2, 3, 4, 5, 6, 7] 순서로 정렬된다.
print(c)

