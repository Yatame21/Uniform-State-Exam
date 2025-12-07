# 2 ** i  >= 37
from math import ceil
# ceil(k*6/8)*3548>12*2**10
for k in range(10**6):
    if ceil(k*6/8)*3548>12*2**10:
        print(k)
        break
