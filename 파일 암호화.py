key = 'abcdefghijklmnopqrstuvwxyz'

# 평문을 받아서 암호화하고 암호문을 반환한다.
def encrypt(n, plaintext):
    result = ''

    for l in plaintext.lower():  # 오류처리구조 try 블록에서 오류 발생시 except 블록에서 해결
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

# 암호문을 받아서 복호화하고 평문을 반환

def decrypt(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

n = 3
text = 'the language of truth is simple.'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)
print('평문: ', text)
print('암호문: ', encrypted)
print('복호문: ', decrypted)


