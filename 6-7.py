T = int(input())

lst = []
for i in range(T):
    S = str(input())
    lst.append(S)

error = 0
for i in lst:
    for j in range(len(i)):
        if str(i).count(i[j]) == 1:
            continue
        else:
            if i[j] * str(i).count(i[j]) in i:
                continue
            else:
                error += 1
                break
                
print(T - error)
            