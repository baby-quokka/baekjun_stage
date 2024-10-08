lst = []
for i in range(5):
    lst.append(list(input()))

lst_len = []
for i in lst:
    lst_len.append(len(i))

length = max(lst_len)

for i in lst:
    while len(i) < length:
        i.append('')

for i in range(length):
    for j in range(5):
        print(lst[j][i], end='')