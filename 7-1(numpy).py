import numpy as np

a, b = map(int, input().split())

lst_A = []
for i in range(a):
    col_A = list(map(int, input().split()))
    lst_A.append(col_A)

lst_B = []
for i in range(a):
    col_B = list(map(int, input().split()))
    lst_B.append(col_B)

a_np = np.array(lst_A)
b_np = np.array(lst_B)

c = a_np + b_np
for i in range(a):
    for j in range(b):
        print(c[i][j], end=' ')
    print("") 