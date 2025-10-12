a = [10, 15, 17, 6]
b = int(input())

gen = [i for i in a if b < i]
print(*gen)