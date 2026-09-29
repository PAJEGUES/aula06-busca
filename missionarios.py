# Arquivo: missionarios.py
# Estado: (missionários na margem esquerda, canibais na margem esquerda, lado do barco)
# Barco 'E' = margem esquerda, 'D' = margem direita.

TOTAL = 3
VIAGENS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # (missionários, canibais) no barco

estado_inicial = (3, 3, 'E')
estado_objetivo = (0, 0, 'D')

def valido(m, c):
    """Canibais não podem ser mais numerosos que missionários em nenhuma margem (se houver missionário)."""
    if m < 0 or c < 0 or m > TOTAL or c > TOTAL:
        return False
    if m > 0 and c > m:  # margem esquerda
        return False
    if (TOTAL - m) > 0 and (TOTAL - c) > (TOTAL - m):  # margem direita
        return False
    return True

def sucessores(estado):
    m, c, barco = estado
    lista = []
    for dm, dc in VIAGENS:
        if barco == 'E':
            novo = (m - dm, c - dc, 'D')
        else:
            novo = (m + dm, c + dc, 'E')
        if valido(novo[0], novo[1]):
            lista.append((f'Levar({dm}M,{dc}C)', novo))
    return lista

def espaco_de_estados(inicio):
    """Gera todos os estados alcançáveis e as arestas entre eles."""
    visitados = {inicio}
    fila = [inicio]
    arestas = []
    while fila:
        atual = fila.pop(0)
        for acao, proximo in sucessores(atual):
            arestas.append((atual, acao, proximo))
            if proximo not in visitados:
                visitados.add(proximo)
                fila.append(proximo)
    return visitados, arestas

def busca_largura(inicio, objetivo):
    fronteira = [(inicio, [inicio])]
    visitados = set()
    while fronteira:
        atual, caminho = fronteira.pop(0)
        if atual == objetivo:
            return caminho
        if atual not in visitados:
            visitados.add(atual)
            for acao, proximo in sucessores(atual):
                if proximo not in visitados:
                    fronteira.append((proximo, caminho + [proximo]))
    return None

def desenhar(estado):
    m, c, barco = estado
    esquerda = 'M' * m + 'C' * c
    direita = 'M' * (TOTAL - m) + 'C' * (TOTAL - c)
    rio = '[B]~~~~~~' if barco == 'E' else '~~~~~~[B]'
    return f'{esquerda:>6} {rio} {direita:<6}'

if __name__ == '__main__':
    todos = [(m, c, b) for m in range(TOTAL + 1) for c in range(TOTAL + 1) for b in 'ED']
    validos = [e for e in todos if valido(e[0], e[1])]
    estados, arestas = espaco_de_estados(estado_inicial)

    print(f'Combinações possíveis (4 x 4 x 2): {len(todos)}')
    print(f'Estados válidos: {len(validos)}')
    print(f'Estados alcançáveis a partir de (3, 3, E): {len(estados)}')

    print('\nEspaço de estados:')
    for origem, acao, destino in arestas:
        print(f'{origem} --{acao}--> {destino}')

    caminho = busca_largura(estado_inicial, estado_objetivo)
    print(f'\nSolução ótima com {len(caminho) - 1} travessias:')
    for estado in caminho:
        print(f'{str(estado):14} {desenhar(estado)}')
