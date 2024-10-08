while True:
    try:
        a = input()
        print(a)
    except:
        break

# 이게 진짜 정답!
arr = []

while True:
    try:
        pra = input()
        if len(pra) != 0:   # 입력값이 빈칸이 아니면 리스트에 추가!
            arr.append(pra)
        else:
            break
    except EOFError:   # except만 해도 가능!
        break
for word in arr:
    print(word)    