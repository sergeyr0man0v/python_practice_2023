from Game import *


class ObstaclesGame(Game):
    static_record = 0
    snake = None
    apple = None
    obstacles_map = None
    obstacles = None

    def make_apple(self):
        apple = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL), \
            randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
        self.apple = Apple(*apple)

    def make_obstacle(self):
        not_created = True
        while not_created:
            x = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
            y = randrange(self.CELL, self.WIDTH - self.CELL, self.CELL)
            if not self.obstacles_map.get((x, y), False):
                if x == self.apple.x and y == self.apple.y:
                    continue
                if (x, y) in self.snake.coord:
                    continue
                self.obstacles_map[(x, y)] = True
                self.obstacles.append((x, y))
                not_created = False

    def __init__(self):
        self.obstacles_map = dict()
        self.obstacles = list()
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
        for i, j in self.obstacles:
            pygame.draw.rect(self.screen, pygame.Color("black"), (i, j, self.CELL - 2, self.CELL - 2))
        self.screen.blit(self.apple_img, self.apple.get_coord())

    def move(self):
        self.snake.move()

    def get_result(self):
        # eat apple
        if self.snake.get_head() == self.apple.get_coord():
            self.make_apple()
            self.snake.length += 1
            self.score += 1
            # self.FPS += 1
            self.make_obstacle()

    def game_over(self):
        # game over
        x, y = self.snake.get_head()
        if x < self.CELL or x > self.WIDTH - 2 * self.CELL or y < self.CELL or y > self.WIDTH - 2 * self.CELL or \
                len(self.snake.coord) != len(set(self.snake.coord)) or self.obstacles_map.get((x, y), False):
            self.update_record()
            return True
