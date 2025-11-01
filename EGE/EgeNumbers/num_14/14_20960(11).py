res= []

for x in range(1,2006):
    n = 5 ** 150 + 5 ** 98  - x
    r = 0
    while n > 0:
        if n % 5 == 0:
            r+=1
        n//=5
    res.append([r,x])
res.sort()
print(res)

# [56, 1875]  -answer