import sys
import random
sys.path.append("../")
import config
import pygame
import pygame_gui

class World():
    def __init__(self) -> None:
        self.current_scene = "start"
        self.current_quiz_num = 0
        
    def process(self):
        if self.current_scene == "start":
            """
            スタート画面用の関数を実行する  
            """
        elif self.current_scene == "game":
            """
            ゲームプレイ用の関数を実行する
            """
        