import pygame

pygame.init()

RES = WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode(RES)
pygame.display.set_caption("Alien Invaders")
FPS = 60
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(FPS)
    WIN.fill((50, 50, 50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    

pygame.quit()