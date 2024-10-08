s = str(input())

S = s.upper()

lst = []
for i in range(65, 91):
    cnt = S.count(chr(i))
    lst.append(cnt)

a = max(lst)
index = lst.index(a)

lst.remove(a)
if a in lst:
    print('?')
if a not in lst:
    print(chr(index + 65))