T = int(input())

lst_int = []
lst_str = []
for i in range(T):
    a, b = map(str, input().split())
    lst_int.append(int(a))
    lst_str.append(str(b))

for i in range(T):
    lst = list(lst_str[i])
    for j in lst:
        print(j * lst_int[i], end='')
    print("")