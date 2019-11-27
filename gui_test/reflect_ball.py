
import pygame
import random

class MyBall(pygame.sprite.Sprite):

    def __init__(self,image_file,location,speed,des_fps):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top,self.rect.left = location
        # self.ori_speed = speed
        self.speed = speed
        self.des_fps = des_fps

    def move(self):
        # print(self.speed)
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] = -self.speed[1]

    # def get_actual_speed(self,frame_rate):
    #     # print(frame_rate)
    #     # if frame_rate == 0:
    #     #     self.speed = self.ori_speed
    #     #     return
    #     if frame_rate < self.des_fps:
    #         self.speed[0] = self.ori_speed[0] * (self.des_fps/frame_rate)
    #         self.speed[1] = self.ori_speed[1] * (self.des_fps/frame_rate)
    #         # print(self.speed)

size = width,height = 640,480
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])

ball_group = pygame.sprite.Group()
img = "./images/bomb.png"
des_fps = 300
screen.fill([255, 255, 255])
for row in range(3):
    for col in range(3):
        location = [120*col+10,120*row+10]
        speed = [random.choice([-2,2]),random.choice([-2,2])]
        myball = MyBall(img,location,speed,des_fps)
        ball_group.add(myball)
        screen.blit(myball.image, myball.rect)

pygame.display.flip()
pygame.time.delay(200)

def animate(ball_group):
    screen.fill([255, 255, 255])
    for ball in ball_group:
        # ball.get_actual_speed(frame_rate)
        ball.move()
    for ball in ball_group:
        ball_group.remove(ball)
        if pygame.sprite.spritecollide(ball,ball_group,False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        ball_group.add(ball)
        screen.blit(ball.image,ball.rect)

    pygame.display.flip()
    pygame.time.delay(20)

clock = pygame.time.Clock()
flag = True
count = 0
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            frame_rate = clock.get_fps()
            print('actual fps:%s'%frame_rate)

    # if count >= des_fps:
    #     frame_rate = clock.get_fps()
    #     if frame_rate != 0:
    #         print(frame_rate)
    #         animate(ball_group, int(frame_rate))
        # count = 0
    # count += 1
    animate(ball_group)
    clock.tick(des_fps)

pygame.quit()

