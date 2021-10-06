List = []
Set = {}
f = open(r"C:\Users\yaung\Desktop\proverbs.txt")  # 파일 열기

for line in f:
    voca = line
    voca = voca.replace('.', '')  # '.'을 공백으로 대체
    voca = voca.lower()           # 전부 소문자로 변경
    voca = voca.split()           # 문장을 단어로 하나하나 쪼개기
    for i in range(len(voca)):    # 보카 리스트 크기 만큼 반복
        List.append(voca[i])      # 단어 하나하나 처음부터 끝까지 리스트에 추가

Set = sorted(set(List))           # 리스트를 집합으로 변환 -> 중복되는 단어는 사라지고 공통된 단어만 남음
print(Set)                        # 집합 도출
a = len(Set)
print("사용된 단어의 개수는 %d개" %a) # 집합 내 단어(요소)의 개수 도출 // %d 사용할 때는 "~~" 뒤에 콤마 없이 '%변수' 집어넣기


