import pygame


class MyBall(pygame.sprite.Sprite):

    def __init__(self,image_file,speed,location,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top,self.rect.left = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_rect().right:
            self.speed[0] = -self.speed[0]

pygame.init()

delay = 50
interval = 20
<<<<<<< HEAD
# pygame.key.set_repeat(delay,interval)
=======
pygame.key.set_repeat(delay,interval)
>>>>>>> 14f312767054a48ba69a7e2d045cb83348118d2b

size = (640,480)
screen = pygame.display.set_mode(size)
print(screen.get_size())
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])

clock = pygame.time.Clock()
# 自定义时钟事件
pygame.time.set_timer(pygame.USEREVENT,1000)

imgf = "images/beach_ball.png"
speed = [10,0]
location = [20,20]
myball = MyBall(imgf,speed,location,screen)

direction = 1
mouse_hold = False
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.USEREVENT:
            # print(myball.rect.centery) # 中间点的y坐标
            myball.rect.centery = myball.rect.centery + (30 * direction)
            if myball.rect.top <= 0 or myball.rect.bottom >= screen.get_rect().bottom:
                direction = -direction

    screen.blit(background,[0,0])

    myball.move()
    screen.blit(myball.image,myball.rect)
    clock.tick(30)

    pygame.display.flip()

pygame.quit()