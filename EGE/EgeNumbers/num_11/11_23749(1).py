# ma-? 2**i>=ma
from math import ceil
# ceil(2783*i/8)*3845627>=11*2**30
for i in range(10**6):
    if ceil(2783 * i / 8) * 3845627 >= 11 * 2 ** 30:
        print(i)
        break

# 2**8+1=257 2**9=512