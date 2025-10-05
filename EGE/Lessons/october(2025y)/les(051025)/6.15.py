a = [10,20,10]

maxi = a[0]

for i in a:
    if a.count(i) > a.count(maxi) or i < maxi and a.count(i) == a.count(maxi):
        maxi = i

print(maxi)