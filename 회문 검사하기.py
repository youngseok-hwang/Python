
def check_pal(s):
    low = 0
    high = len(s) - 1
    while True:
        if low > high:
            return True;
        a = s[low]
        b = s[high]

        if a != b:
            return False
        low += 1
        high -= 1

s = input("문자열을 입력하시오: ")
s = s.replace(" ", "")
check = check_pal(s)

if(check == True):
    print("화문입니다.")
else:
    print("화문이 아닙니다.")

