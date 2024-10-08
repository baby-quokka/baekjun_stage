a = int(input())

lst = []
for i in range(1, a+1):
    b = ' '*int(((2*a-1)-(2*i-1))/2) + '*'*(2*i-1) + ' '
    lst.append(b)


for i in range(len(lst)-1):
    lst.append(lst[a-2-i])

c = str(lst[2*a-2])
c.rstrip(' ')
lst[2*a-2] = c

for i in lst:
    print(i)