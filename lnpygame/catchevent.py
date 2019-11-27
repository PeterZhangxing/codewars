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

# 绘制图像
hero_rect = pygame.Rect(150, 300, 102, 126)
screen.blit(hero, hero_rect)

# 更新绘制完的图片到游戏窗口
pygame.display.update()

# 设置时钟对象
clock = pygame.time.Clock()

while True:

    # 设置每秒循环60次
    clock.tick(60)

    # 获取游戏中所有的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # print("exit the game!")
            exit("exit the game!")

    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    # 重新绘制所有的内容，包括背景和飞机
    screen.blit(bg,(0,0))
    screen.blit(hero, hero_rect)

    # 显示更新后的图片
    pygame.display.update()