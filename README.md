Item 1) Porque o objetivo é o que diz o que importa no problema. Primeiro o agente decide onde quer chegar (por exemplo, "estar em Bucareste"), e só depois ele consegue escolher quais estados e ações precisam entrar na formulação. Sem o objetivo ele não sabe o que é detalhe irrelevante, então não tem como fazer a abstração. Se o objetivo fosse "conhecer a Romênia", as ações e o custo seriam outros, mesmo com o mesmo mapa.

Item 2)
- Estado: uma situação em que o mundo (ou o agente) pode estar, por exemplo "estar em Arad".
- Espaço de estados: o conjunto de todos os estados que dá para alcançar a partir do estado inicial, ligados pelas ações. Na prática é um grafo.
- Árvore de busca: a árvore que o algoritmo vai montando enquanto procura a solução, a raiz é o estado inicial e cada ramo é um caminho testado.
- Nó de busca: cada elemento da árvore de busca, ele guarda o estado, o nó pai, a ação que gerou e o custo do caminho até ali.
- Objetivo: o estado (ou conjunto de estados) que o agente quer atingir, verificado pelo teste de objetivo.
- Ação: o que o agente pode fazer em um estado para ir para outro, por exemplo "Ir(Sibiu)".
- Modelo de transição: a função RESULTADO(s, a) que diz em qual estado o agente fica depois de fazer a ação a no estado s.
- Fator de ramificação: o número máximo de filhos (sucessores) que um nó pode ter.

Item 3) O estado do mundo é a situação real (o carro realmente parado em Arad). A descrição de estado é como a gente representa isso no computador (a string 'Arad' no código). O nó de busca é a estrutura que a busca cria, e que além do estado guarda o pai, a ação e o custo. A distinção é útil porque o mesmo estado pode aparecer em vários nós diferentes, chegando por caminhos diferentes (Arad -> Sibiu e Arad -> Zerind -> Oradea -> Sibiu são dois nós com o mesmo estado Sibiu). É por isso que existe o conjunto de visitados e que conseguimos reconstruir o caminho seguindo os pais.

Item 4) Código no arquivo "jarros.py". Print no arquivo: "Prints_Aula06.pdf".
- Estado inicial: (0, 0), os dois jarros vazios.
- Ações: Encher4, Encher3, Esvaziar4, Esvaziar3, Despejar4em3 e Despejar3em4.
- Modelo de transição: encher deixa o jarro na capacidade máxima, esvaziar deixa em 0, e despejar passa min(o que tem no jarro de origem, o espaço livre no jarro de destino).
- Teste de objetivo: x = 2 ou y = 2.
- Custo de caminho: cada ação custa 1, então o custo é o número de ações.

Quantidade de estados: x vai de 0 a 4 e y vai de 0 a 3, então são 5 x 4 = 20 estados. Mas partindo de (0, 0) só 14 são alcançáveis, porque como não tem marcação, sempre um dos jarros fica cheio ou vazio depois de cada ação (os estados (1,1), (1,2), (2,1), (2,2), (3,1) e (3,2) nunca aparecem).

Uma solução com 4 ações: (0,0) -> Encher3 -> (0,3) -> Despejar3em4 -> (3,0) -> Encher3 -> (3,3) -> Despejar3em4 -> (4,2).

Item 5) Código no arquivo "missionarios.py". Print no arquivo: "Prints_Aula06.pdf".
- Estado: (missionários na margem esquerda, canibais na margem esquerda, lado do barco).
- Estado inicial: (3, 3, E).
- Ações: levar no barco 1M, 2M, 1C, 2C ou 1M+1C para a outra margem.
- Modelo de transição: tira as pessoas da margem onde o barco está e coloca na outra, e o barco troca de lado. Só vale se em nenhuma margem os canibais forem mais que os missionários (quando tiver missionário lá).
- Teste de objetivo: (0, 0, D).
- Custo de caminho: cada travessia custa 1.

Das 32 combinações, 20 são válidas e 16 são alcançáveis a partir de (3, 3, E). Espaço de estados completo (cada linha é uma travessia, que pode ser feita nos dois sentidos):

```
                  (3,3,E)   INICIAL
                /    |    \
         (3,2,D)  (3,1,D)  (2,2,D)
          [beco]      \      /
                      (3,2,E)
                         |
                      (3,0,D)
                         |
                      (3,1,E)
                         |
                      (1,1,D)
                         |
                      (2,2,E)
                         |
                      (0,2,D)
                         |
                      (0,3,E)
                         |
                      (0,1,D)
                       /    \
                 (1,1,E)  (0,2,E)
                       \    /
                      (0,0,D)   OBJETIVO
                         |
                      (0,1,E)
                       [beco]
```

Solução ótima com 11 travessias:
(3,3,E) -> (3,1,D) -> (3,2,E) -> (3,0,D) -> (3,1,E) -> (1,1,D) -> (2,2,E) -> (0,2,D) -> (0,3,E) -> (0,1,D) -> (1,1,E) -> (0,0,D)

Mesmo sendo pequeno, é um bom exemplo porque obriga a pensar na formulação: escolher uma boa representação de estado (só contar quem está na margem esquerda e o lado do barco), abstrair o que não importa (o rio, a cor do barco) e tratar restrições nas ações. Também tem estados repetidos (dá para ir e voltar sem sair do lugar), então mostra por que precisa da busca em grafo com visitados. E a solução não é óbvia para uma pessoa, porque tem que voltar pessoas para trás, parecendo que está piorando.

Item 6) Código no arquivo "tecnico.py". Print no arquivo: "Prints_Aula06.pdf".
O estado precisa ser o par (local atual, conjunto de clientes já visitados). O estado inicial é (Base, {}) e o objetivo é (Base, {C1, C2, C3, C4, C5, C6}). As ações são ir para um cliente que ainda não foi visitado, ou voltar à base quando todos já foram visitados, e o custo de passo é a distância em km. Isso dá 194 estados (1 inicial + 6 x 2^5 + 1 final).

Usar só "cidade atual" como estado está errado porque o estado não guarda quem ainda falta visitar. Assim o estado inicial (Base) já passaria no teste de objetivo "estar na Base" e a solução seria não sair do lugar. Além disso, chegar em C3 depois de visitar 2 clientes ou depois de visitar 5 viraria o mesmo estado, e o conjunto de visitados ia descartar caminhos que são diferentes de verdade, ou então não teria como saber quando parar.
