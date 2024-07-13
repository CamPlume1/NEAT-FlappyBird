import random

import neat.nn
import pygame

from Player import Player
from Column import UpperColumn, LowerColumn

# TODO: Figure out features
# Todo: Figure out eval Function: Candidate time
# Todo: Update scoring


def playGame(genomes, config):
    global timer, x_dist_next, low_vert_next, up_vert_next, low_vert_2nd, up_vert_second, dist_to_floor, dist_to_ceiling, vert_velo, bird_x, bird_y
    # Init game window
    pygame.init()
    #random.seed(7)

    # Show screen
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Hello World")

    players = []
    ge = []
    nets = []

    def remove(index):
        players.pop(index)
        ge.pop(index)
        nets.pop(index)

    # Create Sprite
    #players.append(Player())


    # Init generation
    for genome_id, genome in genomes:
        players.append(Player())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0


    # Init clock
    clock = pygame.time.Clock()
    FPS = 60

    # Create Game States
    score = 0
    timer = 0

    # Create Sprite Groups
    all_sprites = pygame.sprite.Group()

    # Run Game loop
    while ge != []:
        # Clear the screen
        screen.fill((255, 255, 255))
        # Tick Clock
        clock.tick(FPS)

        if timer % 200 == 0:
            center = random.randint(0, 350, ) + 225

            all_sprites.add(UpperColumn(center))
            all_sprites.add(LowerColumn(center))


        # Draw Players, columns
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
        for player in players:
            screen.blit(player.image, player.rect)
        pygame.display.flip()

        '''for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    players[0].jump()'''

        next_info = get_vert_next(all_sprites)

        for i in range(len(players)):
            feats = [next_info[0],
                              next_info[1],
                              next_info[2],
                              get_velocity(players[i]),
                              get_bird_y(players[i]),
                              dist_to_floor(players[i])]
            #print(feats)
            output = nets[i].activate(feats)#TODO)

            if output[0] > 0.5:
                players[i].jump()

        # Move Player, columns
        all_sprites.update()
        for player in players:
            player.update()

        # Increment fitness of surviving birds
        for gen in ge:
            gen.fitness +=1

        # Check for collisions between player and columns
        removal = []
        for i in range(len(players)):
            if pygame.sprite.spritecollide(players[i], all_sprites, False):
                # Collision detected, end the game
                removal.append(i)

            if players[i].rect.y < 0 or players[i].rect.y > 810:
                # Hit ceiling or floor, end game
                removal.append(i)

        for index in reversed(removal):
            remove(index)

        # Remove columns that move off the screen from tracking
        for sprite in all_sprites:
            if isinstance(sprite, UpperColumn) or isinstance(sprite, LowerColumn):
                if sprite.rect.x < -30:
                    sprite.kill()

       # print(len(all_sprites))

        timer += 1


def eval_func():
    return timer

# NEED:
# next upper bound 2
# next lower bound 3
# distance to next column break 4
def get_vert_next(sprite_list):
    upper = 0
    lower = 0
    x = 0
    up_flag = False
    low_flag = False
    # List is ordered, first instances will be closest to left
    for sprite in sprite_list:
        if sprite.rect.x > 305 and type(sprite) == UpperColumn and not up_flag:
            upper = sprite.bound
            up_flag = True
        if sprite.rect.x > 305 and type(sprite) == LowerColumn and not low_flag:
            lower = sprite.bound
            x = sprite.rect.x - 305
            low_flag = True
    return upper, lower, x

# 5
def dist_to_floor(a_sprite):
         return 800 - a_sprite.rect.y
# 6
def get_velocity(a_sprite):
    return a_sprite.velocity

# 7
def get_bird_y(a_sprite):
    return a_sprite.rect.y



