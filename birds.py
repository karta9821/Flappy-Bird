import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.images = {'mid': pygame.image.load('sprites/yellowbird-midflap.png'),
                       'up': pygame.image.load('sprites/yellowbird-upflap.png'),
                       'down': pygame.image.load('sprites/yellowbird-downflap.png')}
        self.image = self.images['mid']
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed_y = 1.5
        self.gravity = 0.2

    def jump(self):
        self.speed_y = -5

    def falling(self):
        if self.speed_y < 3:
            if self.speed_y < 0:
                self.image = self.images['up']
            else:
                self.image = self.images['down']
            self.speed_y += self.gravity
        else:
            self.image = self.images['mid']
        self.rect.top += self.speed_y

    def check_collision(self, sprite):
        if self.rect.colliderect(sprite):
            return True
