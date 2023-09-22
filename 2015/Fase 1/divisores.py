# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f1/divisores/


def ocorrencia(_l=[], exp=[], c=0, p=2, contador=0):
    while True:
        if p not in _l:
            p += 1
        break

    if c == len(_l) + 1:
        return exp

    for numero in _l:
        if numero == p:
            contador += 1
    if contador > 0:
        exp.append(contador)

    c += 1
    p += 1
    return ocorrencia(_l, exp, c, p)


def prim(n, _l=[], div=2):
    if n == 1:
        return _l

    if n % div == 0:
        n = n/div
        _l.append(div)

    else:
        div += 1

    return prim(n, _l, div)


n = int(input())

exp = ocorrencia(prim(n))

r = 1
for a in range(0, len(exp)):

    r *= exp[a] + 1

print(r)
