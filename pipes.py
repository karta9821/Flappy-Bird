import pygame
import random


class Pipe(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.drop = random.randint(0, 270)
        self.image = pygame.image.load('sprites/pipe-green.png')
        self.image_rotated = pygame.image.load('sprites/pipe-green.png')
        self.image_rotated = pygame.transform.rotate(self.image_rotated, 180)
        self.rect = self.image.get_rect()
        self.rect_rotated = self.image_rotated.get_rect()
        self.rect.left, self.rect.bottom = location[0], location[1] + self.drop
        self.rect_rotated.left, self.rect_rotated.bottom = location[0], self.rect.top - 135
        self.speed_x = - 1.5

    def __del__(self):
        pass

    def move(self):
        self.rect_rotated.left += self.speed_x
        self.rect.left += self.speed_x
        if self.rect.left < 0 - self.image.get_width():
            self.__del__()

    def get_mid_position(self):
        return [self.rect.left, self.rect.top - 90]

