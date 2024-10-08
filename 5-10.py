lst = list(str(input()))

time = 0

for i in lst:
    if 65 <= ord(i) < 68:
        time += 3
    elif 68 <= ord(i) < 71:
        time += 4
    elif 71 <= ord(i) < 74:
        time += 5
    elif 74 <= ord(i) < 77:
        time += 6
    elif 77 <= ord(i) < 80:
        time += 7
    elif 80 <= ord(i) < 84:
        time += 8
    elif 84 <= ord(i) < 87:
        time += 9
    elif 87 <= ord(i) < 91:
        time += 10

print(time)

# 더 쉬운 노가다
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)