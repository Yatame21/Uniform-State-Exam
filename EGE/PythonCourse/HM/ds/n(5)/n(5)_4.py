def f(n):
    s =''
    while n>0:
        s = str(n%7)+s
        n = n//7
    return s
res=[]
for n in range(1,100000):
    N=n
    R=f(n)
    if R.count('2') %2==0:
        R = R+'555'
    else:
        R='1'+ R

    R = int(R,7)
    if R < 3799:
        res.append(N)
print(max(res))