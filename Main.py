import pygame
import window


if __name__ == '__main__':
    window.screen.blit(window.bg_start.image_base, (0, 0))
    pygame.display.update()
    while True:
        ev = pygame.event.wait()
        if ev.type == pygame.QUIT:
            pygame.quit()
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                window.main()
