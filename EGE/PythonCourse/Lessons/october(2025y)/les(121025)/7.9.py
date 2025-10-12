a = ['abba', 'aaacbb', 'abab', 'abc', 'baacac']

print(max(a, key=lambda x: x.count('a')))