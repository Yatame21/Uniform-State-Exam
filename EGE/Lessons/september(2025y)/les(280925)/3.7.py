x = int(input())

x1 = x // 1000
x2 = (x // 100) % 10
x3 = (x // 10) % 10
x4 = x % 10

if x1 != x2 and x1 != x3 and x1 != x4 and x2!= x3 and x2 != x4 and x3 != x4:
    print("yes")
else:
    print("no")