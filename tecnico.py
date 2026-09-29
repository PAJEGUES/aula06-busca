# Arquivo: tecnico.py
# Estado = (local atual, clientes ja visitados)

LOCAIS = ['Base', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']

# distancias em km, 0 = base
DIST = [
    [0, 14, 22, 9, 31, 18, 26],
    [14, 0, 12, 17, 24, 29, 11],
    [22, 12, 0, 20, 10, 27, 15],
    [9, 17, 20, 0, 25, 8, 30],
    [31, 24, 10, 25, 0, 19, 13],
    [18, 29, 27, 8, 19, 0, 23],
    [26, 11, 15, 30, 13, 23, 0],
]
CLIENTES = frozenset(range(1, 7))

def acoes(estado):
    atual, visitados = estado
    faltam = CLIENTES - visitados
    if faltam:
        return sorted(faltam)
    if atual != 0:
        return [0]  # todos visitados, volta pra base
    return []

def resultado(estado, destino):
    atual, visitados = estado
    if destino == 0:
        return (0, visitados)
    return (destino, visitados | {destino})

def objetivo(estado):
    return estado[0] == 0 and estado[1] == CLIENTES

def custo_uniforme(inicio):
    fronteira = [(0, inicio, [0])]  # (km, estado, rota)
    explorados = set()
    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        km, atual, rota = fronteira.pop(0)
        if objetivo(atual):
            return rota, km
        if atual not in explorados:
            explorados.add(atual)
            for destino in acoes(atual):
                proximo = resultado(atual, destino)
                if proximo not in explorados:
                    fronteira.append((km + DIST[atual[0]][destino], proximo, rota + [destino]))
    return None, float('inf')

if __name__ == '__main__':
    print('Quantidade de estados:', 1 + 6 * 2 ** 5 + 1)

    rota, km = custo_uniforme((0, frozenset()))
    print(' -> '.join(LOCAIS[i] for i in rota))
    print(f'{km} km')
