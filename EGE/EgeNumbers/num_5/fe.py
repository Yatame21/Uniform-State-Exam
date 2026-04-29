def f(x):
    r = ''
    while x > 0:
        r += str(x % 8)
        x//=8
    return r[::-1]

def g(n):
    r = f(n)
    for i in '0246':
        r = r.replace(i,"")
    r = int(r,8)
    return r
print(g(115))