sp = [int(x) for x in open('17data/17_17873.txt')]

minim = min(sp)

res = []
for i in range(len(sp) - 1):
    x, y = sp[i],sp[i+1]
    if x %16 == minim or y%16 ==minim:
        res.append(x+y)

print(len(res),max(res))