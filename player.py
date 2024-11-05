import pygame
import circleshape
from constants import PLAYER_RADIUS, PLAYER_COLOR, PLAYER_LINE_WIDTH, PLAYER_TURN_SPEED
# Base class for game objects
class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), PLAYER_LINE_WIDTH)

    def update(self, dt):
        # sub-classes must override
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt