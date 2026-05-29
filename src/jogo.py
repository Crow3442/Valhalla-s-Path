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
    PONTUACAO_VITORIA,
    QUANTIDADE_ITENS,
    QUANTIDADE_OBSTACULOS,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    reposicionar_no_topo,
    calcular_velocidade_queda,
)

from src.sprites import pegar_sprite

from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


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

    itens = []
    obstaculos = []

    for _ in range(QUANTIDADE_ITENS):
        item = {
            "imagem": item_image,
            "rect": item_image.get_rect(),
        }
        reposicionar_no_topo(item)
        itens.append(item)

    for _ in range(QUANTIDADE_OBSTACULOS):
        obstaculo = {
            "imagem": obstaculo_image,
            "rect": obstaculo_image.get_rect(),
        }
        reposicionar_no_topo(obstaculo)
        obstaculos.append(obstaculo)

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

        for item in itens:
            item["rect"].y += velocidade_queda

            if item["rect"].top > ALTURA_TELA:
                reposicionar_no_topo(item)

            if verificar_colisao(jogador["rect"], item["rect"]):
                pontos = calcular_pontos(pontos, PONTOS_POR_ITEM)
                reposicionar_no_topo(item)

        for obstaculo in obstaculos:
            obstaculo["rect"].y += velocidade_queda

            if obstaculo["rect"].top > ALTURA_TELA:
                reposicionar_no_topo(obstaculo)

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

        for item in itens:
            tela.blit(item["imagem"], item["rect"])

        for obstaculo in obstaculos:
            tela.blit(obstaculo["imagem"], obstaculo["rect"])

        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    pygame.quit()