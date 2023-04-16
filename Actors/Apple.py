import pygame


class Apple:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y
