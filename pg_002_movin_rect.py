import pygame
from random import *

pygame.init()

win_dim = w,h = 600, 600
win = pygame.display.set_mode(win_dim)
pygame.display.set_caption("First Game")

# pos
x = 50
y = 50
# dimension
width = 40
height = 40

# moving velocity of color block
vel = 20

#dimension
awx = 40
ahx = 40
run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=vel
        if x <= 0:
            x = w
    if keys[pygame.K_RIGHT]:
        x+=vel
        if x >= w:
            x = 0
    if keys[pygame.K_UP]:
        y-=vel
        if y <= 0:
            y = h
    if keys[pygame.K_DOWN]:
        y+=vel
        if y >= h:
            y = 0

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x,y,width, height))
    pygame.display.update()

pygame.quit()