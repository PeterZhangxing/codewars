import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 从磁盘读取图片文件到内存
bg = pygame.image.load("./images/background.png")
# blit 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
# blit 绘制图像
screen.blit(hero, (180, 350))

# 更新绘制完的图片到游戏窗口
pygame.display.update()

while True:
    pass

pygame.quit()