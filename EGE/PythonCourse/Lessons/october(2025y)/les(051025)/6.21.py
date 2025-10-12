a = [10, 15, 17, 6, 4, 16, 6, 7]

ct = 0

gen = sum(1 for i in a if i % 2 == 0)
print(gen)