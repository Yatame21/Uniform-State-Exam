def f(n):
    s =''
    while n > 0:
        s = str(n%3) +s
        n //=3
    return s
res = []
for n in range(1,100000):
    N= n
    R = f(n)
    if n % 3 == 0:
        ost = R[-2:]
        R = R + ost
    else:
        ost = n % 3
        mult = ost *5
        R = R+f(mult)
    R = int(R,3)
    if R > 150:
        res.append(R)
print(min(res))