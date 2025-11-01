from string import digits,ascii_letters
alf = digits+ascii_letters
for x in alf[:21]:
    n1 = int('82934'+x+'2',21)
    n2= int('2924'+x+x+'7',21)
    n3= int('67564'+x+'8',21)
    if (n1+n2+n3)%20 == 0:
        print((n1+n2+n3)//20)
        break