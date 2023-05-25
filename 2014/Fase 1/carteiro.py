'''
A primeira linha contém dois inteiros, N e M, respectivamente o número de casas e o número de encomendas. A       segunda linha contém N inteiros em ordem estritamente crescente, indicando os números das casas. A terceira linha contém M inteiros indicando os números das casas onde as encomendas devem ser entregues, na ordem dada na entrada.
'''
cont = pos = i = 0

casa_entregas = input().split()
casa_entregas = list(map(int, casa_entregas))

n_casas = input().split()
n_casas = list(map(int, n_casas))

encomendas = input().split()
encomendas = list(map(int, encomendas))


for i in range(0, len(encomendas)):
    if n_casas[pos] == encomendas[i]:
        i += 1
    elif n_casas[pos] < encomendas[i]:
        pos +=1
        cont +=1
    elif n_casas[pos] > encomendas[i]:
        pos -=1
        cont +=1

print(cont)

# 5 5
# 1 5 10 20 40
# 10 20 10 40 1
# R = 10