from ClassicGame import *
from ObstaclesGame import *
from GhostGame import *
from DeadlyCocktailGame import *
from Game import *
import pygame_menu

game = ClassicGame()


def set_difficulty(value, level):
    global game
    match level:
        case 1:
            game = ClassicGame()
        case 2:
            game = ObstaclesGame()
        case 3:
            game = GhostGame()
        case 4:
            game = DeadlyCocktailGame()
        case _:
            print("Something went wrong")


def start_the_game():
    global game
    game.__init__()
    game.create_table()
    while game.start():
        game.__init__()
        game.create_table()

    pygame.display.set_mode((600, 400))


pygame.init()
surface = pygame.display.set_mode((600, 400))
menu = pygame_menu.Menu("Welcome to zmeika mat' vashu", 600, 400,
                        theme=pygame_menu.themes.THEME_SOLARIZED)
menu.add.selector('Level :', [('Classic', 1), ('Obstacles', 2), ('Ghost', 3), ('DealyCocktail', 4)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
