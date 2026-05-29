import random

from src.config import (
    LARGURA_TELA,
    VELOCIDADE_QUEDA_INICIAL,
    AUMENTO_VELOCIDADE,
    INTERVALO_DIFICULDADE,
)


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def reposicionar_no_topo(elemento):
    """Reposiciona um elemento acima da tela, em uma posição horizontal aleatória."""
    elemento["rect"].x = random.randint(0, LARGURA_TELA - elemento["rect"].width)
    elemento["rect"].y = random.randint(-150, -50)


def calcular_velocidade_queda(pontos):
    """Calcula a velocidade de queda com base na pontuação atual."""
    aumento = pontos // INTERVALO_DIFICULDADE
    return VELOCIDADE_QUEDA_INICIAL + (aumento * AUMENTO_VELOCIDADE)