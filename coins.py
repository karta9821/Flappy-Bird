import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/coin.png')
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed_x = 1.5

    def __del__(self):
        pass

    def move(self):
        self.rect.left -= self.speed_x
