# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f1/divisores/


def ocorrencia(l=[],exp=[],c=0, p=2,contador=0):
    while True:
        if p not in l:
            p += 1
        break
        
    if c == len(l) + 1:
        return exp
    
    for numero in l:
        if numero == p:
            contador +=1
    if contador > 0:
        exp.append(contador)
        
    c += 1
    p += 1    
    return ocorrencia(l,exp,c,p)


n = int(input())

primos = []

div = 2
while n != 1:
    if n %div == 0:
        n = n/div
        primos.append(div)
    else:
        div += 1

exp = ocorrencia(primos)

r = 1
for a in range(0,len(exp)):
    
    r *= exp[a] + 1

print(r)