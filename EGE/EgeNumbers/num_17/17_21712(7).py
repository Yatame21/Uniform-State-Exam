sp = [int(x) for x in open('17data/17_21712.txt')]

m = min(x for x in sp if 1000<=x<=9999 and x % 10 == 6)

res = []

for i in range(len(sp) - 2):
    x,y,z = sp[i], sp[i+1], sp[i+2]
    if sum(1 for n in [x,y,z] if 1000<=abs(n)<=9999 and abs(n) % 10 ==6) == 1 and x+y+z <=m:
        res.append(x+y+z)

print(len(res), max(res))
