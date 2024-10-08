lst = []
for i in range(1, 31):
    lst.append(i)

for i in range(28):
    a = int(input())
    lst.remove(a)

print(lst[0])
print(lst[1])