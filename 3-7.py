T = int(input()) 
lst = []

for i in range(T):
    a,b = map(int, input().split())
    lst.append(a+b)

for i in range(T):
    print("Case #{0}: {1}".format(i+1, lst[i]))