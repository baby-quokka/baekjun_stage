a = int(input())
b = int(input())

first = b % 10
second = int(((b % 100) - first) / 10)
third = int((b - (second * 10) - first) / 100)

print(a * first)
print(a * second)
print(a * third)
print(a * b)
