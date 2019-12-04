import pygame

pygame.init()

# initiate screen background and game loop clock
screen = pygame.display.set_mode([400,600])
screen.fill([0,0,0])
clock = pygame.time.Clock()

# initiate game elements and parameters
ship = pygame.image.load('lunarlander.png')
moon = pygame.image.load('moonsurface.png')

ground = 540 # ground y pos
start = 90 # mythrottle y pos
ship_mass = 5000.0
fuel = 5000.0
velocity = -100.0
gravity = 10
height = 2000
thrust = 0
delta_v = 0
y_pos = 90

def calculate_velocity():
    '''
    计算每一帧火箭的纵坐标值
    :return:
    '''
    global thrust, fuel, velocity, delta_v, height, y_pos

    delta_t = 1 / fps # time spend 1 frame
    thrust = (500 - mythrottle.rect.centery) * 5.0
    fuel -= thrust / (10 * fps)
    if fuel < 0: fuel = 0.0
    if fuel < 0.1: thrust = 0.0

    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel)) # 加速度
    velocity = velocity + delta_v # 速度
    delta_h = velocity * delta_t # 一帧时间内移动的高度
    height = height + delta_h
    y_pos = ground - (height * (ground - start) / 2000) - 90 # 将高度转换为y

def dis_status():
    '''
    显示当前游戏中每一针火箭的状态
    :return:
    '''
    v_str = "velocity: %i m/s" % velocity
    v_font = pygame.font.Font(None, 26)
    v_surf = v_font.render(v_str,1,(255,255,255))
    screen.blit(v_surf,[10,50])

    h_str = "height: %.1f" % height
    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, (255, 255, 255))
    screen.blit(h_surf, [10, 150])

    t_str = "thrust: %i" % thrust
    t_font = pygame.font.Font(None,26)
    t_surf = t_font.render(t_str,1,(255,255,255))
    screen.blit(t_surf,[10,200])

    a_str = "acceleration: %.1f" % (delta_v * fps)
    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, (255, 255, 255))
    screen.blit(a_surf, [10, 100])

    f_str = "fuel: %i" % fuel
    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, (255, 255, 255))
    screen.blit(f_surf, [60, 300])

def dis_final():
    '''
    游戏结束后显示的信息
    :return:
    '''
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 350, 280], 0)

    final1 = "Game over"
    f1_font = pygame.font.Font(None, 70)
    f1_surf = f1_font.render(final1, 1, (255, 255, 255))
    screen.blit(f1_surf, [20, 50])

    final2 = "You landed at %.1f m/s" % velocity
    f2_font = pygame.font.Font(None, 40)
    f2_surf = f2_font.render(final2, 1, (255, 255, 255))
    screen.blit(f2_surf, [20, 110])

    if velocity > -5:
        final3 = "Nice landing!"
        final4 = "I hear NASA is hiring!"
    elif velocity > -15:
        final3 = "Ouch! A bit rough, but you survived."
        final4 = "You'll do better next time."
    else:
        final3 = "Yikes! You crashed a 30 Billion dollar ship."
        final4 = "How are you getting home?"

    f3_font = pygame.font.Font(None, 26)
    f3_surf = f3_font.render(final3, 1, (255, 255, 255))
    screen.blit(f3_surf, [20, 150])

    f4_font = pygame.font.Font(None, 26)
    f4_surf = f4_font.render(final4, 1, (255, 255, 255))
    screen.blit(f4_surf, [20, 180])

    pygame.display.flip()

def dis_flames():
    '''
    显示三角形火焰，根据推理确定大小
    :return:
    '''
    flame_size = thrust / 15
    for i in range(2):
        startx = 252 - 10 + i * 19
        starty = y_pos + 83
        pygame.draw.polygon(
            screen,
            [255,109,14],
            [(startx, starty),(startx + 4, starty + flame_size),(startx + 8, starty)],
        )

class MyThrottle(pygame.sprite.Sprite):

    def __init__(self,location=[0,0]):
        super(MyThrottle,self).__init__()

        img_surf = pygame.surface.Surface([30,10])
        img_surf.fill([128,128,128])

        self.image = img_surf.convert()
        self.rect = self.image.get_rect()

        self.rect.left,self.rect.centery = location

mythrottle = MyThrottle([15,500])
# screen.blit(mythrottle.image,mythrottle.rect)
# pygame.display.flip()

held_down = False # if mouse button down
flag = True
while flag:
    clock.tick(30)
    fps = clock.get_fps()
    if fps < 1: fps = 30

    # if game is not over
    if height > 0.01:
        calculate_velocity()
        screen.fill([0,0,0])
        dis_status()

        # 画出燃料表轮廓
        pygame.draw.rect(screen, [0, 0, 255], [80, 350, 24, 100], 2)

        fuelbar = 96 * fuel / 5000
        # 燃油量
        pygame.draw.rect(screen, [0, 255, 0],[84, 448 - fuelbar, 18, fuelbar], 0)

        # 画出推进器滑块
        pygame.draw.rect(screen, [255, 0, 0],[25, 300, 10, 200], 0)

        screen.blit(moon, [0, 500, 400, 100]) # draw moon on the screen

        # 降落点
        pygame.draw.rect(screen, [60, 60, 60],[220, 535, 70, 5], 0)

        # 画出推力操纵杆
        screen.blit(mythrottle.image, mythrottle.rect)
        # 画出飞船
        screen.blit(ship, [230, y_pos, 50, 90])

        dis_flames()

        instruct1 = "Land softly without running out of fuel"
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, (255, 255, 255))
        screen.blit(inst1_surf, [50, 550])

        instruct2 = "Good landing: < 15m/s Great landing: < 5m/s"
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst1_font.render(instruct2, 1, (255, 255, 255))
        screen.blit(inst2_surf, [20, 575])

        pygame.display.flip()
    else:
        dis_final()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                mythrottle.rect.centery = event.pos[1]
                if mythrottle.rect.centery > 500:
                    mythrottle.rect.centery = 500
                if mythrottle.rect.centery < 300:
                    mythrottle.rect.centery = 300

pygame.quit()
