sp = [int(x) for x in open('17data/17_17750.txt')]

minim = min(sp)
res = []
for i in range(len(sp) - 1):
    x,y = sp[i],sp[i+1]
    if (x%77 + y%77) == minim:
        res.append(x+ y)

print(len(res), max(res))