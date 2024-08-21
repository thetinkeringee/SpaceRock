from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
from typing import Tuple
import random

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

    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0, 50.0)
        new_velocity1 = self.velocity.rotate(angle) * 1.2
        new_velocity2 = self.velocity.rotate(-angle) * 1.2
        smaller_radius = self.radius -ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        a2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        a1.velocity = new_velocity1
        a2.velocity = new_velocity2
    
