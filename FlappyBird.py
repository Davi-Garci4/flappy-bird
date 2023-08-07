import pygame   #Biblioteca de jogos python
import os       #Biblioteca para integração de arquivos com os códigos
import random   #Biblioteca que gera numeros aleatórios

Tela_largura = 500   #Definindo a largura da tela
Tela_altura = 800    #Definido a altura de tela

imagem_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'pipe.png')))          #Aqui eu estou abrindo a pasta imagens e integrando as imagens a essas variáveis através das biliotecas e aumentando 2x as suas escalas.
imagem_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'base.png')))
imagem_background = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'bg.png')))
imagens_passaro = [pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'bird1.png'))),
                   pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'bird2.png'))),
                   pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'bird3.png')))]

pygame.font.init()               #Aqui eu estou inicializando a entrada do texto atravéz da pygame
fonte_pontos = pygame.font.SysFont("arial", 50)     #Aqui esta sendo informada a fonte e o tamanho dela

class Passaro:
    imagens = imagens_passaro
    #animação de rotação
    rotacao_maxima = 25
    velocidade_rotacao = 20
    tempo_animacao = 5

    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.angulo = 0          #Aqui eu estou criando o angulo do pássaro, considerando o grau de inclinação que ele está
        self.velocidade = 0      #Aqui é a velocidade em que ele se movimenta, no caso pra cima e pra baixo
        self.altura = self.y     #Aqui é a altura em que ele se encontra, considerando que a altura dele é controlada pelo usuário apartir do inicio do jogo
        self.tempo = 0           #Aqui é o tempo do grau de inclinação dele
        self.contagem_imagem = 0  #Aqui é para informar qual imagem do passaro eu estou utilizando no momento
        self.imagem = imagens[0]  #Aqui é a imagem padrão/inicial que aparece do pássaro


class Cano:
    pass

class Chao:
    pass
