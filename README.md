# DominoGame

## Objetivo
O objetivo deste miniprojeto é implementar um sistema de gerenciamento de peças de dominó utilizando listas encadeadas em Python. O projeto visa fornecer uma estrutura de dados eficiente para manipular as peças do jogo de dominó, permitindo
a realização de operações como embaralhar, distribuir, jogar e verificar o estado do jogo.

## Descrição do Problema
O jogo de dominó é um jogo de mesa amplamente conhecido, onde os jogadores devem combinar peças com números
correspondentes em suas extremidades. Neste projeto, você será responsável por criar um programa que simula a
manipulação das peças de dominó em um jogo. O programa deve ser capaz de criar um conjunto de peças de dominó,
distribuí-las aos jogadores, permitir que os jogadores joguem suas peças e verificar o estado do jogo para determinar o
vencedor.

## Requisitos Funcionais
1. Criação de Peças de Dominó: O programa deve ser capaz de criar um conjunto completo de peças de dominó, cada uma
com dois valores numéricos de 0 a 6.
2. Embaralhamento das Peças: As peças de dominó devem ser embaralhadas aleatoriamente antes do início do jogo.
3. Distribuição de Peças aos Jogadores: As peças embaralhadas devem ser distribuídas igualmente entre os jogadores,
mantendo a ordem das peças aleatória.
4. Jogada de Peças: Os jogadores devem ser capazes de jogar suas peças, desde que os números nas extremidades
correspondam às peças previamente jogadas.
5. Verificação de Estado do Jogo: O programa deve verificar o estado atual do jogo, incluindo as peças jogadas, as peças
disponíveis para jogar e determinar o vencedor.


## Restrições
1. O programa deve ser implementado em Python, utilizando listas encadeadas para armazenar as peças de dominó e as
mãos dos jogadores.
2. O número de jogadores pode ser definido como uma constante ou solicitado ao usuário no início do jogo.
3. Construa sua implementação do TAD Lista Encadeada ou adapte a implementação apresentada em sala de aula. Não
utilize algo pronto da linguagem ou disponível da web.

## Integrantes
* [Ian Jairo T. Gonzales](github.com/IanJairo)
* [João Gabriel S. Dantas](github.com/gabrielDantas10)
* [Haul Muller](https://github.com/HaulMuller)

## Comentários sobre a solução
* ### Aprendizado Constante

Durante o desenvolvimento do jogo de dominó, houve um aprendizado contínuo sobre como representar e manipular as peças de dominó, além de entender a lógica do jogo.

* ### Satisfação na Resolução de Problemas

O jogo de dominó apresentou desafios interessantes, como controlar as peças, verificar as jogadas válidas e determinar o vencedor. Superar esses desafios trouxe uma sensação de satisfação.

* ### Testando e Depurando
Assim como em qualquer software, o jogo de dominó exigiu testes e depuração para garantir que funcionasse corretamente. Encontrar e corrigir erros contribuiu para a qualidade do jogo.

* ### A Diversão da Programação

O objetivo do jogo de dominó é proporcionar diversão aos jogadores, e o desenvolvimento do projeto também foi uma experiência divertida.

# Relatório Técnico: Implementação de Listas Encadeadas no Jogo de Dominó

## Introdução

Este relatório técnico descreve a estrutura de listas encadeadas utilizadas na implementação do jogo de dominó em Python. O jogo de dominó é um jogo de mesa amplamente conhecido que envolve a manipulação de peças com números correspondentes em suas extremidades. Para facilitar a manipulação das peças e o funcionamento do jogo, foram utilizadas listas encadeadas.

## Estrutura das Listas Encadeadas

No contexto do jogo de dominó, foram utilizadas duas classes principais para criar as listas encadeadas:

1. **DominoPiece (Peça de Dominó)**:
   - A classe `DominoPiece` representa uma peça individual de dominó.
   - Cada peça possui dois atributos, `value1` e `value2`, que representam os valores numéricos nas extremidades da peça.
   - Além disso, a classe `DominoPiece` possui um atributo `next` que é utilizado para encadear as peças umas às outras.

2. **DominoSet (Conjunto de Peças de Dominó)**:
   - A classe `DominoSet` representa um conjunto de peças de dominó.
   - Ela contém dois atributos, `head` e `tail`, que apontam para o início e o final da lista encadeada de peças.
   - A classe `DominoSet` possui métodos para adicionar peças ao conjunto, remover peças, embaralhar as peças e permitir a iteração sobre as peças.

## Escolhas de Implementação

### 1. Utilização de Classes e Objetos:
   - Para representar as peças de dominó e os conjuntos de peças, foram utilizadas classes e objetos.
   - A classe `DominoPiece` representa uma peça individual, o que facilita a manipulação de cada peça.
   - A classe `DominoSet` representa um conjunto de peças, permitindo a organização das peças em uma lista encadeada.

### 2. Uso de Listas Encadeadas:
   - A escolha de implementar as peças de dominó como uma lista encadeada é adequada, uma vez que as peças precisam ser facilmente adicionadas e removidas durante o jogo.
   - A lista encadeada permite a manipulação eficiente das peças sem a necessidade de realocação de memória.

### 3. Métodos Específicos:
   - Foram criados métodos específicos para adicionar peças, remover peças, embaralhar as peças e verificar se uma peça pode ser jogada.
   - Isso torna o código mais legível, modular e facilita a manutenção.

### 4. Encapsulamento:
   - A implementação segue os princípios de encapsulamento, onde as classes têm métodos para interagir com seus atributos, mantendo a integridade dos dados.

## Conclusão

A implementação das listas encadeadas no jogo de dominó permite uma manipulação eficiente das peças e torna o código mais organizado e legível. As escolhas de implementação, como o uso de classes e métodos específicos, contribuem para a modularidade e facilidade de manutenção do código.

As listas encadeadas são uma escolha apropriada para representar as peças de dominó e foram implementadas de forma a atender aos requisitos funcionais do jogo, incluindo a criação, distribuição e manipulação das peças durante o jogo.

Este relatório técnico fornece uma visão geral da estrutura das listas encadeadas e das decisões de implementação tomadas no projeto do jogo de dominó em Python.