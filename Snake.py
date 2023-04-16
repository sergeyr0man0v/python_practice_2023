import pygame


class Snake:
    curr = {'N': True, 'S': True, 'W': True, 'E': True}
    direction_keys = {
        'N': (pygame.K_w, pygame.K_UP),
        'S': (pygame.K_s, pygame.K_DOWN),
        'W': (pygame.K_a, pygame.K_LEFT),
        'E': (pygame.K_d, pygame.K_RIGHT)
    }
    coord = list()
    dx, dy = 0, 0
    length = 0
    color = "green"

    def __init__(self, x=0, y=0, CELL=50, color="green"):
        self.CELL = CELL
        self.coord.append((x, y))
        self.length = 1
        self.color = color

    def move(self, dx=0, dy=0):
        x, y = self.get_head()
        if dx == 0 and dy == 0:
            key = pygame.key.get_pressed()
            if any(key[i] for i in self.direction_keys['N']) and self.curr['N']:
                self.dx, self.dy = 0, -1
                self.curr = {'N': True, 'S': False, 'W': True, 'E': True}
            if any(key[i] for i in self.direction_keys['S']) and self.curr['S']:
                self.dx, self.dy = 0, 1
                self.curr = {'N': False, 'S': True, 'W': True, 'E': True}
            if any(key[i] for i in self.direction_keys['E']) and self.curr['E']:
                self.dx, self.dy = 1, 0
                self.curr = {'N': True, 'S': True, 'W': False, 'E': True}
            if any(key[i] for i in self.direction_keys['W']) and self.curr['W']:
                self.dx, self.dy = -1, 0
                self.curr = {'N': True, 'S': True, 'W': True, 'E': False}
        else:
            self.dx = dx
            self.dy = dy
        x += self.dx * self.CELL
        y += self.dy * self.CELL

        self.coord.append((x, y))
        self.coord = self.coord[-self.length:]
        # self.coord.pop(0)

    def get_head(self):
        return self.coord[-1]


