sp = [int(x) for x in open('17data/17_23201.txt')]

m = min(x for x in sp if 100<=abs(x)<=999 and x % 10 == 7)
res = []

for i in range(len(sp) - 1):
    x,y = sp[i], sp[i+1]
    n1 = 100<=abs(x)<=999
    n2 = 100<=abs(y)<=999
    if ((n1 and  not n2) or (not n1 and n2)) and ((x+y) % m == 0):
        res.append(x+y)

print(len(res),min(res))
