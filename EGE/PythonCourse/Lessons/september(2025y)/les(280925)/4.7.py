n = int(input())

sum = 0
ct = 0

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        sum += x
        ct += 1



print(sum / ct)