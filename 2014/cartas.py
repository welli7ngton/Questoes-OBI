# link da questão:
# https://olimpiada.ic.unicamp.br/pratique/ps/2014/f1/cartas/


cartas = input().split(" ")

cartas = list(map(int, cartas))

for a in range(0, len(cartas) - 1):
    if cartas[a] < cartas[a + 1]:
        r = True
    else:
        r = False
        break

if r is False:
    for a in range(0, len(cartas) - 1):
        if cartas[a + 1] < cartas[a]:
            r = True
        else:
            r = False
            print("N")
            break
    if r is True:
        print("D")

else:
    print("C")
