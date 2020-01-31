import pygame
from random import *

class Enemy(object):
    #images (total 11 images)
    def __init__(self, x, y, start, end):
        self.x = x
        self.y = y
        self.start = start
        self.width = 64
        self.height = 64
        self.end = end
        self.vel = 3
        self.path = [self.start, self.end]
        self.walkCount = 0
        self.walkRight = []
        self.walkLeft = []
        self.imgFormat = ['.png', '.jpg', '.jpeg']
        self.imgName = ['L', 'R', 'E']
        self.hitBox = (self.x+20, self.y, 30, 60)
        self.visible = True
        self.health = 10
        self.healthCount = 10
        self.failing = 15
        self.failingWindow = 15
        self.score = 0
        
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
        if self.visible:
            if self.walkCount + 1 == 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3],(self.x, self.y))
                self.walkCount += 1
            else :
                win.blit(self.walkLeft[self.walkCount // 3],(self.x, self.y))
                self.walkCount += 1
            
            self.hitBox = (self.x+20 , self.y, 30, 60)
            
            pygame.draw.rect(win, (255,0,0), (self.hitBox[0], self.hitBox[1] - 5,  15, 5))
            pygame.draw.rect(win, (0,125,0), (self.hitBox[0], self.hitBox[1] - 5,  self.failing, 5))
        
        pygame.draw.rect(win, (255,0,0), self.hitBox, 2)
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
    
    def hit(self):
        self.failing = self.failing - (self.failingWindow/self.healthCount)
        if self.health > 0:
            self.score += 1
            self.health -= 1
        else :
            self.visible = False
        print('hit', self.score)

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
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitBox = (self.x + 10, self.y, 30, 60)
        self.injury = False

    def draw(self, win):
        if self.injury:
            self.injury = False
            print (' new x: ', self.x, ' new y: ', self.y)
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
        
        self.hitBox = (self.x + 10, self.y, 30, 60)
        pygame.draw.rect(win, (255,0,0), self.hitBox, 2)

    def hit(self, goblin):
        self.isJump = False
        self.jumpCount = 10
        print ('Injury ', self.x, ' ', self.y)
        self.injury = True

        midway = (goblin.start + goblin.end)*0.5
        if goblin.vel < 0:
            if goblin.x < midway:
                self.x = 750
                self.y = 400
            if goblin.x > midway:
                self.x = 20
                self.y = 400
        elif goblin.vel > 0:
            if goblin.x < midway:
                self.x = 750
                self.y = 400
            if goblin.x > midway:
               self.x = 20
               self.y = 400
        
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100, True)
        text = font.render('-5', 1, (255,0,0))
        win.blit(text, (400 - text.get_width(), 300))
        pygame.display.update()

        i = 1
        while i<300:
            pygame.time.delay(10)
            i += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

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
    text = font.render('Score: ' + str(goblin.score), 1, (0,0,0))
    win.blit(text, ( 500, 10))
    player.draw(win)
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
player = Player(40, 400)
bullets = []
goblin = Enemy(500, 400, 20, 750)
coolDown = 0
font = pygame.font.SysFont('comicsans', 30, True)

boundryPlayer = (player.hitBox[2]*0.5, player.hitBox[3]*0.5)
boundryGoblin   = (goblin.hitBox[2]*0.5, goblin.hitBox[3]*0.5)
boundry = (boundryPlayer[0] + boundryGoblin[0], boundryPlayer[1] + boundryGoblin[1])

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    # bullet lag
    if coolDown < 3:
        coolDown += 1
    else:
        coolDown = 0

    pc = ((player.x + player.hitBox[2] *0.5), (player.y + player.hitBox[3] *0.5))
    gc = ((goblin.x + goblin.hitBox[2] *0.5), (goblin.y + goblin.hitBox[3] *0.5))
    diffX = abs(pc[0] - gc[0])
    diffY = abs(pc[1] - gc[1])

    if diffX <= boundry[0] and diffY <= boundry[1]:
        player.hit(goblin)

    for bullet in bullets:
        if bullet.y + bullet.radius < goblin.hitBox[1] + goblin.hitBox[3] and bullet.y - bullet.radius > goblin.hitBox[1]:
            if bullet.x + bullet.radius < goblin.hitBox[0] + goblin.hitBox[2] and bullet.x > goblin.hitBox[0]:
                goblin.hit();
                bullets.pop(bullets.index(bullet))
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE] and coolDown == 0:
        facing = 1
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) <= 5:
            bullets.append(Projectile( round(player.x + player.width * 0.5), round(player.y + player.height * 0.5),  6, (0,0,0), facing))
        coolDown += 1

    if keys[pygame.K_LEFT]:
        if player.x + player.vel > 10:
            player.x-= player.vel
            player.left = True
            player.right = False
            player.standing = False

    elif keys[pygame.K_RIGHT]:
        if player.x + player.vel < w:
            player.x += player.vel
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

    if player.isJump :
        print(' Jump x: ', player.x, ' Jump y: ', player.y)
    # if player.left or player.right :print('Man x: ', player.x, ' Man y: ', player.y, ' Enemy x: ', goblin.x, ' Enemy y: ', goblin.y, ' vel : ',goblin.vel)
    drawGame()
pygame.quit()