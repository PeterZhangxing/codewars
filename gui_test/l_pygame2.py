import pygame
from pygame.color import THECOLORS
import random

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

for i in range(100):
    axis_x = random.randint(0,500)
    axis_y = random.randint(0,400)
    width = random.randint(0,250)
    height = random.randint(0,100)

    line_width = random.randint(1,3)

    color_key = random.choice(list(THECOLORS.keys()))
    rand_color = THECOLORS[color_key]

    myrect = pygame.Rect(axis_x,axis_y,width,height)
    pygame.draw.rect(screen,rand_color,myrect,line_width)

pygame.display.flip()

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()