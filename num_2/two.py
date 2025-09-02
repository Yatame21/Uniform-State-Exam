# ((y → x) ≡ (x → w)) ∧ (z ∨ x) 
from itertools import product,permutations

def f(x, y, z, w): # tyt
    return ((y <= x) == (x <= w)) and (z or x) # tyt

for x1,x2,x3,x4,x5,x6 in product([0,1], repeat=6): # tyt

    t = ( # tyt
        (0,x1,x2,0,1),
        (0,0,0,x3,1),
        (x4,x5,0,x6,1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4): # tyt
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)