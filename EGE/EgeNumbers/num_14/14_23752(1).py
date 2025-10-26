n=2*2187**2020+729**2021-2*243**2022+81**2023-2*27**2024-6561

def f27(x):
    r=0
    while x>0:
        if x%27>9:
            r+=1
        x//=27
    return r

print(f27(n))
# 3367

print(bin(29)[2:],oct(29),hex(29))

def f2_9(x,osn):
    r=''
    while x>0:
        r=str(x%osn)+r
        x//=osn
    return r
print(f2_9(29,2))


from string import digits,ascii_lowercase


def f2_36(x,osn):
    alf=digits+ascii_lowercase
    r=''
    while x>0:
        r=alf[x%osn]+r
        x//=osn
    return r

n27=f2_36(n,27)
print(sum(1 for d in n27 if int(d,27)>9))