#! /usr/bin/python
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot


def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Player.containers= (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    



    clock = pygame.time.Clock()
    dt: float = 0.0

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for i in updateable:
            i.update(dt)

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            for s in shots:
                if s.collided(a):
                    s.kill()
                    a.split()
                    continue

            if player.collided(a):
                print("Game over!")
                return



        pygame.display.flip()

        ticks = clock.tick( 60.0 ) 
        dt = ticks / 1000.0 # Convert to milliseconds



if __name__ == "__main__":
    main()
