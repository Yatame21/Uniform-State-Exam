from itertools import product

sp = list(map(''.join, product('012345678', repeat=5)))

ct= 0

for x in sp:
    if x[0] != '0' and x.count('0') ==1 and all(not((x[i] == '0' and int(x[i+1])%2==1) or (x[i+1]=='0' and int(x[i])%2==1)) for i in range(len(x)-1)):
        ct += 1

print(ct)