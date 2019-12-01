import pygame

from lnpygame.mysprites import BackgroundSprite
from lnpygame.mysprites import EnemySprite
from lnpygame.mysprites import HeroSprite

from lnpygame.mysprites import SCREEN_RECT,FRAME_PER_SEC
from lnpygame.mysprites import CREATE_ENEMY_EVENT,HERO_FIRE_EVENT


class PlaneGame(object):

    def __init__(self):
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()

        # 3. 调用私有方法，完成游戏中所有精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件,每隔设置的事件间隔触发一次自定义的事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        bg1 = BackgroundSprite()
        bg2 = BackgroundSprite(True)
        self.back_ground_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = HeroSprite()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新/绘制精灵组
            self.__update_sprites()

            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方法获取键盘按键
        pressed_keys = pygame.key.get_pressed()
        # print(pressed_keys)

        if pressed_keys[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif pressed_keys[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1. 子弹摧毁敌机,碰撞发生，子弹消失，敌机也消失
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # 2. 敌机撞毁英雄,碰撞发生，敌机消失
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        # 如果有敌机消失了，说明英雄被撞了，也该消失
        if enemies:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_ground_group.update()
        self.back_ground_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit('game over!')


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()