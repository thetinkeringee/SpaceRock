#! /usr/bin/python
import pygame
from constants import *
from player import Player


def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    clock = pygame.time.Clock()
    dt: float = 0.0

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)


        pygame.display.flip()

        ticks = clock.tick( 60.0 ) 
        dt = ticks / 1000.0 # Convert to milliseconds



if __name__ == "__main__":
    main()
