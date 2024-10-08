a, b = map(int, input().split())

if b >= 45:
    print(a, b - 45)

elif a > 0 and b < 45:
    print(a-1, 60 - abs(b-45))

elif a == 0 and b < 45:
    print(23, 60 - abs(b-45))