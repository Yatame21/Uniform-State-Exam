def f(n):
    s = ''
    while n > 0:
        s = str(n%7)+s
        n = n // 7
    return s
res=[]
for n in range(1,100000):
    N =n
    R=f(n)
    if n % 7 == 0:
        ch = R[-2:]
        R = R+ch
    else:
        ost = n%7
        mult = ost*2
        R = R + f(mult)
    R = int(R,7)
    if  R <220:
        res.append(N)
print(res)