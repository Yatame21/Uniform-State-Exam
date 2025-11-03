from string import digits, ascii_uppercase

alf = digits + ascii_uppercase
for x in alf[24::-1]:
    n1 = int("A4" + x + "7F2", 25)
    n2 = int("N" + x + "G5" + x + "H", 25)
    n3 = int("74" + x + "M26", 25)
    to = n1 + n2 + n3
    if to % 24 == 0:
        print(to // 24)
        break