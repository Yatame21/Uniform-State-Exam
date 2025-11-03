sp = [int(x) for x in open('17data/17_19249.txt')]

m = max(x for x in sp if 10000 <= abs(x) <= 99999 and abs(x) % 100 == 43)
res= []

for i in range(len(sp) - 2):
    x,y,z = sp[i],sp[i+1],sp[i+2]
    s = x*x + y*y + z*z
    if any(10000 <= abs(n)<= 99999 and abs(n) % 100 == 43 for n in (x,y,z)) and s <= m*m:
        res.append(s)

print(len(res),min(res))