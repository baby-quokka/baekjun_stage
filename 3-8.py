T = int(input()) #Test case
lst_a = []
lst_b = []

for i in range(T):
    a,b = map(int, input().split())
    lst_a.append(a)
    lst_b.append(b)

for i in range(T):
    print("Case #{0}: {1} + {2} = {3}".format(i+1, lst_a[i], lst_b[i], lst_a[i]+lst_b[i]))


# 이런 방법이!!
number = int(input())

list = []
for i in range(number):
    a, b = input().split()
    a = int(a)
    b = int(b)
    list.append((i+1,a ,b ,a+b))  # 통째로 리스트에 저장

for n in list:
    print('Case #%s: %s + %s = %s' % n)  # format이랑 같은 방식