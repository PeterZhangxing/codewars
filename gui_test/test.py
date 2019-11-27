import easygui

# 使用按钮框,完成选择
# flavor = easygui.buttonbox(
#     msg='choose your favourate flavor',
#     choices=['strawberry','chocolate','milk','coffee']
# )

# 使用选择框,完成选择
# flavor = easygui.choicebox(
#     msg='choose your favourate flavor',
#     choices=['strawberry','chocolate','milk','coffee']
# )

# 使用文本框,获取输入的文字
# flavor = easygui.enterbox(
#     msg='please enter your favourate flavor:',
#     default='strawberry'
# )

# 只能输入整数的对话框
# flavor = easygui.integerbox(
#     msg='please enter your favourate flavor:',
#     default=3
# )
#
# easygui.msgbox('you have chosen %s'%flavor)

# import pygame
# import sys
#
# dots = [[221, 432], [225, 331], [133, 342], [141, 310],[51, 230], [74, 217], [58, 153], [114, 164],[123, 135], [176, 190], [159, 77], [193, 93],[230, 28], [267, 93], [301, 77], [284, 190],[327, 135], [336, 164], [402, 153], [386, 217],[409, 230], [319, 310], [327, 342], [233, 331],[237, 432]]
#
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
# screen.set_at([100,100],[0,0,0]) # 设置单个像素点的位置和颜色
# feature = screen.get_at([100, 100])
# print(feature)
#
# pygame.draw.lines(screen,[255,0,0],True,dots,3)
#
# pygame.display.flip()
#
# flag = True
# while flag:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             flag = False
#
# pygame.quit()

import pygame

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

my_bomb = pygame.image.load("images/bomb.png")
axis_x = 0
axis_y = 0

# screen.blit(my_bomb,[axis_x,axis_y])
# pygame.display.flip()

# pygame.time.delay(2000)
# screen.blit(my_bomb,[163,100])
# pygame.draw.rect(screen,[255,255,255],[100,100,63,57],0)
# pygame.display.flip()

# speed = 5
# for i in range(1,1200):
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [axis_x, axis_y, 63, 57], 0)
#     # screen.fill([255, 255, 255])
#     axis_x += speed
#     if axis_x >= 577:
#         axis_x = 0
#     screen.blit(my_bomb, [axis_x, axis_y])
#     pygame.display.flip()

x_speed = 5
y_speed = 5
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [axis_x, axis_y, 63, 57], 0)
    # screen.fill([255, 255, 255])

    axis_x += x_speed
    axis_y += y_speed
    # if axis_x >= screen.get_width() - 63 or axis_x <= 0:
    #     x_speed = -x_speed
    # if axis_y >= screen.get_height() - 57 or axis_y <= 0:
    #     y_speed = -y_speed

    if axis_x >= screen.get_width():
        axis_x = -63
    if axis_y >= screen.get_height():
        axis_y = -57

    screen.blit(my_bomb, [axis_x, axis_y])
    pygame.display.flip()

pygame.quit()