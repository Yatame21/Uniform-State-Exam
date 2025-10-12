a = [100, 1, 54, 12]

a.sort()
step = a[1] - a[0]

for i in range(len(a) - 1):
    if a[i+1] - a[i] != step:
        print("no")
        break

else:
    print("yes")