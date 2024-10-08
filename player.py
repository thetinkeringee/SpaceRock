from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
import pygame
from typing import Tuple
from shot import Shot

class Player(CircleShape):
    containers:Tuple

     
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)    
        self.position =  pygame.math.Vector2(x, y)
        self.rotation = 0
        self.shot_limiter = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white = pygame.Color(255, 255, 255)
        points = self.triangle()
        pygame.draw.polygon(screen, white, points, 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.shot_limiter > 0.0:
            self.shot_limiter -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)    
        if keys[pygame.K_d]:
            self.rotate(dt) 
        if keys[pygame.K_SPACE]:
            self.shoot()


    def move(self, dt):
        vec = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += vec * PLAYER_SPEED * dt

    def shoot(self): 
        if self.shot_limiter > 0:
            return

        shot = Shot(self.position.x, self.position.y, self.rotation)
        self.shot_limiter = PLAYER_SHOOT_COOLDOWN
        
        

