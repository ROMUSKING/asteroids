import pygame
import circleshape
from constants import *
# Base class for game objects
class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)        
      
    def draw(self, screen):
       
        pygame.draw.circle(screen, SHOT_COLOR, self.position, SHOT_RADIUS, SHOT_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt     