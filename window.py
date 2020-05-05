import pygame
import birds
import pipes
import coins
import points
import music
import medals

pygame.init()

screen = pygame.display.set_mode((400, 624))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
audio = music.Music()

with open("score", 'r') as file:
    saved_score = file.readline()


class Background(pygame.sprite.Sprite):
    def __init__(self, image_landscape, image_base, location_landscape, location_base):
        pygame.sprite.Sprite.__init__(self)
        self.image_landscape = pygame.image.load(image_landscape)
        self.image_base = pygame.image.load(image_base)
        self.rect_landscape = self.image_landscape.get_rect()
        self.rect_base = self.image_base.get_rect()
        self.rect_landscape.left, self.rect_landscape.top = location_landscape
        self.rect_base.left, self.rect_base.top = location_base


def set_landscape(x_pos1, x_pos2, bg_day):
    x_pos1 -= 1.5
    x_pos2 -= 1.5
    if x_pos1 < bg_day.image_landscape.get_width() * - 1:
        x_pos1 = bg_day.image_landscape.get_width()
    if x_pos2 < bg_day.image_landscape.get_width() * - 1:
        x_pos2 = bg_day.image_landscape.get_width()

    screen.blit(bg_day.image_landscape, (x_pos1, 0))
    screen.blit(bg_day.image_landscape, (x_pos2, 0))
    return x_pos1, x_pos2


def set_base(x_pos1, x_pos2, bg_day):
    screen.blit(bg_day.image_base, (x_pos1, 512))
    screen.blit(bg_day.image_base, (x_pos2, 512))


def draw_pipes(pipes_list):
    for pipe in pipes_list:
        screen.blit(pipe.image, [pipe.rect.left, pipe.rect.top])
        screen.blit(pipe.image_rotated, [pipe.rect_rotated.left, pipe.rect_rotated.top])
        pipe.move()


def draw_coins(coins_list):
    for coin in coins_list:
        screen.blit(coin.image, [coin.rect.left, coin.rect.top])
        coin.move()


def stop(bg_game_over, bg_day, score):
    clock.tick(60)
    medal = medals.Medal([45, 840])
    score_location = [285, 825]
    if score > int(saved_score):
        medal.medal_select(True)
        score_o = points.Point(score_location)
        score_s = points.Point(score_location)
        sv_score = score
        with open("score", 'w') as file:
            file.write(str(score))
    else:
        medal.medal_select(False)
        score_o = points.Point([0, 0])
        score_s = points.Point([0, 0])
        sv_score = int(saved_score)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    main()
        if bg_game_over.rect_base.top > 112:
            bg_game_over.rect_base.top -= 8
            medal.rect.top -= 8
            score_location[1] -= 8
            screen.blit(bg_day.image_landscape, [bg_day.rect_landscape.left,bg_day.rect_landscape.top])
            screen.blit(bg_day.image_base, [bg_day.rect_base.left, bg_day.rect_base.top])
        screen.blit(bg_game_over.image_base, [0, bg_game_over.rect_base.top])
        screen.blit(medal.image, [medal.rect.left, medal.rect.top])
        score_o.draw_score(score, score_location, screen)
        score_s.draw_score(sv_score, [score_location[0], score_location[1]+70], screen)
        pygame.display.update()


def collision_detection(bird, pipes_list, score, coins_list, bg_game_over, bg_day):
    if bird.rect.bottom > 512 or bird.rect.top < 0:
        audio.play_die()
        stop(bg_game_over, bg_day, score)
    for pipe in pipes_list:
        if bird.check_collision(pipe.rect) or bird.check_collision(pipe.rect_rotated):
            audio.play_die()
            stop(bg_game_over, bg_day, score)
    for coin in coins_list:
        if bird.check_collision(coin.rect):
            coin.__del__()
            audio.play_point()
            coins_list.remove(coin)
            pygame.display.update()
            score += 1
    return score


def create_pipes_and_coins(point, pipes_list, coins_list):
    if pipes_list[-1].rect.left + 202 < 400 and point < 15:
        pipes_list.append(pipes.Pipe([400, 512]))
        coins_list.append(coins.Coin(pipes_list[-1].get_mid_position()))
    elif pipes_list[-1].rect.left + 182 < 400 and 15 <= point < 35:
        pipes_list.append(pipes.Pipe([400, 512]))
        coins_list.append(coins.Coin(pipes_list[-1].get_mid_position()))
    elif pipes_list[-1].rect.left + 152 < 400 and point >= 35:
        pipes_list.append(pipes.Pipe([400, 512]))
        coins_list.append(coins.Coin(pipes_list[-1].get_mid_position()))


bg_start = Background('sprites/message.png', 'sprites/message.png', [0, 0], [0, 0])


def main():
    bg_day = Background('sprites/background-day.png', 'sprites/base.png', [0, 0], [0, 512])
    bg_game_over = Background('sprites/game_over.png', 'sprites/game_over.png', [0, 655], [0, 655])
    bgx = 0
    bgx2 = bg_day.image_landscape.get_width()
    score = 0
    point = points.Point([170, 100])
    pipes_list = []
    coins_list = []
    bird = birds.Bird([150, 300])
    pipes_list.append(pipes.Pipe([400, 512]))
    coins_list.append(coins.Coin(pipes_list[-1].get_mid_position()))
    while True:
        score = collision_detection(bird, pipes_list, score, coins_list, bg_game_over, bg_day)
        create_pipes_and_coins(score, pipes_list, coins_list)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    bird.jump()
                    audio.play_fly()

        screen.fill([255, 255, 255])
        bgx, bgx2 = set_landscape(bgx, bgx2, bg_day)
        draw_coins(coins_list)
        bird.falling()
        draw_pipes(pipes_list)
        bird.update()
        screen.blit(bird.image, [bird.rect.left, bird.rect.top])
        set_base(bgx, bgx2, bg_day)
        point.draw(score, screen)
        pygame.display.update()
        clock.tick(60)
