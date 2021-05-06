import pygame
import settings
from models.GameColors import GameColors


class GameView:

    def __init__(self, game_model, screen):
        pygame.font.init()
        self.game_model = game_model
        self.screen = screen
        self.__top_bar_font = pygame.font.SysFont('Arial', 24)
        self.__end_font = pygame.font.SysFont('Arial', 40)
        self.__restart_font = pygame.font.SysFont('Arial', 14)
        

    def draw_game(self):

        # Dark Background
        self.screen.fill(
            GameColors.BACKGROUND_DARK_COLOR.value,
            (0, 0, settings.GAME_WIDTH_PIXELS, settings.GAME_HEIGHT_PIXELS))

        # Top bar area
        self.screen.fill(
            GameColors.TOP_BAR_BACKGROUND_COLOR.value,
            (0, 0, settings.GAME_WIDTH_PIXELS, settings.TOP_BAR_HEIGHT_PIXELS))

        # Top bar text (score
        self.screen.blit(self.__top_bar_font.render(f"SCORE: {self.game_model.score}", True,
                                                    GameColors.TEXT_LIGHT.value), (10, 5))

        # Game field grid
        for ii in range(settings.TABLE_HEIGHT):
            for jj in range(ii % 1, settings.TABLE_WIDTH, 2):
                self.screen.fill(GameColors.BACKGROUND_LIGHT_COLOR.value,
                                 (jj * settings.CELL_DIMENSION_PIXELS,
                                  settings.TOP_BAR_HEIGHT_PIXELS + ii * settings.CELL_DIMENSION_PIXELS,
                                  settings.CELL_DIMENSION_PIXELS,
                                  settings.CELL_DIMENSION_PIXELS))
        
        #drawBar
        self.screen.blit(self.game_model.bar.bar_image,
                         (self.game_model.bar.position['x'],
                          self.game_model.bar.position['y']))

        #DICT COMP
        #a={key: value for (key, value) in iterator}
        #drawBall
        for element in self.game_model.ball:
            posBallxy = element.position
        

            self.screen.blit(element.ball_image,
                            (posBallxy['x'],
                            posBallxy['y'] ))

        #drawBlocks
        for i in range(len(self.game_model.level.blocks)):
            posBlockxy = self.game_model.level.blocks[i].position
            self.screen.blit(self.game_model.level.blocks[i].block_image,
                           (posBlockxy['x'],
                            posBlockxy['y']))

        

      