n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    change = []
    change.append(lst[a-1])
    change.append(lst[b-1])
    change.reverse()
    lst[a-1] = change[0]
    lst[b-1] = change[1]

for i in lst:
    print(i, end=' ')