from fileinput import filename
import pygame
from pygame.locals import *
from sys import exit
from time import sleep
pygame.mixer.init()

pygame.init() # sempre tem que iniciar o pygame
background_music = pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound('pa.wav')
lista_id = []
class Alien:
    import pygame
    def __init__(self, id):
        self.id = id
        self.xAlien = 0
        self.yAlien = 0
        self.surface = window
        self.cor= (80,0,80)
        lista_id.append(id)
        self.pygame.draw.rect(self.surface, self.cor, (self.xAlien,self.yAlien,70,30), border_radius=8)
        self.left = False

    def move(self):
        if self.xAlien >= (640-70):
            self.left = True
            self.yAlien += 35 
        elif self.xAlien <= 0:
            self.left = False
            self.yAlien += 35
        if self.left:
            self.xAlien -= 7
        else:   
            self.xAlien += 7
    

largura = 640
altura = 480

x = 0
y = 0
xPlayer = (largura/2 - 25)
yPlayer = 435
left = False

window = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('alien')
font = pygame.font.SysFont('Calibri', 20, bold=True, italic=True) #fonte do score
score = 0
shoot = False

clock = pygame.time.Clock()

while True: # todo jogo tem o looping infinito
    clock.tick(60) # frames por segundo
    window.fill((0,0,0))
    msg = f'Score: {score}'
    text = font.render(msg, True, (255,255,255))
    for event in pygame.event.get(): # for para captar cada evento novo no jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                shoot = True
        alien = Alien(id)
    if pygame.key.get_pressed()[K_LEFT]:
        xPlayer -= 8
    if pygame.key.get_pressed()[K_RIGHT]:
        xPlayer += 8
    
    if shoot:
        bullet = pygame.draw.circle(window, (0,255,0), (xPlayer+25,yPlayer-2), 3)
        shoot = False
    jogador = pygame.draw.rect(window, (255,0,0), (xPlayer,yPlayer,50,10), border_radius=2)
    pygame.draw.line(window, (80,80,80), (0,447),(640,447), 2)
    if x >= (largura-70):
        left = True
        y += 35
    elif x <= 0:
        left = False
        y += 35
    if left:
        x -= 7
    else:   
        x += 7

    # if alien.colliderect(jogador):
    #     # pygame.mixer.Sound.play(collision_sound)
    #     pygame.quit()
    #     exit()
    window.blit(text, (10,454))
    pygame.display.update() 
