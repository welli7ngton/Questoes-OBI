# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f1/cor/

class Grafo:
    def __init__(self, num_estacoes):
        self.num_estacoes = num_estacoes
        self.adjacencias = [[] for _ in range(num_estacoes + 1)]

    def adicionar_ligacao(self, estacao_origem, estacao_destino):
        self.adjacencias[estacao_origem].append(estacao_destino)

def dfs(grafo, estacao_atual, visitadas):
    visitadas.add(estacao_atual)

    for estacao_vizinha in grafo.adjacencias[estacao_atual]:
        if estacao_vizinha not in visitadas:
            dfs(grafo, estacao_vizinha, visitadas)

def contar_estacoes_passadas(grafo):
    estacoes_visitadas = set()
    dfs(grafo, 1, estacoes_visitadas)
    return len(estacoes_visitadas) - 1  # Excluindo a estação inicial

# Leitura da entrada
N, M = map(int, input().split())

# Criação do grafo
grafo = Grafo(N)

# Leitura das ligações e adição ao grafo
for _ in range(M):
    P, Q = map(int, input().split())
    grafo.adicionar_ligacao(P, Q)

# Contagem das estações alcançáveis
resultado = contar_estacoes_passadas(grafo)

# Impressão do resultado
print(resultado)

print(grafo)