import pygame
from random import *

class Enemy(object):
    #images (total 11 images)
    
    
    def __init__(self, x, y, end):
        self.x = x
        self.y = y
        self.width = 2
        self.height = 2
        self.end = end
        self.vel = 3
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.walkRight = []
        self.walkLeft = []
        self.imgFormat = ['.png', '.jpg', '.jpeg']
        self.imgName = ['L', 'R', 'E']
        
        for i in range(0,11):
            print(i)
            leftImage = self.imgName[0]+str(i+1)+self.imgName[2]+self.imgFormat[0]
            rightImage = self.imgName[1]+str(i+1)+self.imgName[2]+self.imgFormat[0]
            self.walkRight.insert(i, pygame.image.load('Game/'+str(rightImage)))
            self.walkLeft.insert(i, pygame.image.load('Game/'+str(leftImage)))
            # print('\n Image Name: '+ leftImage + ' '+ rightImage + '\n')
        
        # print('Enemy Image Count : '+ str(len(self.walkRight)))

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3],(self.x, self.y))
            self.walkCount += 1
        else :
            win.blit(self.walkLeft[self.walkCount // 3],(self.x, self.y))
            self.walkCount += 1
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel <= self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x + self.vel >= self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

class Player(object):
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

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.width = 2
        self.height = 2
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def reDraw(self, win):
        if self.walkCount + 1 == 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right: 
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(self.walkLeft[0], (self.x, self.y))
            elif self.right:
                win.blit(self.walkRight[0], (self.x, self.y))

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 4 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawGame():
    win.blit(bg, (0,0))
    player.reDraw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

pygame.init()
clock = pygame.time.Clock()
win_dim = w,h = 800, 480
win = pygame.display.set_mode(win_dim)
pygame.display.set_caption("First Game")

bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')
player = Player(0, 400)
bullets = []
goblin = Enemy(20, 400, 750)


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE]:
        facing = 1
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) <= 5:
            bullets.append(Projectile( round(player.x + player.width//2), round(player.y + player.height//2),  6, (0,0,0), facing))
        
    if keys[pygame.K_LEFT]:
        player.x-= player.vel
        if player.x < 0:
            player.x = w
        player.left = True
        player.right = False
        player.standing = False

    elif keys[pygame.K_RIGHT]:
        player.x += player.vel
        if player.x > w:
            player.x = 0
        player.left = False
        player.right = True
        player.standing = False

    else :
        player.walkCount = 0
        player.standing = True
        
    if not (player.isJump):
        if keys[pygame.K_UP]:
           player.isJump = True
           player.walkCount = 0
    else:
        neg = 1
        if player.jumpCount >= -10:
            if player.jumpCount > 0: # go down else go up with help of neg value
                neg = -1

            player.y += (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    if player.left or player.right :print('Man x: ', player.x, ' Man y: ', player.y, ' Enemy x: ', goblin.x, ' Enemy y: ', goblin.y, ' vel : ',goblin.vel)
    drawGame()
pygame.quit()