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
        self.x = x              #Eixo X
        self.y = y              #Eixo Y
        self.angulo = 0          #Aqui eu estou criando o angulo do pássaro, considerando o grau de inclinação que ele está
        self.velocidade = 0      #Aqui é a velocidade em que ele se movimenta, no caso pra cima e pra baixo
        self.altura = self.y     #Aqui é a altura em que ele se encontra, considerando que a altura dele é controlada pelo usuário apartir do inicio do jogo
        self.tempo = 0           #Aqui é o tempo do grau de inclinação dele
        self.contagem_imagem = 0  #Aqui é para informar qual imagem do passaro eu estou utilizando no momento
        self.imagem = self.imagens[0]  #Aqui é a imagem padrão/inicial que aparece do pássaro

    def pular(self):
        self.velocidade = -10.5   # Essa é a velocidade do pulo do pássaro
        self.velocidade = 0       #
        self.altura = self.y

    def mover(self):
        #Calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo #Fómula do sorvetão de fisica, que mede o deslocamento

        #Restringir o deslocamento, para que o pássaro não possa subir e nem possa descer infinitamente
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2 # Aqui eu estou dando um ganho extra para o deslocamento do pássaro para cima, para que o pulo seja maior
        self.y += deslocamento   # Aqui esta o deslocamento pássaro

        #angulo do pássaro
        if deslocamento < 0 or self.y < (self.altura + 50):    #Aqui eu estou deixando o angulo do pássaro pra cima, sempre que ele esta acima do angulo inicial
            if self.angulo < self.rotacao_maxima:
                self.angulo = self.rotacao_maxima

        else:
            if self.angulo >- 90:                           #Aqui eu estou limitando o angulo de caida do passaro a -90 graus
                self.angulo -= self.velocidade_rotacao      # Aqui eu estou gerando a caida do pássaro gradativamente até o angulo de -90 graus

    def desenhar(self):
        self.contagem_imagem += 1
        if self.contagem_imagem < self.tempo_animacao:
            self.imagem = self.imagens[0]
        elif self.contagem_imagem < self.tempo_animacao*2:
            self.imagem = self.imagens[1]
        elif self.contagem_imagem < self.tempo_animacao*3:
            self.imagem = self.imagens[2]


class Cano:
    pass

class Chao:
    pass
