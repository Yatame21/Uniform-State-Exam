for x in range(16,37):
    n1 = 1 * x **4 + 7 * x**3 + 4 * x**2 + 9 *x + 6
    n2 = 9 * x ** 4 + 1 * x ** 3 + int('F',36) * x **2 + 8 * x + 3
    n3 = int('D',36) * x ** 4 + 9 * x ** 3 + 5 * x ** 2 + 4 * x + 3
    r = n1 + n2 + n3
    if r % 12 == 0 :
        print(r // 12)
        break
