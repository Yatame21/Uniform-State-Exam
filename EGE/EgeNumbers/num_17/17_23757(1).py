sp=[int(x) for x in open('17data/17_23757.txt')]

m2=min(x for x in sp if 10<=x<=99)
rez=[]
for i in range(len(sp)-1):
    x,y=sp[i],sp[i+1]
    if sum(1 for n in [x,y] if 10<=n<=99)==1 and (x+y)%m2==0:
        rez.append(x+y)
print(len(rez),max(rez))

# 150 9930

