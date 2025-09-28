x = "БАБАВГВДАБАВ"
ct = 0

for i in range(len(x) - 1):
    if x[i] in"БВГД" and x[i + 1] in "АЕ":
        ct += 1
print(ct)

#the second method
ct = 0
for s in "БВГД":
    for d in "АЕ":
        ct += x.count(s + d)
print(ct)

