a = [5, 6, 3, 11, 10, 1, 15, 9, 14, 4]
b = [1, 8, 2, 15, 10, 20, 10, 5, 10, 6]

c = []

for i in range(len(a)):
    c.append(min(a[i], b[i]))

print(*c)