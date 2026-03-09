from itertools import permutations,product

def f(x,y,z):
    return (x == z) or (x <= (y and z))

for x1,x2,x3 in product([0,1], repeat=3):
    t = (
        (0,0,x1,0),
        (1,x2,x3,0)
    )   

    if len(t) == len(set(t)):
        for p in permutations('xyz', r=3): 
            if all(f(**dict(zip(p,line))) == line[-1] for line in t):
                print(*p)