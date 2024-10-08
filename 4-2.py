a, b = map(int, input().split())

lst = list(map(int, input(). split()))
small = []

for i in range(a):
    if lst[i] < b:
        small.append(lst[i])

for i in range(len(small)):
    print(small[i], end=' ')