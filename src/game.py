import pygame
from utils.load_db import load_db
from core.world import World
import config
import random
from scene_manager import SceneManager


def init():
    """
    Initialize game window and world
    """
    pygame.init()
    # pygame.display.set_icon()
    pygame.display.set_caption("TEST")
    window = pygame.display.set_mode(config.SCREEN_SIZE)
    window.fill((255,255,255))
    
    world = World()
    world.add_window(window)
    question_df = load_db("../data/qa.csv")
    world.add_quiz_df(question_df)
    world.add_scene_manager(SceneManager(world))
    world.current_scene = "start_menu"
    return world, window

def main():
    """
    """
    world, window = init()
    clock = pygame.time.Clock()
    world.running = True
    while world.running:
        world.process()
        clock.tick(config.FPS)
        
if __name__ == '__main__':
    main()
