sp = [int(x) for x in open('17data/17_21416.txt')]

otr = sum(x for x in sp if x < 0)
res = []

for i in range(len(sp)- 2):
    x,y,z = sp[i],sp[i+1],sp[i+2]
    if (max(x,y,z) + min(x,y,z)) > otr:
        res.append(x+y+z)

print(len(res), max(res))