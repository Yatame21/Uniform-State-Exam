n = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81**169 - 2*9**107 + 3017

def f27(x):
    r = 0
    while x > 0:
        if x%27:
            if x % 2 == 0 and x <= 25:
                r += 1
                x//=27
    return r

print(f27(n))