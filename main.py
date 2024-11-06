# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
               
        screen.fill(SCREEN_COLOR)

        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            for shot in shots:                
                if asteroid.collide(shot):
                    asteroid.split()
            if asteroid.collide(player):
                print("Game over!")
                exit()
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()  # display update
        dt = clock.tick(FRAME_RATE) / 1000
if __name__ == "__main__":
    main()
    
    