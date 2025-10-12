a = [1, 15, -17, 6, 4, 16, 6, 7, -30, 9]

gen = sum(1 for i in a if 9<abs(i)<100 )
print(gen)