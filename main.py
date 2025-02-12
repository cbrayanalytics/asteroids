# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        clock.tick(60)

        dt = clock.get_time() / 1000

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
