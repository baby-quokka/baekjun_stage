num = int(input())
time = 0
lst = []

while True:
    a,b = map(int, input().split())
    
    lst.append(a+b)
    
    time += 1
    if time == num:
        break

for i in range(num):
    print(lst[i])