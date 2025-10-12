a = ['ааа', 'бб', 'в', 'ггггг', 'ддд', 'ееее', 'жжжжж', 'з']

min = [0]

for i in a:
    if len(i) <= len(min):
        min = i

print(min)