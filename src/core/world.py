import sys
import random
sys.path.append("../")
import config
import pygame
import pygame_gui

class World():
    def __init__(self) -> None:
        self.running = True
        
        self.font = pygame.font.SysFont("Noto Sans JP", 18, bold=True)
        self.tag_question = self.font.render("問題", True, (10,10,10))
        
        self.curernt_scene = "start_menu"
        self.current_quiz_num = 0
    
    def add_question_df(self, question_df):
        self.question_df = question_df
        self.len_quiz = len(self.question_df.content)
        print(self.question_df)
        
    def add_scene_manager(self, scene_manager):
        self.scene_manager = scene_manager
        self.scene_manager.self = self
    
    def add_window(self, window):
        self.window = window
        
    def update_quiz(self):
        
        self.window.fill((255,255,255))
        
        try:
            # print(self.next_quiz)
            question = self.font.render(self.next_quiz.question, True, (10,10,10))
            pos_question = question.get_rect(center = (config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
            pos_question[1] = pos_question[1] - 100
            self.window.blit(self.tag_question, (100,config.SCREEN_SIZE[1]//2 - 160))
            self.window.blit(question, pos_question)
            
            state = f"{self.current_quiz_num}/ {self.len_quiz}"
            message_state = self.font.render(state, True, 20)
            self.window.blit(message_state, (config.SCREEN_SIZE[0]-80, 100))
        except:
            pass

        pygame.display.update()
    
    def handle_event(self):
        for event in pygame.event.get():
            print(event, "in show_quiz")
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                print("Pressed key:", event.key)
                if event.key == pygame.K_ESCAPE:
                    self.current_scene = "start_menu"
                elif event.key == pygame.K_RETURN:
                    self._update_quiz()
                    
    def wait_till_start(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                print(event, "in show_quiz")
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    print("Pressed key:", event.key)
                    if event.key == pygame.K_ESCAPE:
                        self.current_scene = "start_menu"
                    elif event.key == pygame.K_RETURN:
                        running = False
            
            self.window.fill((255,255,255))
            message = self.font.render("エンターを押すとゲームスタート！", True, (10,10,10))
            pos_message = message.get_rect(center = (config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
            self.window.blit(message, pos_message)

            pygame.display.flip()
            pygame.display.update()
            clock.tick(config.FPS)
        
        self._update_quiz()
    
    def _update_quiz(self):
        self.current_quiz_num += 1
        self._next_quiz_index = random.randint(0, len(self.question_df.content)-1)
        self.next_quiz = self.question_df.content.iloc[self._next_quiz_index]
        self.question_df.content = self.question_df.content.drop(index=[self._next_quiz_index]).reset_index(drop=True)
        
    
    def main_menu(self):
        
        self.window.fill((255,255,255))
        message = self.font.render("エンターキーを押して!", True, (10,10,10))
        message_goto_menu = self.font.render("Ecsキーを押してメニューに戻る", True, 16)
        title_font = pygame.font.SysFont("Noto Sans JP", 32, bold=True)
        title = title_font.render("クイズゲーム", True, (10,10,10))
        pos_title = title.get_rect(center=(config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
        pos_message_goto_menu = message_goto_menu.get_rect(center=(config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
        pos_message_goto_menu[1] += 50
        pos_title[1] = 100
        pos_message = message.get_rect(center=(config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
        self.window.blit(message, pos_message)
        self.window.blit(title, pos_title)
        self.window.blit(message_goto_menu, pos_message_goto_menu)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_RETURN:
                    self.current_scene = "play_scene"
                    self.window.fill((255,255,255))
                    self.wait_till_start()
        pygame.display.flip()
        pygame.display.update()
        
    def process(self):
        if self.current_scene == "play_scene":
            self.handle_event()
            self.update_quiz()

        elif self.current_scene == "start_menu":
            self.main_menu()
            