import pygame
from random import *
pygame.init()

window_width = 400
window_height = 400
offset = 30
window_dimension = window_width, window_height
window = pygame.display.set_mode(window_dimension)
pygame.display.set_caption("I'm Window")
run = True

sysrand = SystemRandom()
vel = 20
total = 20
off_width, off_height = window_width-offset, window_height-offset
posX = []
posY = []
dire = [1,2,3,4] #left, top, right, bottom
colors =[]
b_w, b_h = 30,30

x,y = 100,100

i = 0
while i < total:
    posX.insert(i, randint(0, off_height)) 
    posY.insert(i, randint(0, off_height)) 
    dire.insert(i, randint(1,4))
    i+=1

i = 0
while i < 10:
    r = randint(0, 250)
    g = randint(0, 250)
    b = randint(0, 250)
    color = (r,g,b)
    colors.insert(i, color)
    i = i + 1

while run:
    pygame.time.delay(1000)

    for event in pygame.event.get():
           if event.type == pygame.QUIT:
                run = False

    i = 0
    while i < 20:

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                run = False

        li = [-1,-1,-1,-1, 1,1,1,1]
        derx = sysrand.choice(li)
        dery = sysrand.choice(li)
        

        if posX[i] < offset:
            posX[i] = off_width

        if posY[i] < offset:
            posY[i] = off_height
        
        if posX[i] > off_width:
            posX[i] = offset
        
        if posY[i] > off_height:
            posY[i] = offset

        posX[i] += vel * derx
        posY[i] += vel * dery
        # window.fill((0))
        pygame.draw.rect(window, colors[i%9], (posX[i],posY[i],b_w,b_h))
        pygame.display.update()
        i = i + 1
pygame.quit()
