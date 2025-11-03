def f(s,c,m):
    if s>=42:
        return c%2==m%2
    if c==m:
        return 0
    lv=[f(s+1,c+1,m),f(s+3,c+1,m),f(s*2,c+1,m)]
    return any(lv) if (c+1)%2==m%2 else all(lv) # при выигрышных стратегиях
    # return any(lv) if (c+1)%2==m%2 else any(lv) # при неудачных ходах

for s in range(1,42):
    for m in range(1,5):
        if f(s,0,m):
            if m==3 or m==4:
                print(s,m)
            break
# 19) 11
# 20) 10, 17, 19
# 21) 16