# 알파벳 소문자, 대문자, 숫자 0~9만 가능!

a = input()

if type(a) == int:
    print(chr(a))    # 이거 쓰는거 아님! 땡!

elif type(a) == str:
    print(ord(a))


# 이게 된다고??  ->  다 숫자로 바꾸는 거라 ord만 쓰면 됨.
print(ord(input()))