def f(s,m,step):
    if s >= 231 : return m%2 ==0
    if m== 0 : return 0
    if step == 'P':
        h=[f(s+3,m-1,'P'),f(s*3,m-1,'P')]
    else:
        h=[f(s+5,m-1,'V'),f(s*3,m-1,'V')]
    return any(h) if m%2 != 0 else all(h)

print('19)', [s for s in range(1,121) if f(s,2,'P')])

print('20)', [s for s in range(1,121) if not f(s,1,'P') and f(s,3,'P')])

print('21)', [s for s in range(1,121) if not f(s,2,'P') and f(s,4,'P')])