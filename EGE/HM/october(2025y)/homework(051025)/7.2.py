def tr(a, b, c):
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area

print(tr(3, 4, 5))