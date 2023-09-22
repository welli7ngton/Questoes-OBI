# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f2/catador/
# 1 2 0 8 4 2 9 8 1 3
# 9 5 10 6
def retorna_indices(n1, n2):
    soma = n2 + n1
    subt = n2 - n1
    if soma < 0:
        soma *= -1
    if subt < 0:
        subt *= -1

    return soma, subt


n, m = (input().split(" "))

conchas = [int(a) for a in (input().split(" "))]
indices = [int(a) - 1 for a in (input().split(" "))]
c = 0
while c < int(m):
    balde = indices[c]
    qtd_conchas = conchas[indices[c]]
    indice1, indice2 = retorna_indices(balde, qtd_conchas)
    maior = max(indice1, indice2)
    menor = min(indice1, indice2)
    # print(menor, maior)
    # try:
    if maior > len(conchas):
        maior = len(conchas) - 1
    for i in range(menor, maior + 1):
        conchas[i] -= 1
    c += 1
    # except IndexError:
    #     maior = len(conchas)
    #     continue

conchas = [i for i in conchas if i > 0]

print(sum(conchas))
# 1 2 0 8 4 2 9 8 1 3
# 9 5 10 6
