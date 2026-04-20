res=[]
for n in range(1,10000):
    r=bin(n)[2:]
    if n % 2==0:
        r='10'+r
    else:
        r= '1'+ r+'01'
    r = int(r,2)
    if n <=12:
        res.append(r)
print(max(res))
#https://education.yandex.ru/ege/inf/task/6e679e3e-d6c0-4c26-9e5e-d6b89730c238