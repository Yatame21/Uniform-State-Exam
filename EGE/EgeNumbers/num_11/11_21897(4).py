# 2 ** i >= ma
from math import ceil
# ceil(246*i/8)*703569<=77*2**20

for i in range(10**6,0,-1):
    if ceil(246*i/8)*703569<=77*2**20:
        print(i)
        break
