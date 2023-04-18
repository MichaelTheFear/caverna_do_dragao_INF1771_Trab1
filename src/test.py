from itertools import combinations

lista = [1,2,3,4,5]
res = []
for i in range(1, len(lista)+1):
    for comb in combinations(lista, i):
        res.append(list(comb))

print(res)