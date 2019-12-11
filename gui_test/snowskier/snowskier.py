import pygame


skier_images = [
    "skier_down.png",
    "skier_right1.png",
    "skier_right2.png",
    "skier_left2.png",
    "skier_left1.png"
]

class MySkier(pygame.sprite.Sprite):

    def __init__(self):
        super(MySkier,self).__init__()
        self.img = pygame.image.load("skier_down.png")
        self.rect = self.img.get_rect()
        self.rect.center = [320,100]
        self.angle = 0

    def turn(self,direction):
        center = self.rect.center

        self.angle += direction
        if self.angle > 2:
            self.angle = 2
        elif self.angle < -2:
            self.angle = -2
        self.img = pygame.image.load(skier_images[self.angle])
        self.rect = self.img.get_rect()

        self.rect.center = center
        speed = [self.angle*4,6-abs(self.angle)*2]
        return speed

    def move(self,speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx > 620:
            self.rect.centerx = 620
        elif self.rect.centerx < 20:
            self.rect.centerx = 20

def animate(speed):
    screen.fill([255,255,255])
    skier.move(speed)
    screen.blit(skier.img, skier.rect)
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()

skier = MySkier()
speed = [0,6]

flag = True
while flag:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            if event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    animate(speed)

pygame.quit()