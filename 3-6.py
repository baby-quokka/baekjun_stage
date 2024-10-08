import sys

T = int(input()) #Test case
lst = []

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    lst.append(a+b)

for i in range(T):
    print(lst[i])