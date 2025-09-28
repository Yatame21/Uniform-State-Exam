ct = 0

for num_1 in range (1,10):
    for num_2 in range (0,10):
        for num_3 in range (0,10):
            for num_4 in range (0,10):
                if num_1 == num_2 and num_3 == num_4:
                    ct +=1

print(ct)