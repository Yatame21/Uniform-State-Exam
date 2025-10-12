a = [4, -1, 3, 9, 8, 14, 0, 5, 17, -7]
b = [2, 1, 6, 9, -11, 1, 11, 3, 4, 10]

res = []
for i in range(len(a)):
    res += [a[i] * b[i]]

print(*res)