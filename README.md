# Valhalla's Path

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

**Valhalla's Path** é um jogo de desvio de obstáculos e coleta de itens inspirado na mitologia nórdica. O jogador assume o papel de um guerreiro viking que morreu em batalha e precisa atravessar os Nove Reinos para provar seu valor aos deuses e alcançar Valhalla.

Durante sua jornada, o jogador deverá coletar artefatos sagrados e evitar perigos que surgem constantemente pelo caminho.

---

## Integrantes do grupo

* João Eduardo Soares Moreira

---

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicação.
* `src/`: código-fonte principal do jogo (loop, regras, entidades e dados).
* `assets/`: imagens, fontes e sons.
* `data/`: arquivos persistentes (recorde/ranking).
* `tests/`: testes unitários com `pytest`.
* `docs/`: documentação do projeto, incluindo proposta inicial.

---

## Descrição do jogo

Valhalla's Path é um jogo de sobrevivência e coleta de itens em que o jogador controla um guerreiro viking em sua jornada rumo a Valhalla.

Durante a partida, diversos obstáculos caem do topo da tela e devem ser evitados. Ao mesmo tempo, itens sagrados aparecem para serem coletados, aumentando a pontuação do jogador.

A dificuldade aumenta progressivamente ao longo do tempo, tornando a travessia cada vez mais desafiadora.

---

## Objetivo do jogador

O objetivo do jogador é sobreviver pelo maior tempo possível, coletar artefatos sagrados e acumular pontos suficientes para provar seu valor aos deuses.

Além disso, o jogador poderá competir pelo melhor recorde registrado no jogo.

---

## Regras do jogo

* O jogador controla um guerreiro viking.
* O personagem pode se mover para a esquerda e para a direita.
* Obstáculos surgem continuamente na tela.
* Colidir com obstáculos reduz a quantidade de vidas.
* Itens coletáveis aumentam a pontuação.
* A velocidade dos elementos aumenta com o tempo.
* O jogo termina quando o jogador perde todas as vidas.
* O recorde é salvo em arquivo para futuras partidas.

---

## Elementos do jogo

### Obstáculos

* Machados
* Rochas
* Raios de Thor
* Troncos

### Itens coletáveis

* Runas Sagradas
* Moedas Vikings
* Fragmentos de Yggdrasil

---

## Controles

* ← ou A: mover para a esquerda
* → ou D: mover para a direita
* ENTER: iniciar ou reiniciar a partida
* ESC: sair do jogo

---

## Tecnologias utilizadas

* Python 3
* Pygame
* Pytest
* Git
* GitHub

---

## Conceitos da disciplina aplicados

O projeto utiliza diversos conceitos estudados ao longo da disciplina:

* Variáveis
* Entrada e saída de dados
* Estruturas condicionais
* Laços de repetição
* Listas
* Dicionários
* Funções
* Modularização
* Leitura e escrita de arquivos
* Testes automatizados

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o jogo

```bash
python main.py
```

---

## Como executar os testes

```bash
python -m pytest
```

---

## Estrutura prevista de arquivos

```text
.
├── assets/
├── data/
├── docs/
├── src/
│   ├── config.py
│   ├── dados.py
│   ├── funcoes.py
│   └── jogo.py
├── tests/
├── main.py
├── README.md
└── requirements.txt
```

---

## Checklist mínimo para entrega

* [x] Definição da proposta do jogo
* [x] Preenchimento da documentação inicial
* [ ] Protótipo funcional em Pygame
* [ ] Sistema de pontuação
* [ ] Sistema de vidas
* [ ] Sistema de dificuldade progressiva
* [ ] Salvamento de recorde
* [ ] Testes implementados
* [ ] README atualizado
* [ ] Entrega final concluída

---

## Referências

Caso sejam utilizados recursos externos (imagens, sons, fontes ou tutoriais), suas referências e licenças serão documentadas nesta seção durante o desenvolvimento do projeto.

---

## Licença

Projeto acadêmico desenvolvido para fins educacionais na disciplina de Introdução a Algoritmos/Programação da PUC Minas.