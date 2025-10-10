a = [2, 6, 3, 7, 10, 12, 15, 1, 20, 17]

ct = 0
b = a[1::2]

for i in b:
    if i % 2 == 0:
        ct += i

print(ct)