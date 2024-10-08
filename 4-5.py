import sys

n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(0)

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    while a <= b:
        x = 0
        lst[a-1 + x] = c
        x += 1
        a += 1

for i in lst:
    print(i, end=' ')