d = 10 ** 9 + 7

def md(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def cfc(n, m):
    if m == 1:
        return 0
    ans = m * md(m - 1, 2 * n - 1, d)
    return ans % d
n, m = map(int, input().split())
print(cfc(n, m))