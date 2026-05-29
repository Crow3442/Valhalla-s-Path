import random

import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    VIDAS_INICIAIS,
    VELOCIDADE_JOGADOR,
    PONTOS_POR_ITEM,
    VELOCIDADE_QUEDA_INICIAL,
    AUMENTO_VELOCIDADE,
    INTERVALO_DIFICULDADE,
    PONTUACAO_VITORIA,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def reposicionar_no_topo(elemento):
    """Reposiciona um elemento acima da tela, em uma posição horizontal aleatória."""
    elemento["rect"].x = random.randint(0, LARGURA_TELA - elemento["rect"].width)
    elemento["rect"].y = random.randint(-150, -50)


def calcular_velocidade_queda(pontos):
    """Calcula a velocidade de queda com base na pontuação atual."""
    aumento = pontos // INTERVALO_DIFICULDADE
    return VELOCIDADE_QUEDA_INICIAL + (aumento * AUMENTO_VELOCIDADE)


def executar_jogo():
    """Executa o loop principal do Valhalla's Path."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)
    item_image = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)
    obstaculo_image = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)

    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(midbottom=(LARGURA_TELA // 2, ALTURA_TELA - 20)),
    }

    item = {
        "imagem": item_image,
        "rect": item_image.get_rect(),
    }

    obstaculo = {
        "imagem": obstaculo_image,
        "rect": obstaculo_image.get_rect(),
    }

    reposicionar_no_topo(item)
    reposicionar_no_topo(obstaculo)

    pontos = 0
    vidas = VIDAS_INICIAIS
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jogador["rect"].x -= VELOCIDADE_JOGADOR
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jogador["rect"].x += VELOCIDADE_JOGADOR

        jogador["rect"].x = limitar_valor(
            jogador["rect"].x,
            0,
            LARGURA_TELA - jogador["rect"].width,
        )

        velocidade_queda = calcular_velocidade_queda(pontos)

        item["rect"].y += velocidade_queda
        obstaculo["rect"].y += velocidade_queda

        if item["rect"].top > ALTURA_TELA:
            reposicionar_no_topo(item)

        if obstaculo["rect"].top > ALTURA_TELA:
            reposicionar_no_topo(obstaculo)

        if verificar_colisao(jogador["rect"], item["rect"]):
            pontos = calcular_pontos(pontos, PONTOS_POR_ITEM)
            reposicionar_no_topo(item)

        if verificar_colisao(jogador["rect"], obstaculo["rect"]):
            vidas = tomar_dano(vidas, 1)
            reposicionar_no_topo(obstaculo)

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        if jogador_perdeu(vidas) or pontos >= PONTUACAO_VITORIA:
            rodando = False

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)
        tela.blit(item["imagem"], item["rect"])
        tela.blit(obstaculo["imagem"], obstaculo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    pygame.quit()