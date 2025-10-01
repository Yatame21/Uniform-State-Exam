ct = 0

for x1 in range(1,10):
    for x2 in range(0,10):
        for x3 in range(0,10):
            for x4 in range(0,10):
                if x1 % 2 == 0 or x2 % 2 == 1 or x3 % 2 == 1 or x4 % 2 == 0:
                    ct += 1

print(ct)

