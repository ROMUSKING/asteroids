import pygame
import circleshape
from constants import *
# Base class for game objects
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        
      
    def draw(self, screen):
       
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt     