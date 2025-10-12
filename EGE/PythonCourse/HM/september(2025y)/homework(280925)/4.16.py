ct = 0

for x1 in range(1,10):
    for x2 in range(0,10):
        for x3 in range(0,10):
            for x4 in range(0,10):
                k = 0
                if x1 % 2 == 0:
                    k+=1
                if x2 % 2 == 0:
                    k+=1
                if x3 % 2 == 0:
                    k+=1
                if x4 % 2 == 0:
                    k+=1
                if k == 2:
                    ct += 1
print(ct)