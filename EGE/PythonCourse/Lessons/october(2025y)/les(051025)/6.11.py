a = [2, -6, -3, 7, 10, 0, 15, -1, 20, 17]

pos = []
neg = []

for i in a:
    if i > 0:
        pos += [i]
    elif i < 0:
        neg += [i]

print(pos)
print(neg)