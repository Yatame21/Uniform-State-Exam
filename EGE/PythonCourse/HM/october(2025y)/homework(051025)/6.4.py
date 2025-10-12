a = [3, 1, 0, 8, -10, 14, 15, 20, -5, 7]

summ = 0

for i in a:
    if i % 2 == 0 and i >= 0:
        summ += i

print(summ)