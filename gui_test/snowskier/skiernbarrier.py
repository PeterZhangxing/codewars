import pygame
import random

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
        MyObstacle.speed = [ self.angle*2,6-abs(self.angle)*2 ]

    def move(self):
        self.rect.centerx = self.rect.centerx + MyObstacle.speed[0]

        if self.rect.centerx > 620:
            self.rect.centerx = 620
        elif self.rect.centerx < 20:
            self.rect.centerx = 20


class MyObstacle(pygame.sprite.Sprite):
    speed = [0, 6]

    def __init__(self,img_file,location,btype):
        super(MyObstacle,self).__init__()
        self.img_file = img_file
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.btype = btype
        self.passed = False

    def update(self, *args):
        self.rect.centery -= self.speed[1]
        if self.rect.bottom < 0:
            self.kill()


def create_obstacles(obstacles):
    loc_li = []
    for i in range(10):
        col = random.randint(0,9)
        row = random.randint(0,9)
        loc = [ col*64+32,row*64+32+640 ]
        if loc not in loc_li:
            loc_li.append(loc)
            btype = random.choice(["tree", "flag"])
            if btype == "tree":
                img = "skier_tree.png"
            else:
                img = "skier_flag.png"
            myobs = MyObstacle(img,loc,btype)
            obstacles.add(myobs)

def animate(obstacles):
    screen.fill([255,255,255])
    screen.blit(skier.img, skier.rect)
    obstacles.draw(screen)
    screen.blit(score_text,[10,10])
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)

skier = MySkier()
obstacle_group = pygame.sprite.Group()
create_obstacles(obstacle_group)
map_pos = 0
points = 0

flag = True
while flag:
    clock.tick(30)

    hit = pygame.sprite.spritecollide(skier, obstacle_group, False)
    # print('hit:', hit) # hit: [<MyObstacle sprite(in 1 groups)>]
    if hit:
        # print('hit[0]:', hit[0])
        # hit[0]: <MyObstacle sprite(in 1 groups)>
        if hit[0].btype == 'tree' and not hit[0].passed:
            points = points - 100
            score_text = font.render("Score: " + str(points), 1, (0, 0, 0))
            skier.img = pygame.image.load("skier_crash.png")
            animate(obstacle_group)
            pygame.time.delay(2000)

            skier.img = pygame.image.load("skier_down.png")
            skier.angle = 0
            MyObstacle.speed = [0, 6]
            hit[0].passed = True

        elif hit[0].btype == "flag" and not hit[0].passed:
            points += 10
            hit[0].kill()

    score_text = font.render("Score: " + str(points), 1, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                skier.turn(-1)
            if event.key == pygame.K_RIGHT:
                skier.turn(1)
            if event.key == pygame.K_SPACE:
                flag = False

    map_pos += MyObstacle.speed[1]
    if map_pos >= 640:
        create_obstacles(obstacle_group)
        map_pos = 0

    obstacle_group.update()
    skier.move()
    animate(obstacle_group)

pygame.quit()