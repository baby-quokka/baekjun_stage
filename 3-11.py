lst = []

while True:
    a,b = map(int, input().split())
    
    lst.append(a+b)
    
    if a == 0 and b == 0:
        break

for i in range(len(lst)-1):
    print(lst[i])