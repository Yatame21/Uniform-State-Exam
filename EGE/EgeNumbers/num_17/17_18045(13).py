sp = [int(x) for x in open('17data/17_18045.txt')]

na = sum(1 for x in sp if 10<=x<=99)

res = []
for i in range(len(sp) - 1):
    x, y = sp[i],sp[i + 1]
    if (x%10 + y%10) == na:
        res.append(x+y)

print(len(res),min(res))