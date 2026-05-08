def f(n):
    s = ''
    while n > 0:
        s = str(n%3)+s
        n //=3
    return s
res=[]
for n in range(100000,1,-1):
    N=n
    R=f(n)
    R= ''.join(sorted(R)[::-1])
    R = R + R[0]
    R = int(R,3)
    if R <1200:
        res.append(R)
print(max(res))

#https://education.yandex.ru/ege/inf/training/5/task/1?examTaskId=2308aff6-3610-4a99-8d93-fe28a61f5e7b&examTaskNumber=5&taskId=afe8a9d0-8162-4f92-9e87-1c2dc7265290&categoryId=e983ac00-7a01-494f-aab0-d495ba630d5d