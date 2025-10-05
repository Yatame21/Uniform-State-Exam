a = [2, 6, 3, 7, 10, 12, 15, 1, 20, 17]

chet = 0
nechet = 0

for i in a:
    if i % 2 == 0 :
        chet += i
    else:
        nechet += i

print(chet, nechet)