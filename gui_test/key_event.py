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
pygame.key.set_repeat(delay,interval)

size = (640,480)
screen = pygame.display.set_mode(size)
print(screen.get_size())
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()

imgf = "images/beach_ball.png"
speed = [10,0]
location = [20,20]
myball = MyBall(imgf,speed,location,screen)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                myball.rect.top += 10
                if myball.rect.top >= screen.get_size()[1]:
                    myball.rect.bottom = 0
            if event.key == pygame.K_UP:
                myball.rect.top -= 10
                if myball.rect.bottom <= 0:
                    myball.rect.top = screen.get_size()[1]

    screen.blit(background,[0,0])

    myball.move()
    screen.blit(myball.image,myball.rect)

    clock.tick(30)
    pygame.display.flip()

pygame.quit()
