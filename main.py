# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots,updateable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.isColliding(asteroid):
                    asteroid.split()
                    shot.kill()



        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        

        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()

