import pygame
from random import *

pygame.init()
clock = pygame.time.Clock()
win_dim = w,h = 852, 480
win = pygame.display.set_mode(win_dim)
pygame.display.set_caption("First Game")

#images
walkRight = []
walkLeft = []
imgFormat = ['.png', '.jpg', '.jpeg']
imgName = ['L', 'R']

for i in range(0,9):
    print(i)
    leftImage = imgName[0]+str(i+1)+imgFormat[0]
    rightImage = imgName[1]+str(i+1)+imgFormat[0]
    walkRight.insert(i, pygame.image.load('Game/'+str(rightImage)))
    walkLeft.insert(i, pygame.image.load('Game/'+str(leftImage)))

print('size left: ', len(walkLeft))
print('size right: ', len(walkRight))
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

# Block configuation

# pos
x = 50
y = 400

# dimension
width = 40
height = 40

# moving velocity of color block
vel = 5
run = True
isJump = False
jumpCount = 10
walkCount = 0
left = False
right = False

def reDraw():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 == 27:
        walkCount = 0
    
    if left:
        win.blit(walkLeft[walkCount // 3], (x,y))
        walkCount += 1
    elif right: 
        win.blit(walkRight[walkCount // 3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=vel
        if x <= 0:
            x = w
        left = True
        right = False

    elif keys[pygame.K_RIGHT]:
        x+=vel
        if x >= w:
            x = 0
        left = False
        right = True

    else :
        walkCount = 0
        left = False
        right = False
  
    if not (isJump):
        if keys[pygame.K_SPACE]:
           isJump = True
           walkCount = 0
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


    if left or right :print('jumpCount: ', jumpCount, 'height: ', y, ' left: ',left, ' right: ', right, 'walkCount: ', walkCount, 'index: ', walkCount//3 )

    reDraw()

pygame.quit()