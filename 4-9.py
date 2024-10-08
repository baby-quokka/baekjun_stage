n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    rev = lst[a-1:b]
    rev.reverse()
    lst[a-1:b] = rev

for i in lst:
    print(i, end=' ')