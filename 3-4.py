total = int(input())
type = int(input())

lst = []

for i in range(1, type+1):
    a,b = map(int, input().split())
    lst.append(a*b)

if total == sum(lst):
    print("Yes")

else:
    print("No")