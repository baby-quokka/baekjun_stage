board = [[0] * 100 for _ in range(100)]

T = int(input())
lst_a = []
for i in range(T):
    a = list(map(int, input().split()))
    lst_a.append(a)

for x in lst_a:
    for i in range(x[0],x[0]+10):
        for j in range(x[1],x[1]+10):
            board[i][j] = 1

cnt = 0
for i in range(100):
    b = board[i].count(1)
    cnt += b

print(cnt)