sp = [int(x) for x in open("17data/17_23276.txt")]

ma = max(x for x in sp if abs(x) % 100 == 25)
res = []

for i in range(len(sp)-2):
    x,y,z=sp[i],sp[i+1],sp[i+2]
    if sum(1 for n in [x,y,z] if 1000<=abs(n)<=9999) <= 2 and x+y+z < ma:
        res.append(x+y+z)

print(len(res), max(res))
