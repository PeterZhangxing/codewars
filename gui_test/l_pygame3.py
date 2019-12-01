import pygame
import math

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

def get_points():
    points_li = []
    for x in range(640):
        y = int(math.sin(x/640.0*4*math.pi)*200+240)
        points_li.append([x,y])
    return points_li

pygame.draw.lines(screen,[0,0,0],False,get_points(),2)

pygame.display.flip()

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()