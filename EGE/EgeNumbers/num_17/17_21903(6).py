sp = [int(x) for x in open('17data/17_21903.txt')]

m = min(x for x in sp if abs(x) % 100 == 15 and 100<= abs(x)<= 999)**2
res = []

for i in range(len(sp)-2):
    x,y,z = sp[i],sp[i+1],sp[i+2]
    if min(x,y,z) * max(x,y,z) > m :
        res.append(min(x,y,z) * max(x,y,z))

print(len(res), min(res))