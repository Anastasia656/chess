import pygame
import random
import math

# Initialize the pygame
pygame.init()
W = 400
H = 400
size = 50

# Create the screen
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

class Square:
    def __init__(self, x, y,color): 
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(x*size, y*size, size-1, size-1)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color,self.hitbox)
    def check_click(self, x, y):
        if self.hitbox.collidepoint(x, y):
            self.color = (0,255,0)

square_list = []
for y in range(8): #кол-во столбцов и строк(0-7)
    for x in range(8):
        if x%2 == 0 and y%2 == 0 or x%2 == 1 and y%2 == 1:
            color = (255,255,255)
        else:
            color = (0,0,0)
        square = Square(x,y,color)
        square_list.append(square)
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for square in square_list:
                square.check_click(x, y)

    for square in square_list:
        square.draw()
    pygame.display.update()
    clock.tick(60)

