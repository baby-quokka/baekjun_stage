a, b = map(str, input().split())

A = list(a)

B = list(b)

rev_a = 0
for i in range(len(A)):
    rev_a += int(A[i]) * 10**(i)

rev_b = 0
for i in range(len(B)):
    rev_b += int(B[i]) * 10**(i)

lst = [rev_a, rev_b]
print(max(lst))