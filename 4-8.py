set = {'A'}

for i in range(10):
    a = int(input())
    set.add(a%42)

set.remove('A')
print(len(set))