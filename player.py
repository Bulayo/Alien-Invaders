import pygame

class Player:

    def __init__(self, x, y, image, bullet_sfx, hurt_sfx):
        self.image = image
        self.rect = self.image.get_rect(center= (x, y))
        self.height = self.image.get_height()
        self.bullet_group = pygame.sprite.Group()
        self.bullet_sfx = bullet_sfx
        self.hurt_sfx = hurt_sfx

    def draw(self, win):
        win.blit(self.image, self.rect)
        self.bullet_group.draw(win)
        self.bullet_group.update()

    def move(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        dx = 0

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left + dx > 0:
            dx = -3

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right + dx < 700:
            dx = 3

        if keys[pygame.K_SPACE] or mouse[0]:
            if len(self.bullet_group) == 0:
                bullet = Bullet(self.rect.centerx, (self.rect.centery - (self.height / 2)))
                self.bullet_sfx.play()
                self.bullet_group.add(bullet)

        self.rect.x += dx


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        

    def update(self):

        self.rect.y -= 7

        if self.rect.bottom < 0:
            self.kill()
