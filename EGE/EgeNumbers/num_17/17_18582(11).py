sp = [int(x) for x in open('17data/17_18582.txt')]

mini = min(sp)
res= []

for i in range(len(sp) - 2):
    x,y,z = sp[i],sp[i+1],sp[i+2]
    if (sum(1 for n in (x,y,z) if n < 0) > sum(1 for n in (x,y,z) if n > 0)) and (x+y+z) %10== mini %10:
        res.append(abs(x + y + z))

print(len(res), max(res))