a,b,c = map(int, input().split())

list = [a,b,c]

if a==b==c:
    print(10000+a*1000)

elif a==b or b==c:
    print(1000+b*100)

elif a==c:
    print(1000+a*100)

elif a!=b!=c:
    print(max(list)*100)