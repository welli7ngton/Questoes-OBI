# link da questão:
# https://olimpiada.ic.unicamp.br/pratique/ps/2014/f2/voo/

'''
Por exemplo, um voo sai da Haquérnia às 10:00 horas e chega na Nerdínia às 22:00 horas, ao passo que outro voo sai da Nerdínia às 10:00 horas e chega na Haquérnia às 18:00 horas. Qual a explicação? Note que ambos os voos utilizam aeronaves idênticas, na mesma rota, um de ida, outro de volta. Na realidade, o voo dura 10 horas e Nerdínia fica em um fuso horário +2 horas à frente do fuso horário da Haquérnia (portanto o fuso horário de Haquérnia fica -2 horas à frente do fuso horário de Nerdínia).
'''

'''
Entrada
A entrada é composta de apenas uma linha, com 4 horários, separados por um espaço em branco. Esses horários envolvem voos entre duas cidades, A e B e são, respectivamente, p_A, c_B, p_B e c_A. O horário p_A indica a hora da partida de um voo de A para B, hora local de A. O horário c_B indica a hora de chegada do mesmo voo na cidade B, hora local de B. O horário p_B é a hora de partida do voo de volta, de B para A, hora local de B. O horário c_A é a hora de chegada do voo de volta, hora local de A.
Saída
A saída consiste de uma linha, informando a duração do voo em minutos e quantas horas B está à frente de A, em termos de fusos horários. Os dois valores devem ser separados por um espaço em branco.
'''

# Entrada
# Pa    Cb                             Pb    Ca                diferença de fusos:
# 18:00 12:00                          18:00 14:00                    11hrs
# 18:00 01:00 hora a                   07:00 14:00 hora a      tempo de voo:
# 05:00 12:00 hora b                   18:00 01:00 hora b             7hrs

    



p_A = input().split()
p_A  = list(map(str, p_A))


c_B = p_A[1]
p_B = p_A[2]
c_A = p_A[3]
p_A = p_A[0]

horarios = []

horarios.append(int(p_A[:2]))
horarios.append(int(c_B[:2]))
horarios.append(int(p_B[:2]))
horarios.append(int(c_A[:2]))

xa = horarios[0] - horarios[1]
xb = horarios[2] - horarios[3]

if horarios[0] > horarios[1] and horarios[2] > horarios[3]:
    delta = 0

    if xa > xb:
        while xa != xb:
            xa -= 1
            xb += 1
            delta += 1
        delta = delta * -1 if xb < 0 else delta
        
    else:
        while xa != xb:
            xa += 1
            xb -= 1
            delta += 1
        delta = delta * -1 if xb > 0 else delta
    
    delta = xa
    

    pbha = (horarios[3] + delta) - 12
    fuso = horarios[2] - pbha
    print(fuso)




else:

    delta = 0

    if xa > xb:
        while xa != xb:
            xa -= 1
            xb += 1
            delta += 1
        delta = delta * -1 if xb > 0 else delta
        
    else:
        while xa != xb:
            xa += 1
            xb -= 1
            delta += 1
        delta = delta * -1 if xb < 0 else delta


    cbha = horarios[1] + delta
        
    t_voo = (cbha - horarios[0]) * 60
    print(t_voo, delta * -1)  


  



