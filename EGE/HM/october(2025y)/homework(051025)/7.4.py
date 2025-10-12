def vivo(n):
    ct = 0
    for i in str(n):
        if int(i) % 2 != 0:
            ct += 1
    return ct

print(vivo(12345))
print(vivo(2468))
