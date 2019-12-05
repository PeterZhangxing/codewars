import pygame


class MyThrottle(pygame.sprite.Sprite):
    '''
    生成控制火箭推力大小的推杆的精灵类
    '''
    def __init__(self,location=[0,0]):
        super(MyThrottle,self).__init__()

        img_surf = pygame.surface.Surface([30,10])
        img_surf.fill([128,128,128])

        self.image = img_surf.convert()
        self.rect = self.image.get_rect()

        self.rect.left,self.rect.centery = location


class MyLLGame(object):
    '''
    游戏主逻辑类
    '''
    game_name = 'lunar lander'

    def __init__(self):
        '''
        初始化游戏及游戏中用到的资源
        '''
        pygame.init()
        self.screen = pygame.display.set_mode([400, 600])
        self.background = pygame.surface.Surface([400, 600])
        self.bag_img = self.background.convert()

        self.screen.fill([0, 0, 0])

        self.clock = pygame.time.Clock()

        self.ship = pygame.image.load('lunarlander.png')
        self.moon = pygame.image.load('moonsurface.png')

        self.ground = 540  # ground y pos
        self.start = 90  # mythrottle y pos
        self.ship_mass = 5000.0
        self.fuel = 5000.0
        self.velocity = -100.0
        self.gravity = 10
        self.height = 2000
        self.thrust = 0
        self.delta_v = 0
        self.y_pos = 90
        self.fps = 30

        self.mythrottle = MyThrottle([15, 500])


    def calculate_velocity(self):
        '''
        计算每一帧火箭的纵坐标值
        :return:
        '''
        delta_t = 1 / self.fps  # time spend 1 frame
        self.thrust = (500 - self.mythrottle.rect.centery) * 5.0
        self.fuel -= self.thrust / (10 * self.fps)
        if self.fuel < 0: self.fuel = 0.0
        if self.fuel < 0.1: self.thrust = 0.0

        self.delta_v = delta_t * (-self.gravity + 200 * self.thrust / (self.ship_mass + self.fuel))  # 加速度
        self.velocity = self.velocity + self.delta_v  # 速度
        delta_h = self.velocity * delta_t  # 一帧时间内移动的高度
        self.height = self.height + delta_h
        self.y_pos = self.ground - (self.height * (self.ground - self.start) / 2000) - 90  # 将高度转换为y

    def dis_flames(self):
        '''
        显示三角形火焰，根据推理确定大小
        :return:
        '''
        flame_size = self.thrust / 15
        for i in range(2):
            startx = 252 - 10 + i * 19
            starty = self.y_pos + 83
            pygame.draw.polygon(
                self.screen,
                [255, 109, 14],
                [(startx, starty), (startx + 4, starty + flame_size), (startx + 8, starty)],
            )

    def dis_status(self):
        '''
        显示当前游戏中每一针火箭的状态
        :return:
        '''
        v_str = "velocity: %i m/s" % self.velocity
        v_font = pygame.font.Font(None, 26)
        v_surf = v_font.render(v_str, 1, (255, 255, 255))
        self.screen.blit(v_surf, [10, 50])

        h_str = "height: %.1f" % self.height
        h_font = pygame.font.Font(None, 26)
        h_surf = h_font.render(h_str, 1, (255, 255, 255))
        self.screen.blit(h_surf, [10, 150])

        t_str = "thrust: %i" % self.thrust
        t_font = pygame.font.Font(None, 26)
        t_surf = t_font.render(t_str, 1, (255, 255, 255))
        self.screen.blit(t_surf, [10, 200])

        a_str = "acceleration: %.1f" % (self.delta_v * self.fps)
        a_font = pygame.font.Font(None, 26)
        a_surf = a_font.render(a_str, 1, (255, 255, 255))
        self.screen.blit(a_surf, [10, 100])

        f_str = "fuel: %i" % self.fuel
        f_font = pygame.font.Font(None, 26)
        f_surf = f_font.render(f_str, 1, (255, 255, 255))
        self.screen.blit(f_surf, [60, 300])

    def dis_final(self):
        '''
        飞船降落，游戏结束后显示的信息
        :return:
        '''
        pygame.draw.rect(self.screen, [0, 0, 0], [0, 0, 355, 285], 0)

        final1 = "Game over"
        f1_font = pygame.font.Font(None, 70)
        f1_surf = f1_font.render(final1, 1, (255, 255, 255))
        self.screen.blit(f1_surf, [20, 50])

        final2 = "You landed at %.1f m/s" % self.velocity
        f2_font = pygame.font.Font(None, 40)
        f2_surf = f2_font.render(final2, 1, (255, 255, 255))
        self.screen.blit(f2_surf, [20, 110])

        if self.velocity > -5:
            final3 = "Nice landing!"
            final4 = "I hear NASA is hiring!"
        elif self.velocity > -15:
            final3 = "Ouch! A bit rough, but you survived."
            final4 = "You'll do better next time."
        else:
            final3 = "Yikes! You crashed a 30 Billion dollar ship."
            final4 = "How are you getting home?"

        f3_font = pygame.font.Font(None, 26)
        f3_surf = f3_font.render(final3, 1, (255, 255, 255))
        self.screen.blit(f3_surf, [20, 150])

        f4_font = pygame.font.Font(None, 26)
        f4_surf = f4_font.render(final4, 1, (255, 255, 255))
        self.screen.blit(f4_surf, [20, 180])

        pygame.display.flip()

    def dis_final2(self):
        '''
        飞出游戏屏幕，游戏结束后显示的信息
        :return:
        '''
        pygame.draw.rect(self.screen, [0, 0, 0], [0, 0, 355, 285], 0)

        final1 = "Game over"
        f1_font = pygame.font.Font(None, 70)
        f1_surf = f1_font.render(final1, 1, (255, 255, 255))
        self.screen.blit(f1_surf, [20, 50])

        final2 = "You have flied back to the space!"
        f2_font = pygame.font.Font(None, 30)
        f2_surf = f2_font.render(final2, 1, (255, 255, 255))
        self.screen.blit(f2_surf, [20, 110])
        pygame.display.flip()

    def dis_instruction(self):
        # 在屏幕底部绘制游戏提示1
        instruct1 = "Land softly without running out of fuel"
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, (255, 255, 255))
        self.screen.blit(inst1_surf, [50, 550])

        # 在屏幕底部绘制游戏提示2
        instruct2 = "Good landing: < 15m/s Great landing: < 5m/s"
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst2_font.render(instruct2, 1, (255, 255, 255))
        self.screen.blit(inst2_surf, [20, 575])

        # 快捷键提示
        instruct3 = "Press s to reset the game,press t to quit!"
        inst3_font = pygame.font.Font(None, 15)
        inst3_surf = inst3_font.render(instruct2, 1, (255, 255, 255))
        self.screen.blit(inst3_surf, [5, 0])

    def game_loop(self):
        held_down = False
        self.flag = True
        outspace = False

        while self.flag:
            self.clock.tick(30)

            self.fps = self.clock.get_fps()
            if self.fps < 1:
                self.fps = 30

            if self.height > 0.01 and not outspace: # 如果还没有着陆
                self.calculate_velocity() # 更新每一帧游戏的状态信息
                self.screen.blit(self.bag_img, [0, 0])
                self.dis_status() # 将状态信息显示到图片上

                # 在屏幕上绘制游戏元素

                # 画出燃料表轮廓
                pygame.draw.rect(self.screen, [0, 0, 255], [80, 350, 24, 100], 2)

                # 绘制燃油量
                fuelbar = 96 * self.fuel / 5000
                pygame.draw.rect(self.screen, [0, 255, 0], [84, 448 - fuelbar, 18, fuelbar], 0)

                # 画出推进器滑块移动槽
                pygame.draw.rect(self.screen, [255, 0, 0], [25, 300, 10, 200], 0)

                # 绘制月球图片
                self.screen.blit(self.moon, [0, 500, 400, 100])  # draw moon on the screen

                # 绘制降落点
                pygame.draw.rect(self.screen, [60, 60, 60], [220, 535, 70, 5], 0)

                # 画出推力操纵杆
                self.screen.blit(self.mythrottle.image, self.mythrottle.rect)

                # 画出飞船
                self.screen.blit(self.ship, [230, self.y_pos, 50, 90])

                # 绘制火焰
                self.dis_flames()

                # 显示游戏提示信息
                self.dis_instruction()

                pygame.display.flip()

            elif not outspace:
                self.dis_final()
                # print(self.y_pos)

            if self.y_pos <= -86.0:
                # print(self.y_pos)
                outspace = True
                self.dis_final2()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    held_down = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    held_down = False
                elif event.type == pygame.MOUSEMOTION:
                    if held_down:
                        self.mythrottle.rect.centery = event.pos[1]
                        if self.mythrottle.rect.centery > 500:
                            self.mythrottle.rect.centery = 500
                        if self.mythrottle.rect.centery < 300:
                            self.mythrottle.rect.centery = 300

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        # print('S')
                        outspace = False
                        self.__init__()
                    elif event.key == pygame.K_t:
                        # print('T')
                        self.flag = False
        pygame.quit()


if __name__ == '__main__':

    myllgame = MyLLGame()
    myllgame.game_loop()