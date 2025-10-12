sp=[int(x) for x in open('17data/17_23563.txt')]

de = min(x for x in sp if x > 0 and x % 35 == 0)

res = []
for i in range(len(sp)- 1):
    x,y = sp[i],sp[i+1]
    if x != y and abs(x-y) % de== 0:
        res.append(x+y)

print(len(res), max(res))
