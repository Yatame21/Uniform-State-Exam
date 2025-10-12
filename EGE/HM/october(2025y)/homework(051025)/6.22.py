a = [10, 15, 17, 6, 4, 16, 6, 7]

res = [i for i in range(len(a)) if a[i] % 2 != 0]
print(*res)