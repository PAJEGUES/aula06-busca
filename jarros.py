# Arquivo: jarros.py
# Exercício 4: problema dos dois jarros (4 litros e 3 litros) formulado com os cinco componentes.

CAP_4 = 4
CAP_3 = 3

# 1. Estado inicial: os dois jarros vazios -> (litros no jarro de 4, litros no jarro de 3)
estado_inicial = (0, 0)

def acoes(estado):
    """2. AÇÕES(s): só devolve as ações que mudam alguma coisa no estado."""
    x, y = estado
    lista = []
    if x < CAP_4: lista.append('Encher4')
    if y < CAP_3: lista.append('Encher3')
    if x > 0: lista.append('Esvaziar4')
    if y > 0: lista.append('Esvaziar3')
    if x > 0 and y < CAP_3: lista.append('Despejar4em3')
    if y > 0 and x < CAP_4: lista.append('Despejar3em4')
    return lista

def resultado(estado, acao):
    """3. Modelo de transição RESULTADO(s, a)."""
    x, y = estado
    if acao == 'Encher4': return (CAP_4, y)
    if acao == 'Encher3': return (x, CAP_3)
    if acao == 'Esvaziar4': return (0, y)
    if acao == 'Esvaziar3': return (x, 0)
    if acao == 'Despejar4em3':
        quantidade = min(x, CAP_3 - y)
        return (x - quantidade, y + quantidade)
    if acao == 'Despejar3em4':
        quantidade = min(y, CAP_4 - x)
        return (x + quantidade, y - quantidade)
    return estado

def teste_objetivo(estado):
    """4. Teste de objetivo: exatamente 2 litros em um dos jarros."""
    return estado[0] == 2 or estado[1] == 2

def custo_passo(estado, acao, proximo):
    """5. Custo de passo: cada ação custa 1."""
    return 1

def busca_largura(inicio):
    fronteira = [(inicio, [inicio], [])]  # (estado, caminho de estados, ações)
    visitados = set()
    while fronteira:
        atual, caminho, plano = fronteira.pop(0)
        if teste_objetivo(atual):
            return caminho, plano
        if atual not in visitados:
            visitados.add(atual)
            for acao in acoes(atual):
                proximo = resultado(atual, acao)
                if proximo not in visitados:
                    fronteira.append((proximo, caminho + [proximo], plano + [acao]))
    return None, None

def estados_alcancaveis(inicio):
    visitados = {inicio}
    fila = [inicio]
    while fila:
        atual = fila.pop(0)
        for acao in acoes(atual):
            proximo = resultado(atual, acao)
            if proximo not in visitados:
                visitados.add(proximo)
                fila.append(proximo)
    return visitados

if __name__ == '__main__':
    todos = [(x, y) for x in range(CAP_4 + 1) for y in range(CAP_3 + 1)]
    alcancaveis = estados_alcancaveis(estado_inicial)

    print(f'Estados possíveis (5 x 4): {len(todos)}')
    print(f'Estados alcançáveis a partir de (0, 0): {len(alcancaveis)}')
    print(sorted(alcancaveis))
    print(f'Não alcançáveis: {sorted(set(todos) - alcancaveis)}')

    caminho, plano = busca_largura(estado_inicial)
    print('\nSolução encontrada (busca em largura):')
    for i, acao in enumerate(plano):
        print(f'{caminho[i]} --{acao}--> {caminho[i + 1]}')
    print(f'Custo do caminho: {len(plano)} ações')
