Item 1) Porque é o objetivo que diz o que importa no problema. Primeiro o agente decide onde quer chegar (por exemplo, estar em Bucareste) e só depois dá para escolher quais estados e ações entram na formulação. Sem o objetivo não tem como saber o que é detalhe e o que não é, então não dá para fazer a abstração. Se o objetivo fosse conhecer a Romênia, as ações e o custo seriam outros, mesmo usando o mesmo mapa.

Item 2)
Estado: uma situação em que o mundo pode estar, por exemplo estar em Arad.
Espaço de estados: todos os estados que dá para alcançar a partir do estado inicial, ligados pelas ações. Na prática é um grafo.
Árvore de busca: a árvore que a busca vai montando, a raiz é o estado inicial e cada ramo é um caminho que foi testado.
Nó de busca: cada elemento dessa árvore, guarda o estado, o pai, a ação que gerou ele e o custo até ali.
Objetivo: o estado (ou estados) que o agente quer atingir, conferido pelo teste de objetivo.
Ação: o que o agente pode fazer num estado para ir para outro, tipo Ir(Sibiu).
Modelo de transição: a função RESULTADO(s, a), que diz em que estado o agente fica depois de fazer a ação a no estado s.
Fator de ramificação: o número máximo de filhos que um nó pode ter.

Item 3) O estado do mundo é a situação real, o carro realmente parado em Arad. A descrição de estado é como isso fica no computador, a string 'Arad' no código. O nó de busca é o que a busca cria, e além do estado guarda o pai, a ação e o custo. Isso é útil porque o mesmo estado pode aparecer em vários nós, chegando por caminhos diferentes (Arad -> Sibiu e Arad -> Zerind -> Oradea -> Sibiu são dois nós com o mesmo estado Sibiu). Por isso precisa do conjunto de visitados, e é seguindo os pais que dá para montar o caminho no final.

Item 4) Código no arquivo jarros.py.
Estado inicial: (0, 0), os dois jarros vazios.
Ações: encher o de 4, encher o de 3, esvaziar o de 4, esvaziar o de 3, despejar o de 4 no de 3 e despejar o de 3 no de 4.
Modelo de transição: encher deixa o jarro cheio, esvaziar deixa em 0, e despejar passa o que couber, ou seja, o menor valor entre o que tem no jarro de origem e o espaço que sobra no outro.
Teste de objetivo: um dos jarros com 2 litros.
Custo: cada ação custa 1.

O jarro de 4 pode ter de 0 a 4 litros e o de 3 de 0 a 3, então são 5 x 4 = 20 estados. Só que começando de (0, 0) só dá para chegar em 14 deles, porque sem marcação, depois de qualquer ação sempre tem um jarro cheio ou vazio. Os estados (1,1), (1,2), (2,1), (2,2), (3,1) e (3,2) nunca aparecem.

Uma solução com 4 ações: (0,0) -> enche o de 3 -> (0,3) -> despeja no de 4 -> (3,0) -> enche o de 3 -> (3,3) -> despeja no de 4 -> (4,2).

Item 5) Código no arquivo missionarios.py.
Estado: (missionários na margem esquerda, canibais na margem esquerda, lado do barco).
Estado inicial: (3, 3, E).
Ações: levar no barco 1M, 2M, 1C, 2C ou 1M e 1C para a outra margem.
Modelo de transição: tira as pessoas da margem onde está o barco, coloca na outra e o barco troca de lado. Só vale se em nenhuma margem tiver mais canibal que missionário (quando tiver missionário lá).
Teste de objetivo: (0, 0, D).
Custo: cada travessia custa 1.

São 32 combinações, 20 são válidas e 16 dá para alcançar a partir de (3, 3, E). O espaço de estados fica assim (cada ligação é uma travessia e dá para fazer nos dois sentidos):

```
                  (3,3,E)   inicio
                /    |    \
         (3,2,D)  (3,1,D)  (2,2,D)
          sem         \      /
         saida        (3,2,E)
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
                      (0,0,D)   objetivo
                         |
                      (0,1,E)
                     sem saida
```

A solução mais curta tem 11 travessias:
(3,3,E) -> (3,1,D) -> (3,2,E) -> (3,0,D) -> (3,1,E) -> (1,1,D) -> (2,2,E) -> (0,2,D) -> (0,3,E) -> (0,1,D) -> (1,1,E) -> (0,0,D)

Mesmo sendo pequeno é um bom exemplo porque obriga a pensar na formulação, escolher um estado que guarde só o necessário (quem está na margem esquerda e o lado do barco) e deixar de fora o que não importa, como o rio e o barco em si. Também tem estado repetido, dá para ir e voltar sem sair do lugar, o que mostra por que precisa guardar os visitados. E a solução não é óbvia para uma pessoa, porque em alguns momentos tem que voltar gente para trás e parece que está piorando.

Item 6) Código no arquivo tecnico.py.
O estado tem que ser (local atual, clientes que já foram visitados). Começa em (Base, nenhum visitado) e o objetivo é (Base, todos os 6 visitados). As ações são ir para um cliente que ainda não foi visitado, ou voltar para a base quando todos já foram, e o custo é a distância em km. Isso dá 194 estados (1 inicial + 6 x 2^5 + 1 final).

Se o estado for só a cidade atual, ele não guarda quem ainda falta visitar. Aí o próprio estado inicial já passa no teste de estar na base, e a solução seria não sair do lugar. Além disso, chegar no cliente 3 depois de ter passado por 2 clientes ou por 5 viraria o mesmo estado, e a busca ia descartar caminhos que na verdade são diferentes.
