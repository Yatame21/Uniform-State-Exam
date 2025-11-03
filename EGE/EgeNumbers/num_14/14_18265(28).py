for p in range(28, 37):
    for s in range(10, 35):
        n1 = 27 * (p - 1) + 4
        n2 = 11 * (s + 2)
        n3 = 29 * p**4 + 3 * p**3 + 23 * p**2 + 20 * p + 4
        if n1 + n2 + n3 == 23593399:
            print(p*s)