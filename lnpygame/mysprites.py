import random
import pygame


SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    '''
    所有游戏精灵的基类
    '''

    def __init__(self,image_path,speed=1):
        super(GameSprite,self).__init__()

        # 将游戏角色图片加载到内存
        self.image = pygame.image.load(image_path)
        # 从角色图片获取矩形对象
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        '''
        游戏精灵在游戏循环中更新状态，就会自动调用该方法
        :param args:
        :return:
        '''
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    '''
    游戏背景精灵
    '''

    def __init__(self,is_alt=False):
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class EnemySprite(GameSprite):
    '''
    敌人飞机精灵
    '''

    def __init__(self):
        super().__init__("images/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self, *args):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)


class HeroSprite(GameSprite):
    '''
    英雄飞机精灵
    '''

    def __init__(self):
        super().__init__("images/me1.png",0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0,1,2):
            bullet = BulletSprite()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)


class BulletSprite(GameSprite):
    '''
    子弹精灵
    '''

    def __init__(self):
        super().__init__("images/bullet1.png", -2)

    def update(self, *args):
        super().update()

        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")