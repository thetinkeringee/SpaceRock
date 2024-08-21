import pygame
from circleshape import CircleShape
from constants import (PLAYER_SHOOT_SPEED, SHOT_RADIUS)
from typing import Tuple

class Shot(CircleShape):
    containers: Tuple

    def __init__(self,x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        vec = pygame.Vector2(0,1).rotate(rotation)
        self.velocity = vec * PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        width = 2
        white = pygame.Color(255,255,255)
        pygame.draw.circle(screen, white, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt



