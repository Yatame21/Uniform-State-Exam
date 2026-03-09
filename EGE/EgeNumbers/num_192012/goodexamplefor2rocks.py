def f(s1,s2,m):
    if s1+s2 <= 200 : return m%2 == 0
    if m==0 : return 0
    h = [f(s1 - 3,s2 - 4,m - 1), f(s1 - 8,s2 // 2,m - 1),f(s1 // 2 + s1 % 2,s2 - 10,m - 1)]
    # хорошйий пример с условием во втором условие мы округляем s2 // 2 до меньшего , а в третьем условии s1 // 2 + s1 % 2 до большего
    return any(h) if m %2 != 0 else all(h)

print('19)', [s for s in range(100,1000) if f(110,s,2)])
print('20)', [s for s in range(100,1000) if not f(110,s,1) and f(110,s,3)])
print('21)', [s for s in range(100,1000) if not f(110,s,2) and f(110,s,4)])
