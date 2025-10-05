s = '2456789467'

ct = 0

for i in range(len(s) - 1):
    if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 1:
        ct += 1
print(ct)