import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

splat = pygame.mixer.Sound('splat.wav')
splat.set_volume(0.5)
# splat.play(loops=10)

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=1)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    if not pygame.mixer.music.get_busy():
        splat.play()
        pygame.time.delay(1000)
        flag = False

pygame.quit()