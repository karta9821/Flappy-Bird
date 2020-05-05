import pygame


class Medal(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.images = {
            'golden': pygame.image.load('sprites/golden_medal.png'),
            'silver': pygame.image.load('sprites/silver_medal.png')
        }
        self.location = location
        self.image = None
        self.rect = None

    def medal_select(self, new_record):
        if new_record:
            self.image = self.images['golden']
        else:
            self.image = self.images['silver']
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.location

