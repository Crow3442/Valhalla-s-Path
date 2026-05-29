# Proposta Inicial do Jogo

Este documento apresenta a proposta inicial do jogo desenvolvido pelo grupo para o projeto final da disciplina, utilizando Python e a biblioteca Pygame.

## 1. Nome provisório do jogo

**Valhalla's Path**
**O Caminho para Valhalla**

## 2. Integrantes do grupo

* Nome 1: João Eduardo Soares Moreira

## 3. Tipo de jogo

Tipo escolhido pelo grupo: Jogo de desviar de obstáculos com coleta de itens.

## 4. Descrição geral do jogo

**Valhalla's Path** é um jogo simples desenvolvido em Python com Pygame, no qual o jogador controla um guerreiro viking que morreu em batalha e precisa atravessar um caminho perigoso entre os Nove Reinos para provar seu valor aos deuses e alcançar Valhalla.

Durante a partida, o personagem se movimenta horizontalmente pela parte inferior da tela, desviando de obstáculos que caem do topo, como machados, rochas, troncos e raios de Thor. Ao mesmo tempo, o jogador deve coletar itens sagrados, como runas, moedas vikings e fragmentos de Yggdrasil, para aumentar sua pontuação.

A dificuldade aumenta com o passar do tempo, tornando os obstáculos mais rápidos e a partida mais desafiadora.

## 5. Objetivo do jogador

O objetivo principal do jogador é sobreviver pelo maior tempo possível, coletar itens sagrados e alcançar a maior pontuação antes de perder todas as vidas.

Além disso, o jogador busca provar seu valor aos deuses, acumulando pontos suficientes para entrar em Valhalla.

## 6. Regras principais

* O jogador começa a partida com uma quantidade inicial de vidas.
* O personagem pode se mover para a esquerda e para a direita.
* Obstáculos caem do topo da tela em posições aleatórias.
* O jogador deve desviar dos obstáculos para não perder vidas.
* Itens coletáveis também aparecem na tela e aumentam a pontuação.
* Cada colisão com um obstáculo remove uma vida do jogador.
* A partida termina quando o jogador perde todas as vidas.
* A dificuldade aumenta gradualmente com o tempo.
* O recorde ou ranking será salvo em arquivo.
* A pontuação final representa o desempenho do jogador na jornada até Valhalla.

## 7. Condição de vitória

A condição principal de vitória será atingir uma pontuação mínima definida, representando que o guerreiro provou seu valor e conseguiu alcançar Valhalla.

Inicialmente, a pontuação de vitória prevista será de **300 pontos**.

Modo de sobrevivência: a vitória poderá ser interpretada como alcançar a maior pontuação possível e registrar um novo recorde.

## 8. Condição de derrota ou encerramento

A partida será encerrada quando o jogador perder todas as vidas.

O jogador perde vidas ao colidir com obstáculos, como machados, rochas, troncos ou raios. Quando a quantidade de vidas chegar a zero, o jogo termina e a pontuação final é exibida.

Caso a pontuação final seja maior que o recorde salvo anteriormente, o novo recorde será registrado em arquivo.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

O jogador controlará um guerreiro viking posicionado na parte inferior da tela. Esse personagem poderá se mover horizontalmente para a esquerda e para a direita, desviando dos perigos e coletando itens sagrados.

## Obstáculos, inimigos ou desafios

Os obstáculos cairão do topo da tela em posições aleatórias. Os principais obstáculos previstos são:

* machados;
* rochas;
* raios de Thor;
* troncos.

Esses elementos representarão os perigos encontrados pelo guerreiro durante sua travessia pelos Nove Reinos. Caso o jogador colida com um obstáculo, perderá uma vida.

## Itens, alvos ou objetos de interação

Os itens coletáveis também cairão do topo da tela e deverão ser coletados pelo jogador para aumentar sua pontuação. Os principais itens previstos são:

* runas sagradas;
* moedas vikings;
* fragmentos de Yggdrasil.

Cada item poderá ter uma pontuação diferente, permitindo o uso de dicionários para armazenar seus valores.

## Pontuação, vidas, tempo ou progresso

O jogador começará com uma quantidade inicial de vidas, como 3 vidas. A pontuação aumentará sempre que o jogador coletar um item.

A dificuldade será progressiva, aumentando a velocidade dos obstáculos conforme o tempo de jogo ou a pontuação do jogador aumenta.

Também será utilizado um sistema de recorde ou ranking salvo em arquivo, permitindo registrar o melhor desempenho obtido.

## 10. Controles previstos

Controles do grupo:

* Seta para esquerda ou tecla A: mover o personagem para a esquerda.
* Seta para direita ou tecla D: mover o personagem para a direita.
* ESC: sair do jogo.
* Espaço ou Enter: iniciar ou reiniciar a partida.

## 11. Organização inicial do código

A organização planejada seguirá a estrutura inicial do template da disciplina, mantendo os arquivos principais e adaptando o código para a proposta do jogo.

Organização planejada:

* `main.py`: responsável por iniciar o jogo.
* `src/jogo.py`: conterá o loop principal do jogo, a atualização dos elementos, as colisões e a renderização da tela.
* `src/config.py`: guardará configurações gerais, como tamanho da tela, cores, velocidade inicial, quantidade de vidas e pontuação de vitória.
* `src/funcoes.py`: conterá funções auxiliares e funções de lógica que poderão ser testadas.
* `src/dados.py`: conterá funções para leitura e escrita de arquivos, como salvar e carregar o recorde.
* `tests/test_logica.py`: conterá testes simples para funções de lógica do jogo.
* `docs/proposta.MD`: armazenará a proposta inicial do projeto.

## 12. Recursos externos previstos

Recursos previstos: O grupo utilizará imagens, sons ou fontes gratuitas para representar o guerreiro viking, obstáculos, itens coletáveis e efeitos sonoros simples. Caso sejam utilizados recursos externos, suas origens e licenças serão informadas no arquivo README.md.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

* Implementar corretamente a colisão entre o jogador, os obstáculos e os itens coletáveis.
* Organizar o surgimento aleatório dos obstáculos e itens na tela.
* Criar o aumento progressivo da dificuldade sem deixar o jogo impossível.
* Implementar o sistema de pontuação, vidas e encerramento da partida.
* Salvar e carregar o recorde ou ranking usando arquivos.
* Manter o código organizado em funções e módulos.
* Criar testes simples para funções de lógica sem depender diretamente da execução gráfica do Pygame.

## 14. Escopo mínimo para a entrega final

Escopo mínimo: A versão mínima do jogo terá uma janela funcional em Pygame, um personagem controlado pelo teclado, obstáculos caindo do topo da tela, itens coletáveis, sistema de pontuação, sistema de vidas, aumento simples de dificuldade, condição de fim de jogo e salvamento de recorde em arquivo.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

* Tela inicial com o nome do jogo.
* Tela de fim de jogo com pontuação final e recorde.
* Sons para coleta de itens, colisão e fim de jogo.
* Imagens para o guerreiro, obstáculos e itens.
* Diferentes tipos de obstáculos com velocidades ou danos diferentes.
* Diferentes tipos de itens com pontuações variadas.
* Ranking com mais de uma pontuação salva.
* Sistema de fases ou representação dos Nove Reinos.
* Animações simples.
* Menu de pausa.
* Efeitos visuais simples ao coletar itens ou sofrer dano.
