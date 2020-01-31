import pygame
from random import *
pygame.init()

class Shape:
    def __init__(self, typeOfShape=None):
        self.typeOfShape = typeOfShape

    def get_shape(self):
        print(self.typeOfShape)

#1
class Circle(Shape):
    def __init__(self, radius, position, window):
        Shape.__init__(self, "Circle\n")
        self.radius = radius
        self.position = position
        self.window = window
    
    def getMeta(self):
        print("Radius: {}".format(self.radius) +
        " Position: "+str(self.position))

#2
class Rectangle(Shape):
    def __init__(self, width, height, window):
        Shape.__init__(self, "Rectangle\n")   
        self.width = width
        self.height = height
        self.window = window
    
    def getMeta(self):
        print("Width: {}".format( self.width) +
        " Height: {}".format(self.height) )

#3
class Square(Shape):
    def __init__(self, length, window):
        Shape.__init__(self, "Square\n")
        self.length = length
        self.window = window

    def getMeta(self):
        print("Length: {}".format(self.length))

def process():
    count = 25
    window_dim = window_w, window_h = 900, 700
    window = pygame.display.set_mode(window_dim)
    pygame.display.set_caption("Random")

    velocity = 4
    base_len, base_height, base_width = 15,15,15
    base_radius = 15
    
    run = True

    li = []

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        random_shape = randint(1, 3)

        random_size = randint(1,5)

        random_c_r = randint(1, 255)
        random_c_g = randint(1, 255)
        random_c_b = randint(1, 255)
        #color
        random_color = (random_c_r, random_c_g, random_c_b)
        
        random_pos_x = randint(0, window_w)
        random_pos_y = randint(0, window_h)
        #position
        random_pos = (random_pos_x*random_size, 
        random_pos_y*random_size)

        window.fill((0,0,0))
        count = count - 1

        if random_shape == 1:
            a= pygame.draw.circle(window, random_color, random_pos, base_radius*random_size)
            li.append(a)

        if random_shape == 2:
            a= pygame.draw.rect(window, random_color, (random_pos_x,
            random_pos_y, base_width*random_size, base_height*random_size))
            li.append(a)

        if random_shape == 3:
            a= pygame.draw.rect(window, random_color, (random_pos_x,
            random_pos_y, base_len*random_size, base_len*random_size))
            li.append(a)
        
        # if count == 0:
        #     break

        pygame.display.update()
    

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    process()