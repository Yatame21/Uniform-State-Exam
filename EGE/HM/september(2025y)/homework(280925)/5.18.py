x = int(input())

ct = 0

for i in range(x):
    n = input()
    if n.count('а')==1:
        ct += 1

print(ct)