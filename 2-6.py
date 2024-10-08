A, B = map(int, input().split())
C = int(input())

if B+C < 60:
    print(A, B+C)

elif B+C >= 60:
    print((A+(B+C)//60)-((A+(B+C)//60)//24)*24, (B+C)-((B+C)//60)*60)


# 쉬운 방법
a, b = map(int, input().split())
c = int(input())

m = (b+c)%60   # 나머지 분(minute)
alpha = (b+c)//60   # 추가된 시간(hour)
h = (a + alpha)%24   # 나머지 시간(hour)

print(h, m)