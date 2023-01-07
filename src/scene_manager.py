import pygame
from core import world

class SceneManager():
    def __init__(self, world) -> None:
        self.current_scene = "start_menu"
        self.world = world

    def update_scene(self, scene:str):
        self.world.current_scene = scene
        # self._update_scene()
    
    def _update_scene(self):
        pass