T = int(input())

lst = []
for i in range(T):
    s = str(input())
    lst.append(s)

for i in lst:
    print(i[0] + i[-1])