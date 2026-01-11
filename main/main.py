


def f(a,b,m):
    if a+b >= 77: return m % 2 == 0
    if m == 0:return 0
    h = [f(a+1,b,m-1), f(a,b+1,m-1), f(a*2,b,m-1), f(a,b*2,m-1)]
    return any(h) if m%2 != 0 else any(h)

print([s for s in range(1,70)])
def f(s,m):
    if s <= 16: return m%2 == 0
    if m == 0:return 0
    h = [f(s-3,m-1), f(s-8,m-1), f(s//3,m-1)]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(17,100) if f(s,2)])
print([s for s in range(17,100) if not f(s,1) and f(s,3)])
print([s for s in range(17,100) if not f(s,2) and f(s,4)])


# pr