address = input("이메일 주소를 읿력하시오: ")

(id, domain) = address.split('@')  # @ 기준으로 각각 id 와 domain 으로 나눠짐

print("이메일 주소:", address)
print("아이디:", id)
print("도메인주소:", domain)


