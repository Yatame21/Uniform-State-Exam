n = int(input())
ct = 0

for i in range(n):
    s = input()
    if s == s[::-1]:
        ct += 1

print(ct)