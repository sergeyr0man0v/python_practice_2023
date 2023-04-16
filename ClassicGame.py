from Game import *


class ClassicGame(Game):
    static_record = 0
    snake = None
    apple = None

    def make_apple(self):
        apple = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL), \
            randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.apple = Apple(*apple)

    def __init__(self):
        self.FPS = 10
        self.score = 0
        x = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        y = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.snake = Snake(x, y)
        self.make_apple()

    def display(self):
        self.screen.blit(self.background, (0, 0))

        # self.is_paused()
        # self.screen.fill(pygame.Color('black'))
        self.display_record()
        # show score
        self.display_score()

        # drawing snake and apple
        for i, j in self.snake.coord:
            pygame.draw.rect(self.screen, self.snake.color, (i, j, self.CELL - 2, self.CELL - 2))
        self.screen.blit(self.apple_img, self.apple.get_coord())

    def move(self):
        self.snake.move()

    def get_result(self):
        # eat apple
        if self.snake.get_head() == self.apple.get_coord():
            self.make_apple()
            self.snake.length += 1
            self.score += 1
            self.FPS += 1

    def game_over(self):
        # game over
        x, y = self.snake.get_head()
        if x < self.CELL or x > self.WIDTH - 2 * self.CELL or y < self.CELL or y > self.WIDTH - 2 * self.CELL or \
                len(self.snake.coord) != len(set(self.snake.coord)):
            self.update_record()
            return True
