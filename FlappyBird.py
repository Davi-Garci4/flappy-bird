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
