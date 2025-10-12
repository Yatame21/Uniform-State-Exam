s = "Я сдам ЕГЭ на сто баллов"
for i in ",?!;":
    s = s.replace(i, ' ')
words = s.split()
long = words[0]
for word in words:
    if len(word) > len(long):
        long = word
print(long)