res =[]

from string import digits,ascii_lowercase
alf = digits+ascii_lowercase
for x in alf[:21]:
    for y in alf[:21]:
        n1 = int('943697'+x+'21',21)
        n2 = int('2'+y+'9253',21)
        if(n1-n2)%20 == 0:
            res.append([int(x,21)-int(y,21) ,(n1 - n2) // 20] )
res.sort()
print(res)