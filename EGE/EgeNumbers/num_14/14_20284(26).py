for x in range(0, 42):
    n1 = int('J',36)* 42**4 + 5 * 42 ** 3 + 6 * 42 ** 2 + 9 * 42 ** 1 + x
    n2 = 1 * 42 **3 + x * 42**2 + int('I',36) * 42**1 + 10
    res = n1+n2
    if res % 155 == 0:
        print(res // 155)
        break