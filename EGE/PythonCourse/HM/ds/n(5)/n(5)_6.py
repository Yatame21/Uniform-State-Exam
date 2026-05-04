def f(n):
    s = ''
    while n>0:
        s=str(n%3)+s
        n=n//3
    return s
res = []
for n in range(1,100000):
    N =n
    R = f(n)
    if n % 3 ==0 :
        R = '1'+R+'02'
    else:
        ost =n%3
        mult = ost *4
        R = R + f(mult)
    R = int(R,3)
    if R <100:
        res.append(N)
print(max(res))
