lst = list(map(int, input().split()))

lst_or = [1,1,2,2,2,8]

A = []
for i in range(6):
    a = lst_or[i] - lst[i]
    A.append(a)

for i in A:
    print(i, end=' ')