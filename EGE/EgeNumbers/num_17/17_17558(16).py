sp = [int(x) for x in open('17data/17_17558.txt')]

ct = sum(1 for x in sp if x % 32 == 0)
res = []
for i in range(len(sp) - 1):
    x, y = sp[i],sp[i+1]
    if (x< 0 or y<0) and (x+y) < ct:
        res.append(x+y)

print(len(res), max(res))