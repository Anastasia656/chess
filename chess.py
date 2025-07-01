import pygame
import random
import math
# Initialize the pygame
pygame.init()
W = 400
H = 400
size = 50
targetx = random.randint(0,7) 
targety = random.randint(0,7)

# Create the screen
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pechatnik = pygame.font.Font(None,size*2)
target_img = pechatnik.render(str(targetx) + str(targety),True,(0,0,250))
target_hitbox = target_img.get_rect(center = (W//2,H//2)) 
class Square:
    def __init__(self, x, y,color): 
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(x*size, y*size, size-1, size-1)
        self.color = color
        self.start_color = color

    def draw(self):
        pygame.draw.rect(screen, self.color,self.hitbox)
    def check_click(self, x, y):
        if self.hitbox.collidepoint(x, y):
            if (targetx,targety) == (self.x,self.y):
                self.color = (0,255,0)
                generate()
            else:
                self.color = (255,0,0)

square_list = []
for y in range(8): #кол-во столбцов и строк(0-7)
    for x in range(8):
        if x%2 == 0 and y%2 == 0 or x%2 == 1 and y%2 == 1:
            color = (255,255,255)
        else:
            color = (0,0,0)
        square = Square(x,y,color)
        square_list.append(square)
   
def generate():
    global targetx,targety,target_img,target_hitbox
    targetx = random.randint(0,7) 
    targety = random.randint(0,7)
    target_img = pechatnik.render(str(targetx) + str(targety),True,(0,0,250))
    target_hitbox = target_img.get_rect(center = (W//2,H//2)) 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.set_timer(pygame.USEREVENT,500)
            x, y = event.pos
            for square in square_list:
                square.check_click(x, y)
        elif event.type == pygame.USEREVENT:
            for square in square_list:
                square.color = square.start_color
    for square in square_list:
        square.draw()
    screen.blit(target_img,target_hitbox)
    pygame.display.update()
    clock.tick(1)

