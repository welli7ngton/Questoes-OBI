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
# 10:00 22:00 10:00 18:00

# Saída
# 600 2






p_A = input().split()
p_A  = list(map(str, p_A))


c_B = p_A[1]
p_B = p_A[2]
c_A = p_A[3]
p_A = p_A[0]

tempo_voo = []

tempo_voo.append(int(c_B[:2]) - int(p_A[:2]))
tempo_voo.append(int(c_A[:2]) - int(p_B[:2]))

if tempo_voo[0] > tempo_voo[1]:
    maior, menor = tempo_voo[0], tempo_voo[1]
else:
    maior, menor = tempo_voo[1], tempo_voo[0]

dif = 0
while True:
    if maior != menor:
        maior -= 1
        menor +=1 
        dif += 1
    else:
        break
    
    
print(dif)





