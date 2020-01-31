import pygame
from random import *

pygame.init()

win_dim = w,h = 600, 600
win = pygame.display.set_mode(win_dim)
pygame.display.set_caption("First Game")

# Block configuation
# pos
x = 50
y = 550
# dimension
width = 40
height = 40
# moving velocity of color block
vel = 5

run = True

isJump = False
jumpCount = 10

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
  
    if not (isJump):
        if keys[pygame.K_UP]:
                y-=vel
                if y <= 0:
                    y = h
        if keys[pygame.K_DOWN]:
                y+=vel
                if y >= h:
                    y = 0 
        if keys[pygame.K_SPACE]:
           isJump = True
    else:
        neg = 1
        if jumpCount >= -10:
            if jumpCount > 0: # go down else go up with help of neg value
                neg = -1

            y += (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

        print('jumpCount: ', jumpCount, ' neg: ', neg )
     

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width, height))
    pygame.display.update()

pygame.quit()