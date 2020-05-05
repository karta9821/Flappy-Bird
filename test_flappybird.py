import unittest
import pygame
import birds
import pipes
import points
import window
import coins


class PointsTest(unittest.TestCase):

    def test_string_convert(self):
        self.point = points.Point([0, 0])
        self.screen = pygame.display.set_mode((0, 0))
        self.point.draw(52, self.screen)
        self.assertEqual(self.point.point0_image, self.point.number['0'])
        self.assertEqual(self.point.point1_image, self.point.number['5'])
        self.assertEqual(self.point.point2_image, self.point.number['2'])


class PipesTest(unittest.TestCase):

    def test_gap(self):
        self.pipe = pipes.Pipe([0, 0])
        self.assertEqual(self.pipe.rect.top - self.pipe.rect_rotated.bottom, 135)


class BirdTest(unittest.TestCase):

    def setUp(self):
        self.bird = birds.Bird([0, 0])

    def test_jump(self):
        self.bird.jump()
        self.assertEqual(self.bird.speed_y, -5)

    def test_image(self):
        self.bird.speed_y = 3
        self.bird.falling()

        self.assertEqual(self.bird.image, self.bird.images['mid'])
        self.bird.speed_y = 2.4
        self.bird.falling()

        self.assertEqual(self.bird.image, self.bird.images['down'])
        self.bird.speed_y = -3
        self.bird.falling()
        self.assertEqual(self.bird.image, self.bird.images['up'])

    def test_collision(self):
        self.pipe = pipes.Pipe([0, 0])
        self.bird.check_collision(self.pipe.rect)


class WindowTest(unittest.TestCase):

    def test_collision(self):
        self.bird = birds.Bird(([0, 0]))
        self.coin_list = [coins.Coin([0, 0])]
        self.coins = 0
        self.bg_game_over = window.Background('sprites/game_over.png', 'sprites/game_over.png', [0, 0], [0, 0])
        self.coins = window.collision_detection(self.bird, [], self.coins, self.coin_list, self.bg_game_over)
        self.assertEqual(self.coins, 1)


if __name__ == '__main__':
    unittest.main()
