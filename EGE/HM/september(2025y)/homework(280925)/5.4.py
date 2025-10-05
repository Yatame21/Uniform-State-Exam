n = int(input())

mini = 0

for i in range(n):
    x = input()
    ct = len(x)
    if ct < mini:
        mini = ct

print(mini)

