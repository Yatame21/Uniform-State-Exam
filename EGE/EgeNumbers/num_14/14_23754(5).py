def f11(x):
    r=0
    while x>0:
        if x%11==0:
            r+=1
        x//=11
    return r
for x in range(3000,0,-1):
    n=9*11**210+8*11**150-x
    if f11(n)==60:
        print(x)
        break

# 2992