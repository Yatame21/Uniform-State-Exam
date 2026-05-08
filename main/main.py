res = []
for n in range(1,1000000):
    r=bin(n)[2:]
    ost = r[:-3]
    if n % 5 ==0 :
        r  = r+ost
   # else:
