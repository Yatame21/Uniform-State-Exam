from itertools import product
k=0
e=0
l=0
for i in product(sorted('БЮДЖЕТНИК'),repeat=6):
    s=''.join(i)
    k+=1
    if s == 'БЮДЖЕТ':
        break

    for i in "БДЖТНК":
        s = s.replace(i, 'j')
    for i in "ЮЕИ":
        s = s.replace(i, 'n')
    if "jj" not in s and 'nn' not in s:
        l += k

print(l)
#https://education.yandex.ru/ege/inf/training/8/task/1?examTaskId=8c19415d-5b26-4b40-a7ec-f879ec5ca2b7&examTaskNumber=8&taskId=a835b02e-7ae7-480c-a0cf-866d4a013e09&categoryId=9741e20f-d7f2-4e1b-b8d7-2f3613dd68dd