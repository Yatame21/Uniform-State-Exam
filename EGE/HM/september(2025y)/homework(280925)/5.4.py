n = int(input())

for i in range(n):
    x = input()

    if i==0 or len(x) < mini:
        mini = len(x)

print(mini)

