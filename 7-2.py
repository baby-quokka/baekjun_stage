lst = []
for i in range(9):
    a = list(map(int, input().split()))
    lst.append(a)

max_lst = []
for i in lst:
    max_lst.append(max(i))

max_int = max(max_lst)
print(max(max_lst))

max_col = max_lst.index(max(max_lst))
lst_col = lst[max_col]
max_row = lst_col.index(max_int)
print(max_lst.index(max(max_lst))+1, end=' ')
print(max_row+1)