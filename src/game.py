import pygame
from utils.load_db import load_db
from ecs.world import world
import config
import random


def init():
    """
    Initialize game window and world
    """
    pygame.init()
    # pygame.display.set_icon()
    pygame.display.set_caption("TEST")
    window = pygame.display.set_mode(config.SCREEN_SIZE)
    window.fill((255,255,255))
    
    world = world.World()
    question_df = load_db("data/qa.csv")
    world.add_question_df(question_df)
    
    return world, window

def main():
    """
    """
    world, window = init()
    clock = pygame.time.Clock()
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.keys == pygame.K_ESCAPE:
                    running = False
                elif event.keys == pygame.K_RETURN:
                    print(world.question_df.content[random.randint(1,2)])
        
        clock.tick(config.FPS)
        
if __name__ == '__main__':
    main()