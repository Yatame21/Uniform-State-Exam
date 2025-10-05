res = 0

while True:
    x = int(input())

    if x == 0:
        break
    if 100 <= x <= 999:
        res += x

print(res)
