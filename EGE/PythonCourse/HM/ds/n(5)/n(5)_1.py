res=[]
for n in range(1,10000):
    r=bin(n)[2:]
    if n % 2 ==0:
        r = '1'+r+'1'
    else:
        r = r+'10'
    r=int(r,2)
    if r>179:
        res.append(n)

print(min(res))