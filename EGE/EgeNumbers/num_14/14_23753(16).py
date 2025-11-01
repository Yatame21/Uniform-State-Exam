from string import digits,ascii_lowercase
alf=digits+ascii_lowercase
for x in alf[:29][::-1]:
    # если наибольшое то [::-1]:
    n1=int('923'+x+'874',29)
    n2=int('524'+x+'6152',29)
    if (n1+n2)%28==0:
        print((n1+n2)//28)
        break
