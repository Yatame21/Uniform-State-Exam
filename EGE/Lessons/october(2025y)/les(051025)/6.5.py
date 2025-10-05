a = ['ааа', 'бб', 'ввввв', 'ггггг', 'ддд', 'ееее', 'жжжжж', 'з']

maxi = a[0]


for i in a:
    if len(i) >= len(maxi):
        maxi = i

print(maxi)