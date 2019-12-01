import pygame

pygame.init()
screen = pygame.display.set_mode([640,480])

screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0],[305,225],30,0)

# 4 条边： top、 left、 bottom、 right
# four corners: topleft, bottomleft, topright, bottomright
# 每条边的中点： midtop、 midleft、 midbottom、 midright
# 中心： center、 centerx、 centery
# 尺寸： size、 width、 height
myrect = pygame.Rect(100,100,100,150)
# pygame.draw.rect(screen,[0,0,0],myrect,0)
pygame.draw.rect(screen,[0,0,0],myrect,5)

pygame.display.flip()

tag = True
while tag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tag = False
pygame.quit()