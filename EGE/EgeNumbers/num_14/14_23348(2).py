n = 77 * 81 ** 2031 + 23 * 729 ** 1037 - 7 * 9 ** 3023

def f81(x):
    r=0
    while x > 0:
        if (x%81)%4 == 0:
            r+=1
        x//=81
    return r
print(f81(n))
    