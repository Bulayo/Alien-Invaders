import pygame
from player import Player

pygame.init()

# Setup
RES = WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode(RES)
pygame.display.set_caption("Alien Invaders")
FPS = 60
clock = pygame.time.Clock()

# Assets
player_img = pygame.image.load("assets/danger.png").convert_alpha()

# Objects
player = Player(WIDTH / 2, 550, player_img)

running = True
while running:

    clock.tick(FPS)
    WIN.fill((50, 50, 50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # draw
    player.draw(WIN)

    # update
    player.move()

    pygame.display.flip()

    

pygame.quit()