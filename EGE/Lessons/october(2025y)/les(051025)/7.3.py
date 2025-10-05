def fs (n):
    return sum(int(i) for i in str(n) if int(i) % 2 == 0)

print(fs(29))
print(fs(28))
print(fs(2123))
print(fs(1))


def chet(n):
    return any(int(i) % 2 == 0 for i in str(n))

print(chet(99))