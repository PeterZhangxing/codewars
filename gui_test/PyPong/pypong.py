import pygame
import random

class MyBall(pygame.sprite.Sprite):

    def __init__(self,image_file,speed,location,screen,hit_wall,hit_top):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top,self.rect.left = location
        self.speed = speed

        self.hit_wall = hit_wall
        self.hit_top = hit_top

    def move(self):
        global score,score_surf,score_font

        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_rect().right:
            self.speed[0] = -self.speed[0]

            if self.rect.top <= screen.get_height():
                self.hit_wall.play()

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            self.hit_top.play()

            score += 1
            score_surf = score_font.render(str(score),1,(0,0,0))


class MyPaddle(pygame.sprite.Sprite):

    def __init__(self,location=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
pygame.mixer.init()
pygame.time.delay(1000)

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()

hit_paddle = pygame.mixer.Sound('hit_paddle.wav')
hit_paddle.set_volume(0.6)

hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.4)

get_point = pygame.mixer.Sound("get_point.wav")
get_point.set_volume(0.6)

splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.6)

new_life = pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.5)

bye = pygame.mixer.Sound("game_over.wav")
bye.set_volume(0.6)

myBall = MyBall('wackyball.bmp', [10,5], [50, 50],screen,hit_wall,get_point)
ball_group = pygame.sprite.Group()
ball_group.add(myBall)

mypaddle = MyPaddle([270,430])

score = 0
score_font = pygame.font.Font(None,50)
score_surf = score_font.render(str(score),1,(0,0,0))
score_pos = [10,10]

live = 3
done = False
flag = True
while flag:
    clock.tick(30)
    screen.fill([255,255,255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.MOUSEMOTION:
            mypaddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(mypaddle,ball_group,False):
        # myBall.speed[1] = -myBall.speed[1]
        hit_paddle.play()

        myBall.speed[1] = -1 * random.choice([8,12,18])
        myBall.speed[0] = -1 * random.choice([12,18,24])

    myBall.move()

    if not done:
        # myBall.move()
        for i in range(0,live):
            screen.blit(myBall.image, [screen.get_rect().width - 40 * i, 20])

        screen.blit(myBall.image,myBall.rect)
        screen.blit(mypaddle.image,mypaddle.rect)
        screen.blit(score_surf, score_pos)

        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        if not done:
            splat.play()
            live -= 1
        # print(live)
        if live <= 0:
            if not done:
                pygame.time.delay(1000)
                bye.play()

            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(score)

            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))

            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))

            screen.blit(ft1_surf,[screen.get_rect().width/2 - ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_rect().width/2 - ft2_surf.get_width()/2,200])

            done = True

            pygame.time.delay(1000)
            pygame.mixer.music.fadeout(2000)
            pygame.display.flip()
        else:

            pygame.time.delay(1000)
            myBall.rect.topleft = [50, 50]

            new_life.play()
            screen.blit(myBall.image, myBall.rect)
            pygame.display.flip()
            pygame.time.delay(1000)

pygame.quit()