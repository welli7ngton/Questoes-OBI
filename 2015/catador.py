# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f2/catador/

def retorna_indices(n1, n2):
    soma = n1 + n2
    subt = n1 - n2
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
    # print("balde", balde)
    # print("qtd", qtd_conchas)
    indice1, indice2 = retorna_indices(balde, qtd_conchas)

    maior = max(indice1, indice2)
    menor = min(indice1, indice2)
    print(menor, maior)
    for i in range(menor, maior):
        conchas[i] -= 1
        # print(conchas[i])

    c += 1
print("conchas final", sum(conchas))
