def f(n):
    s = ""
    while n > 0:
        s = str(n % 8) + s
        n = n // 8
    return s
res=[]
for n in range(1,100000):
    N=n
    R=f(n)
    if n % 2 == 0:
        R = R+'10'
    else:
        R = R+'00'
    R = int(R,8)
    if R <=999:
        res.append(R)
print(res)
