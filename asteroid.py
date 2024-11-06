import pygame
import circleshape
from constants import *
import random
# Base class for game objects
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        
      
    def draw(self, screen):
       
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt     

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        left_angle = self.velocity.rotate(angle)
        right_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_left.velocity = left_angle * 1.2
        asteroid_right.velocity = right_angle * 1.2