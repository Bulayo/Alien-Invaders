import pygame, random
from player import Player
from enemy import Alien, SpaceShip

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
ship = pygame.mixer.music.load("assets/spaceship.wav") 
pygame.mixer.music.play()

# Assets
player_img = pygame.image.load("assets/player.png").convert_alpha()

enemy = []
for file in range(5):
    enemy.append(pygame.image.load(f"assets/enemy_{file}.png").convert_alpha())

ship_img = pygame.image.load("assets/spaceship.png").convert_alpha()

# Objects
player = Player(WIDTH / 2, 550, player_img, lazar, hurt)


# Groups
alien_group = pygame.sprite.Group()
ship_group = pygame.sprite.Group()

for y in range(2, 7):
    for x in range(2, 13):
        if y == 2:
            alien = Alien(x * 50, y * 50, enemy[2], random.randint(1, 7))
        
        elif y > 2 and y <= 4:
            alien = Alien(x * 50, y * 50, enemy[0], random.randint(1, 7))

        elif y > 4:
            alien = Alien(x * 50, y * 50, enemy[4], random.randint(1, 7))

        alien_group.add(alien)


running = True
while running:

    clock.tick(FPS)
    WIN.fill((40, 40, 40))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # draw
    player.draw(WIN)
    alien_group.draw(WIN)
    ship_group.draw(WIN)

    # update
    player.move()
    alien_group.update(WIN)
    ship_group.update()

    # collisions
    if pygame.sprite.groupcollide(alien_group, player.bullet_group, True, True):
        hurt.play()

    if pygame.sprite.groupcollide(ship_group, player.bullet_group, True, True):
        hurt.play()

    # spawning enemies
    if len(alien_group) == 0:
        for y in range(2, 7):
            for x in range(2, 13):
                if y == 2:
                    alien = Alien(x * 50, y * 50, enemy[2], random.randint(1, 7))
                
                elif y > 2 and y <= 4:
                    alien = Alien(x * 50, y * 50, enemy[0], random.randint(1, 7))

                elif y > 4:
                    alien = Alien(x * 50, y * 50, enemy[4], random.randint(1, 7))

                alien_group.add(alien)

    if random.randint(1, 500) == 1:
        if len(ship_group) == 0:
            spaceship = SpaceShip(random.randint(0, 1), ship_img)
            ship_group.add(spaceship)
            pygame.mixer.music.play()


    pygame.display.flip()

pygame.quit()