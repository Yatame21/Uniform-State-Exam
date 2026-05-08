from itertools import product
k=0
for i in product(sorted('ЦАПЛЯ'),repeat=5):
    s=''.join(i)
    k+=1
    if s.count("А")==1 and s.count('Ц') == 2 and s.count('Л')== 0:
        print(k)