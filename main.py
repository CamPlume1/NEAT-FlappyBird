import random
import sys

import pygame
from Player import Player
from Column import UpperColumn, LowerColumn


def playGame():
    # Init game window
    pygame.init()

    # Show screen
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Hello World")

    # Init clock
    clock = pygame.time.Clock()
    FPS = 60

    # Create Game States
    score = 0
    timer = 0

    # Create Sprite Groups
    all_sprites = pygame.sprite.Group()

    # Create Sprite
    player = Player()

    # Run Game loop
    while True:
        # Clear the screen
        screen.fill((255, 255, 255))
        # Tick Clock
        clock.tick(FPS)

        if timer % 200 == 0:
            center = random.randint(0, 350) + 225

            all_sprites.add(UpperColumn(center))
            all_sprites.add(LowerColumn(center))
            print("Timer executed")

        # Draw Player, columns
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Move Player, columns
        all_sprites.update()
        player.update()

        # Check for collisions between player and columns
        if pygame.sprite.spritecollide(player, all_sprites, False):
            # Collision detected, end the game
            print("Game Over!")
            pygame.quit()
            break

        if player.rect.y < 0 or player.rect.y > 810:
            print("Game Over!")
            pygame.quit()
            break


        # Score Increment

        # Remove columns that move off the screen from tracking
        for sprite in all_sprites:
            if isinstance(sprite, UpperColumn) or isinstance(sprite, LowerColumn):
                if sprite.rect.x < -30:
                    sprite.kill()

        print(len(all_sprites))
        timer += 1

    # return timer as fit function
    return timer 

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Score: " + str(playGame()))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
