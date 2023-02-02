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
        self.clock = pygame.time.Clock()
        self.FPS = 60
    
    def add_quiz_data(self, quiz_data):
        self.quiz_data = quiz_data
        self.quiz_data.origin_content = self.quiz_data.content.copy()
        self.len_quiz = len(self.quiz_data.content)
        print(self.quiz_data)
        
    def add_scene_manager(self, scene_manager):
        self.scene_manager = scene_manager
        self.scene_manager.self = self
    
    def add_window(self, window):
        self.window = window
    
    def add_pygame_gui_manager(self, manager):
        self.manager = manager
        
    def show_quiz(self):
        
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
        
        if self.current_quiz_num >= self.len_quiz:
            self.current_scene = "result_scene"

        pygame.display.update()
        
    def _update_quiz(self):
        self.current_quiz_num += 1
        self._next_quiz_index = random.randint(0, len(self.quiz_data.content)-1)
        self.next_quiz = self.quiz_data.content.iloc[self._next_quiz_index]
        self.quiz_data.content = self.quiz_data.content.drop(index=[self._next_quiz_index]).reset_index(drop=True)
    
    
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
    
    def process_choices(self):
        if self.next_quiz["type"] == "4択":
            self._process_choices()
            # message = ""
            # for choice in self.next_quiz["choices"]:
            #     message += f"{choice}, "
            # message = message[:-2]
            # message = self.font.render(message, True, (10,10,10))
            # message_pos = message.get_rect(center = (config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
            
            # self.window.blit(message, message_pos)
            
        else:
            pass
        
        pygame.display.flip()
        pygame.display.update()
        
    def _process_choices(self):
        buttons = []
        for i,choice in enumerate(self.next_quiz["choices"]):
            buttons.append(pygame_gui.elements.UIButton(pygame.Rect((350*(i+1), 275*(i+1)), (100, 50)),
                            text=choice, manager=self.manager))
            
        pass
    
    
    def process_input(self):
        pass

    def _process_input(self):
        pass
    
    def show_start_screen(self):
        
        self.quiz_data.content = self.quiz_data.origin_content.copy()
        self.current_quiz_num = 0
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
        
    def show_result(self):
        for event in pygame.event.get():
                print(event, "in show_result")
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    print("Pressed key:", event.key)
                    if event.key == pygame.K_ESCAPE:
                        self.current_scene = "start_menu"
                    elif event.key == pygame.K_RETURN:
                        running = False
        self.window.fill((255,255,255))
        message = self.font.render("終了！", True, (10,10,10))
        message_pos = message.get_rect(center = (config.SCREEN_SIZE[0]//2, config.SCREEN_SIZE[1]//2))
        self.window.blit(message, message_pos)
        pygame.display.flip()
        pygame.display.update()
    
    def render(self):
        self.manager.update()

        self.window.blit("", (0, 0))
        self.manager.draw_ui(self.window)
        
    def process(self):
        if self.current_scene == "play_scene":
            self.handle_event()
            self.show_quiz()
            self.process_choices()
            self.process_input()
            self.render()

        elif self.current_scene == "start_menu":
            self.show_start_screen()
        
        elif self.current_scene == "result_scene":
            self.show_result()
            