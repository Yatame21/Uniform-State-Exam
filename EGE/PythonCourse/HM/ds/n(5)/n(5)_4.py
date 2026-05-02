def f(n):
    s =''
    while n>0:
        s = str(n%2)+s
        n = n//2
    return s
res=[]
for n in range(1,100000):
    N=n
    R=f(n)
    if



    R = int(R,7)
    if R < 3799:
        res.append(N)
print(max(res))