import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, image, can_shoot):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft= (x, y))
        self.height = self.image.get_height()
        self.bullet_group = pygame.sprite.Group()
        self.can_shoot = can_shoot
        self.move_speed = 50
        self.move_time = 1500
        self.can_move = pygame.time.get_ticks()


    def update(self, win):

        if (pygame.time.get_ticks() - self.can_move) > self.move_time:
            self.rect.x += self.move_speed
            self.can_move = pygame.time.get_ticks()

        if self.rect.right > 700:
            self.rect.y += 50
            self.rect.right = 700
            self.move_speed = -50
        
        elif self.rect.left < 0:
            self.rect.y += 50
            self.rect.left = 0
            self.move_speed = 50
        
        if self.can_shoot == 1 and len(self.bullet_group) == 0:
            bullet = Bullet(self.rect.centerx, self.rect.centery + self.height)
            self.bullet_group.add(bullet)

        self.bullet_group.draw(win)
        self.bullet_group.update()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        

    def update(self):

        self.rect.y += 3

        if self.rect.top > 700:
            self.kill()


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, spawn, image):
        super().__init__()
        self.image = image
        self.spawn_pos = spawn
        if self.spawn_pos == 0:
            self.rect = self.image.get_rect(topleft = (800, 0))
        else:
            self.rect = self.image.get_rect(topleft = (-100, 0))

    def update(self):

        if self.spawn_pos == 0:
            self.rect.x -= 5
            if self.rect.right < 0:
                self.kill()

        else:
            self.rect.x += 5
            if self.rect.left > 700:
                self.kill()

        