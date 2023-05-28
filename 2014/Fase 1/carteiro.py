# link da questão:
# https://olimpiada.ic.unicamp.br/pratique/ps/2014/f1/carteiro/


tempo = pos = a = 0

casa_para_entregas = input().split()
casa_para_entregas = list(map(int, casa_para_entregas))

n_casas = input().split()
n_casas = list(map(int, n_casas))

encomendas = input().split()
encomendas = list(map(int, encomendas))



while a < casa_para_entregas[1]:
    if n_casas[pos] == encomendas[a]:
        a += 1
    elif n_casas[pos]  < encomendas[a]:
        pos += 1 
        tempo += 1
    elif n_casas[pos] > encomendas[a]:
        pos -= 1
        tempo += 1
    

print(tempo)

    
# 5 5
# 1 5 10 20 40     n casas
# 10 20 10 40 1    n encomendas
# R = 10


# 3 4
# 50 80 100
# 80 80 100 50
# R= 4