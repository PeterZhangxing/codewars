import pygame
import random

class MyBall(pygame.sprite.Sprite):

    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

size = width,height = 640,480
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])

def animate(group):
    screen.fill([255,255,255])

    for ball in group:
        ball.move()

    for ball in group:
        group.remove(ball)

        if pygame.sprite.spritecollide(ball,group,False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)
        screen.blit(ball.image,ball.rect)

    pygame.display.flip()
    pygame.time.delay(20)

image_file = "images/beach_ball.png"
# ball_li = []
group = pygame.sprite.Group()
for row in range(3):
    for column in range(3):
        location = [column*180+10,row*180+10]
        speed = [random.choice([-2,2]),random.choice([-2.2])]
        myball = MyBall(image_file,location,speed)
        group.add(myball)

flag = True
# while flag:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             flag = False
#
#     pygame.time.delay(20)
#     screen.fill([255,255,255])
#
#     for ball in ball_li:
#         ball.move()
#         screen.blit(ball.image,ball.rect)
#
#     pygame.display.flip()

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    animate(group)

pygame.quit()