import pygame

from Game import *


class GhostGame(Game):
    static_record = 0
    snake_real = None
    snake_ghost = None
    apple_real = None
    apple_ghost = None
    ghost_snake_color = (108, 224, 158)

    def make_apple(self):
        apple = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL), \
            randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        """self.apple_real = self.apple_ghost
        self.apple_ghost = Apple(*apple)"""
        self.apple_real = Apple(*apple)
        self.apple_ghost = Apple(self.WIDTH - self.CELL - apple[0], self.WIDTH - self.CELL - apple[1])

    def __init__(self):
        self.FPS = 10
        self.score = 0
        x1 = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        y1 = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.snake_real = Snake(x1, y1)
        x2 = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        y2 = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.apple_ghost = Apple(x2, y2)
        self.make_apple()

    def display(self):
        self.screen.blit(self.background, (0, 0))

        # self.is_paused()
        # self.screen.fill(pygame.Color('black'))
        self.display_record()
        # show score
        self.display_score()

        # drawing snake and apple
        for i, j in self.snake_real.coord:
            pygame.draw.rect(self.screen, self.snake_real.color, (i, j, self.CELL - 2, self.CELL - 2))
            # drawing ghost snake
            pygame.draw.rect(self.screen, self.ghost_snake_color, (self.WIDTH - i - self.CELL, self.WIDTH - j- self.CELL, self.CELL - 2, self.CELL - 2))
        self.screen.blit(self.apple_img, self.apple_real.get_coord())
        # drawing ghost apple
        pygame.draw.rect(self.screen, pygame.Color("grey"), (self.apple_ghost.x, self.apple_ghost.y, self.CELL - 2, self.CELL - 2))
        # self.screen.blit(self.apple_img, self.apple_ghost.get_coord())

    def move(self):
        self.snake_real.move()

    def get_result(self):
        # eat apple
        if self.snake_real.get_head() == self.apple_real.get_coord():
            self.make_apple()
            self.snake_real.length += 1
            self.score += 1
            # self.FPS += 1

    def game_over(self):
        # game over
        x, y = self.snake_real.get_head()
        if x < self.CELL or x > self.WIDTH - 2 * self.CELL or y < self.CELL or y > self.WIDTH - 2 * self.CELL or \
                len(self.snake_real.coord) != len(set(self.snake_real.coord)) or self.crash_with_ghost():
            self.update_record()
            return True

    def crash_with_ghost(self):
        for i, j in self.snake_real.coord:
            for x, y in self.snake_real.coord:
                if i == self.WIDTH - self.CELL - x and j == self.WIDTH - self.CELL - y:
                    return True
        return False
