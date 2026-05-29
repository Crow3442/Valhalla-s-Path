import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    PRETO,
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


def desenhar_texto(tela, texto, fonte, cor, centro):
    """Desenha um texto centralizado na tela."""
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=centro)
    tela.blit(superficie, retangulo)


def exibir_tela_inicial(tela, relogio):
    """Exibe a tela inicial do jogo."""
    fonte_titulo = pygame.font.Font(None, 72)
    fonte_texto = pygame.font.Font(None, 36)

    aguardando = True

    while aguardando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return True

                if evento.key == pygame.K_ESCAPE:
                    return False

        tela.fill(CINZA)

        desenhar_texto(
            tela,
            TITULO_JOGO,
            fonte_titulo,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 - 80),
        )

        desenhar_texto(
            tela,
            "Colete itens, desvie dos obstáculos e alcance Valhalla.",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2),
        )

        desenhar_texto(
            tela,
            "Pressione ENTER para iniciar",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 + 60),
        )

        desenhar_texto(
            tela,
            "Pressione ESC para sair",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 + 110),
        )

        pygame.display.flip()

    return False


def exibir_tela_final(tela, relogio, pontos, recorde, venceu):
    """Exibe a tela final de vitória ou derrota."""
    fonte_titulo = pygame.font.Font(None, 72)
    fonte_texto = pygame.font.Font(None, 36)

    aguardando = True

    while aguardando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return True

                if evento.key == pygame.K_ESCAPE:
                    return False

        tela.fill(CINZA)

        mensagem = "Você alcançou Valhalla!" if venceu else "Fim de jornada"

        desenhar_texto(
            tela,
            mensagem,
            fonte_titulo,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 - 100),
        )

        desenhar_texto(
            tela,
            f"Pontuação: {pontos}",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 - 20),
        )

        desenhar_texto(
            tela,
            f"Recorde: {recorde}",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 + 25),
        )

        desenhar_texto(
            tela,
            "Pressione ENTER para jogar novamente",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 + 90),
        )

        desenhar_texto(
            tela,
            "Pressione ESC para sair",
            fonte_texto,
            PRETO,
            (LARGURA_TELA // 2, ALTURA_TELA // 2 + 140),
        )

        pygame.display.flip()

    return False


def executar_partida(tela, relogio):
    """Executa uma partida do Valhalla's Path."""
    fonte_hud = pygame.font.Font(None, 32)

    player_image = pegar_sprite(
        CAMINHO_SPRITES,
        x=110,
        y=120,
        width=190,
        height=190,
        scale=0.5,
    )

    item_image = pegar_sprite(
        CAMINHO_SPRITES,
        x=900,
        y=690,
        width=200,
        height=200,
        scale=0.5,
    )

    obstaculo_image = pegar_sprite(
        CAMINHO_SPRITES,
        x=905,
        y=1060,
        width=200,
        height=130,
        scale=0.5,
    )

    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(
            midbottom=(LARGURA_TELA // 2, ALTURA_TELA - 20)
        ),
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
    venceu = False
    rodando = True

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return pontos, recorde, venceu, False

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return pontos, recorde, venceu, False

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

        if pontos >= PONTUACAO_VITORIA:
            venceu = True
            rodando = False

        if jogador_perdeu(vidas):
            rodando = False

        pygame.display.set_caption(
            f"{TITULO_JOGO} | "
            f"Pontos: {pontos} | "
            f"Recorde: {recorde} | "
            f"Vidas: {vidas}"
        )

        tela.fill(CINZA)

        texto_hud = fonte_hud.render(
            f"Pontos: {pontos} | Vidas: {vidas} | Recorde: {recorde}",
            True,
            PRETO,
        )

        tela.blit(texto_hud, (20, 20))

        for item in itens:
            tela.blit(item["imagem"], item["rect"])

        for obstaculo in obstaculos:
            tela.blit(obstaculo["imagem"], obstaculo["rect"])

        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    return pontos, recorde, venceu, True


def executar_jogo():
    """Executa o fluxo completo do jogo."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    continuar = exibir_tela_inicial(tela, relogio)

    while continuar:
        pontos, recorde, venceu, continuar = executar_partida(tela, relogio)

        if continuar:
            continuar = exibir_tela_final(
                tela,
                relogio,
                pontos,
                recorde,
                venceu,
            )

    pygame.quit()