#!/usr/bin/python3
import pygame
import os
import settings
from controllers.KeybController import KeybController
from models.GameModel import GameModel
from views.GameView import GameView


def main():

    # Suggests to OS the window position. May not be honored
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    pygame.display.set_caption("beSharp Arkanoid")
    screen = pygame.display.set_mode((settings.GAME_WIDTH_PIXELS, settings.GAME_HEIGHT_PIXELS))


    # FPS control variables
    fps = 40
    clock = pygame.time.Clock()

    # Main loop control variables
    running = True

    # MVC objects
    ark_game = GameModel()
    game_view = GameView(ark_game, screen)
    game_controller = KeybController(ark_game)

    #game_controller = KeyboardController(snake_game)

    while running:

        # Events Handling by controller
        running = game_controller.events_handling(running)

        # Update the game after controller changed model
        ark_game.update_game()

        # Draw the game
        game_view.draw_game()

        pygame.display.flip()
        clock.tick(fps)
        


if __name__ == "__main__":
    main()
