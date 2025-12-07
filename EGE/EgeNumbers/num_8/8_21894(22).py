from itertools import permutations
sp = list(map(''.join, permutations('0123456789', 4)))

ct = 0

for x in sp:
    if x[0] != '0' and all((int(x[i])%2) != (int(x[i+1]) %2) for i in range(3)):
        ct+=1

print(ct)
