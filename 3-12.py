lst = []

while True:
    try:
        a,b = map(int, input().split())
        
        lst.append(a+b)

    except:
        break

for i in range(len(lst)):
    print(lst[i])