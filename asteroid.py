from circleshape import CircleShape
import pygame
from typing import Tuple

class Asteroid(CircleShape):
    containers: Tuple 

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 

    def draw(self, screen):
        width = 2
        white = pygame.Color(255,255,255)
        pygame.draw.circle(screen,white, self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)



    
