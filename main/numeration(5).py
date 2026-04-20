from string import ascii_uppercase
d = '0123456789' + ascii_uppercase
def f(x,n):
    r = ''
    if x == 0:
        return '0'
    while x > 0:
        r +=d[x%n]
        x//=n
    return r[::-1]

print(f(564230,24))

print(int('10',2))