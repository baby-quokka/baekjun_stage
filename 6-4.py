lst = list(str(input()))
lst_rev = []
for i in range(len(lst)):
    lst_rev.append(lst[len(lst)-1-i])

if lst == lst_rev:
    print(1)

else:
    print(0)