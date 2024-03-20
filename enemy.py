import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, image, can_shoot):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft= (x, y))
        self.height = self.image.get_height()
        self.bullet_group = pygame.sprite.Group()
        self.can_shoot = can_shoot


    def update(self, win):
        
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