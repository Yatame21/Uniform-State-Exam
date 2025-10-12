sp = [int(x) for x in open('17data/17_20963.txt')]

minimal = min(x for x in sp if 1000<=abs(x)<=9999 and x % 17 == 0)
res = []

for i in range(len(sp)- 2):
    x,y,z = sp[i],sp[i+1],sp[i+2]
    if sum(1 for n in [x,y,z] if 1000<=abs(n)<=9999 and abs(n)%100 == 27) >= 1 and x**2 + y**2 + z**2 <= minimal**2 :
        res.append(abs(x)+abs(y)+abs(z))

print(len(res),min(res))