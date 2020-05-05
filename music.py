import pygame

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.audio = {
            'hit': 'audio/hit.wav',
            'point': 'audio/point.wav',
            'fly': 'audio/wing.wav',
        }
        self.loaded = None

    def play_die(self):
        self.loaded = pygame.mixer.Sound(self.audio['hit'])
        self.loaded.set_volume(0.15)
        self.loaded.play()

    def play_point(self):
        self.loaded = pygame.mixer.Sound(self.audio['point'])
        self.loaded.set_volume(0.15)
        self.loaded.play()

    def play_fly(self):
        self.loaded = pygame.mixer.Sound(self.audio['fly'])
        self.loaded.set_volume(0.15)
        self.loaded.play()