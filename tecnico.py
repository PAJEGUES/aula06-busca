# Arquivo: tecnico.py
# Exercício 6: técnico que precisa visitar 6 clientes e voltar à base (caixeiro-viajante).
# Estado correto: (local atual, conjunto de clientes já visitados)
from itertools import permutations

# Distâncias em km (matriz simétrica). Índice 0 = base, 1..6 = clientes.
LOCAIS = ['Base', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']
DIST = [
    [0, 12, 18, 25, 30, 22, 15],
    [12, 0, 10, 20, 28, 26, 17],
    [18, 10, 0, 11, 19, 24, 21],
    [25, 20, 11, 0, 9, 16, 23],
    [30, 28, 19, 9, 0, 10, 20],
    [22, 26, 24, 16, 10, 0, 8],
    [15, 17, 21, 23, 20, 8, 0],
]
CLIENTES = frozenset(range(1, 7))

estado_inicial = (0, frozenset())  # na base, ninguém visitado

def acoes(estado):
    """Ir para um cliente ainda não visitado; se todos foram visitados, voltar à base."""
    atual, visitados = estado
    faltam = CLIENTES - visitados
    if faltam:
        return sorted(faltam)
    if atual != 0:
        return [0]
    return []

def resultado(estado, destino):
    atual, visitados = estado
    if destino == 0:
        return (0, visitados)
    return (destino, visitados | {destino})

def teste_objetivo(estado):
    return estado[0] == 0 and estado[1] == CLIENTES

def custo_passo(estado, destino):
    return DIST[estado[0]][destino]

def busca_custo_uniforme(inicio):
    fronteira = [(0, inicio, [0])]  # (custo g, estado, rota)
    explorados = set()
    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        g, atual, rota = fronteira.pop(0)
        if teste_objetivo(atual):
            return rota, g, len(explorados)
        if atual not in explorados:
            explorados.add(atual)
            for destino in acoes(atual):
                proximo = resultado(atual, destino)
                if proximo not in explorados:
                    fronteira.append((g + custo_passo(atual, destino), proximo, rota + [destino]))
    return None, float('inf'), len(explorados)

def forca_bruta():
    """Confere a resposta testando as 6! = 720 ordens de visita."""
    melhor = None
    for ordem in permutations(range(1, 7)):
        rota = [0] + list(ordem) + [0]
        km = sum(DIST[rota[i]][rota[i + 1]] for i in range(len(rota) - 1))
        if melhor is None or km < melhor[1]:
            melhor = (rota, km)
    return melhor

if __name__ == '__main__':
    print(f'Estados com (local, visitados): 1 + 6 x 2^5 + 1 = {1 + 6 * 2 ** 5 + 1}')
    print('Estados usando só "cidade atual": 7  -> não guarda quem falta visitar\n')

    rota, km, explorados = busca_custo_uniforme(estado_inicial)
    print('Busca de custo uniforme com estado (local, visitados):')
    print(' -> '.join(LOCAIS[i] for i in rota), f'= {km} km  ({explorados} estados explorados)')

    rota_fb, km_fb = forca_bruta()
    print('\nConferência por força bruta (720 permutações):')
    print(' -> '.join(LOCAIS[i] for i in rota_fb), f'= {km_fb} km')

    # Se o estado fosse só a cidade atual, o conjunto de explorados impediria voltar à Base
    # e o teste de objetivo "estar na Base" já seria verdadeiro no estado inicial.
    print('\nCom estado = "cidade atual": teste de objetivo (estar na Base) já é verdadeiro no início -> rota vazia, 0 km.')
