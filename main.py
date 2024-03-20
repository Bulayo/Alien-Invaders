import pygame, random
from player import Player
from enemy import Alien

pygame.mixer.init()
pygame.init()

# Setup
RES = WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode(RES)
pygame.display.set_caption("Alien Invaders")
FPS = 60
clock = pygame.time.Clock()

# Sound
lazar = pygame.mixer.Sound("assets/laserShoot.wav")
hurt = pygame.mixer.Sound("assets/hitHurt.wav")
enemy = pygame.mixer.Sound("assets/enemy.wav")
ship = pygame.mixer.Sound("assets/spaceship.wav") 

# Assets
player_img = pygame.image.load("assets/player.png").convert_alpha()
alien_img = pygame.image.load("assets/enemy_1.png").convert_alpha()

# Objects
player = Player(WIDTH / 2, 550, player_img, lazar, hurt)

# Groups
alien_group = pygame.sprite.Group()

for y in range(2, 5):
    for x in range(2, 13):

        alien = Alien(x * 50, y * 50, alien_img, random.randint(1, 7))
        alien_group.add(alien)


running = True
while running:

    clock.tick(FPS)
    WIN.fill((50, 50, 50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # draw
    player.draw(WIN)
    alien_group.draw(WIN)

    # update
    player.move()
    alien_group.update(WIN)

    # collisions
    if pygame.sprite.groupcollide(alien_group, player.bullet_group, True, True):
        hurt.play()

    # spawning enemies
    if len(alien_group) == 0:
        for y in range(2, 5):
            for x in range(2, 13):

                alien = Alien(x * 50, y * 50, alien_img, random.randint(1, 7))
                alien_group.add(alien)

    pygame.display.flip()

pygame.quit()