a = [3, 1, 0, 8, -10, 14, 15, 20, -5, 7]

mi = a[0]
ma = a[0]

for i in a:
    if i < mi:
        mi = i
    if i > ma:
        ma = i

print(mi + ma)


# print(min(a) + max(a))  - analogue