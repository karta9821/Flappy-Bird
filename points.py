import pygame


class Point(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.number = {f'{i}': pygame.image.load(f'sprites/{i}.png') for i in range(10)}
        self.location = location
        self.point0_image = None
        self.point1_image = None
        self.point2_image = None

    def draw(self, points, screen):
        points = str(points).zfill(3)
        self.point0_image = self.number[points[0]]
        self.point1_image = self.number[points[1]]
        self.point2_image = self.number[points[2]]
        screen.blit(self.point0_image, [self.location[0], self.location[1]])
        screen.blit(self.point1_image, [self.location[0] + self.point0_image.get_width() + 1,
                                        self.location[1]])
        screen.blit(self.point2_image, [self.location[0] + self.point1_image.get_width() + self.point0_image.get_width() + 2,
                                        self.location[1]])

    def draw_score(self, score, location, screen):
        points = str(score).zfill(3)
        self.point0_image = self.number[points[0]]
        self.point1_image = self.number[points[1]]
        self.point2_image = self.number[points[2]]
        screen.blit(self.point0_image, [location[0], location[1]])
        screen.blit(self.point1_image, [location[0] + self.point0_image.get_width() + 1,
                                        location[1]])
        screen.blit(self.point2_image,
                    [location[0] + self.point1_image.get_width() + self.point0_image.get_width() + 2,
                     location[1]])
