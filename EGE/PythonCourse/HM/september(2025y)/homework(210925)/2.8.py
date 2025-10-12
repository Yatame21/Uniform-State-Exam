x= int(input())

x1 = x // 1000
x2 = (x // 100) % 10
x3 = (x // 10) % 10
x4 = x % 10

desatki = x3
sotni = x2
summa = x1+x2+x3+x4
proizvedenie = x1*x2*x3*x4

print(desatki,sotni,summa,proizvedenie)