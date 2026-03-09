def f(s1,s2,m):
    if s1+s2  >= 79 : return m%2 == 0
    if m==0 : return 0
    h= [f(s1+1,s2,m-1),f(s1,s2+1,m-1),f(s1*3,s2,m-1),f(s1,s2*3,m-1)]
    return any (h) if m%2 != 0 else all(h)

#print('19)', [s for s in range(1,73) if f(6,s,2)])
print('20)', [s for s in range(1,73) if not f(6,s,1) and f(6,s,3)])
print('21)', [s for s in range(1,73) if not f(6,s,1) and f(6,s,2)])