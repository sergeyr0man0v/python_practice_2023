from GameModes.Game import *


class DeadlyCocktailGame(Game):
    static_record = 0
    snake = None
    apple = None
    poison = None
    poison_color = (178, 181, 0)

    def make_apple(self):
        apple = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL), \
            randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.apple = Apple(*apple)

    def make_poison(self):
        dx, dy = self.apple.x, self.apple.y
        x = randrange(max(self.CELL, dx - 3 * self.CELL), min(self.WIDTH - self.CELL, dx + 3 * self.CELL), self.CELL)
        y = randrange(max(self.CELL, dy - 3 * self.CELL), min(self.WIDTH - self.CELL, dy + 3 * self.CELL), self.CELL)
        while dx == x and dy == y and any(x == i and y == j for i, j in self.snake.coord):
            x = randrange(max(self.CELL, dx - 3 * self.CELL), min(self.WIDTH - self.CELL, dx + 3 * self.CELL),
                          self.CELL)
            y = randrange(max(self.CELL, dy - 3 * self.CELL), min(self.WIDTH - self.CELL, dy + 3 * self.CELL),
                          self.CELL)
        self.poison = Apple(x, y)

    def __init__(self):
        self.FPS = 10
        self.score = 0
        x = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        y = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.snake = Snake(x, y)
        self.make_apple()
        self.make_poison()

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

        # drawing poison
        pygame.draw.rect(self.screen, self.poison_color, (self.poison.x, self.poison.y, self.CELL - 2, self.CELL - 2))

    def move(self):
        self.snake.move()

    def get_result(self):
        # eat apple
        if self.snake.get_head() == self.apple.get_coord():
            self.make_apple()
            self.make_poison()
            self.snake.length += 1
            self.score += 1
            self.FPS += 1

        if self.snake.get_head() == self.poison.get_coord():
            self.make_poison()
            ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for movement in range(4):
                dx, dy = ways[randrange(0, 4)]
                while (dx, dy) == self.snake.get_banned_way():
                    dx, dy = ways[randrange(0, 4)]
                self.display()
                self.snake.move(dx, dy)
                if self.game_over():
                    break
                pygame.display.flip()
                self.clock.tick(self.FPS)

    def game_over(self):
        # game over
        x, y = self.snake.get_head()
        if x < self.CELL or x > self.WIDTH - 2 * self.CELL or y < self.CELL or y > self.WIDTH - 2 * self.CELL or \
                len(self.snake.coord) != len(set(self.snake.coord)):
            self.update_record()
            return True
        return False
