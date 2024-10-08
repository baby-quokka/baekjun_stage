a, b = map(int, input().split())

lst_A = []
for i in range(a):
    c = list(map(int, input().split()))
    lst_A.append(c)
    
lst_B = []
for i in range(a):
    c = list(map(int, input().split()))
    lst_B.append(c)

add = []
for i in range(a):
    for j in range(b):
        d = lst_A[i][j] + lst_B[i][j]
        print(d, end=' ')
    print('')