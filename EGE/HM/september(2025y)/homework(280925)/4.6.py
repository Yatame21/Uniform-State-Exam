n = int(input())

ct = 0

for i in range(n):
    x = int(input())
    if x % 13 == 0:
        ct += x

print(ct)