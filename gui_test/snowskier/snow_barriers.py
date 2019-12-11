import pygame
import random


pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()

class MyObstacle(pygame.sprite.Sprite):
    speed = [0, 6]

    def __init__(self,img_file,location,type):
        super(MyObstacle,self).__init__()
        self.img_file = img_file
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type

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
    obstacles.draw(screen)
    pygame.display.flip()

obstacle_group = pygame.sprite.Group()
create_obstacles(obstacle_group)
map_pos = 0
flag = True
while flag:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    map_pos += MyObstacle.speed[1]
    if map_pos >= 640:
        create_obstacles(obstacle_group)
        map_pos = 0

    obstacle_group.update()
    animate(obstacle_group)

pygame.quit()