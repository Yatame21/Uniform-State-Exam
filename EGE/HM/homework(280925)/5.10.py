m = '213456789'

ct = 0
for i in m[1::2]:
    if int(i) % 2 == 0:
        ct += int(i)


print(ct)

