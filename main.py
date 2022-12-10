import pygame
from pygame.locals import *
import time

pygame.init()
w = 960
h = 720
screen = pygame.display.set_mode((w, h))


bg = pygame.image.load('bg.png')

px = 100
py = 100

pygame.display.flip()

def fpstool(i):
    i=0
    while





class P():
    def __init__(self):
        self.image = pygame.image.load('airplane.png')
        self.rect=self.image.get_rect()
        self.rect.centerx=w/2
        self.rect.bottom=h-20
    def update(self):
        self.sx=0
        self.sy=0
        keys = pygame.key.get_pressed()
        #print(keys)
        if keys[pygame.K_d]:
            self.sx=8
        if keys[pygame.K_a]:
            self.sx = -8
        if keys[pygame.K_d]:
            self.sx = 8
        if keys[pygame.K_a]:
            self.sx = -8
        self.rect.centerx += self.sx
        if keys[pygame.K_w]:
            self.sy = -8
        if keys[pygame.K_s]:
            self.sy = 8
        self.rect.centery+=self.sy

Clock=pygame.time.Clock()
fps=480

p = P()
running = True
while running:
    Clock.tick(fps)
    
    
    p.update()
    screen.blit(bg,(-9,-9))
    screen.blit(p.image,p.rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()





