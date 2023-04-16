from abc import abstractmethod
import pygame
from random import randrange
from Actors.Snake import *
from Actors.Apple import *


class Game:
    WIDTH = 900
    CELL = 50
    FPS = 10
    score = 0

    font_score = None
    font_res = None
    screen = None
    clock = None
    background = None
    apple_img = None

    '''_____This functions must be specified to each game mode___________'''

    @abstractmethod
    def display(self):
        """Displays current game"""
        pass

    @abstractmethod
    def move(self):
        """Reacts to user actions"""
        pass

    @abstractmethod
    def get_result(self):
        """Changes game status after user actions (snake eats apple or smth"""
        pass

    @abstractmethod
    def game_over(self):
        """Rule to finish the game"""
        pass

    '''___________________________________________________________________'''

    def update_record(self):
        self.__class__.static_record = max(self.__class__.static_record, self.score)

    def display_record(self):
        render_record = self.font_score.render(f'RECORD: {self.__class__.static_record}', 1, pygame.Color("orange"))
        self.screen.blit(render_record, (self.WIDTH - 5 * self.CELL - 5, 5))

    def display_score(self):
        render_score = self.font_score.render(f'SCORE: {self.score}', 1, pygame.Color("orange"))
        self.screen.blit(render_score, (self.CELL + 5, 5))

    def display_results(self):
        """Displays game over status"""
        while True:
            render_res = self.font_res.render('GAME OVER', 1, pygame.Color("orange"))
            self.screen.blit(render_res, (self.WIDTH // 2 - 250, self.WIDTH // 3))
            navigation = self.font_score.render('ENTER to continue / ESC to exit', 1, pygame.Color("black"))
            self.screen.blit(navigation, (self.WIDTH // 2 - 200, self.WIDTH - self.CELL))
            pygame.display.flip()
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                return True
            if key[pygame.K_ESCAPE]:
                return False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def pause(self):
        """Displays pause status"""
        unpause_key = (pygame.K_SPACE, pygame.K_RETURN)
        paused = True
        pause = self.font_res.render('PAUSED', 1, pygame.Color("orange"))
        self.screen.blit(pause, (self.WIDTH // 2 - 175, self.WIDTH // 3))
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                    if event.key in unpause_key:
                        paused = False
            pygame.display.update()
            self.clock.tick(60)
        return False

    def end(self):
        return self.display_results()

    def create_table(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.WIDTH))
        self.clock = pygame.time.Clock()
        self.font_score = pygame.font.SysFont('Arial', 28, bold=True)
        self.font_res = pygame.font.SysFont('Arial', 80, bold=True)
        self.background = pygame.image.load('Pictures/2.jpg').convert()
        self.apple_img = pygame.image.load('Pictures/apple.jpg').convert()

        pygame.display.update()

    def start(self):
        """Returns true if user wants to continue after game over"""
        self.create_table()

        while True:
            # rule to exit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                        if self.pause():
                            self.update_record()
                            return False

            self.display()

            self.move()

            self.get_result()

            if self.game_over():
                return self.end()
            else:
                pygame.display.flip()
                self.clock.tick(self.FPS)
