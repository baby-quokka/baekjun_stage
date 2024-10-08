S = str(input())

cor = ['c=', 'c-', 'dz=', 'd-' , 'lj', 'nj', 's=', 'z=']

alphabet = 0
for i in range(8):
    if cor[i] in S:
        cnt = S.count(cor[i])
        alphabet += cnt
        S = S.replace(cor[i],' ')

lst = list(S)
blank = 0
for i in range(len(lst)):
    if lst[i] == ' ':
        blank += 1

print(alphabet + len(lst) - blank)
