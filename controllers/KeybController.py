import pygame


class KeybController:

    def __init__(self, game_model):
        self.game_model = game_model

    def events_handling(self, running):

        #pressed = 0
        #acceleration = 0
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game_model.bar.acceleration=-4
                elif event.key == pygame.K_RIGHT:
                    self.game_model.bar.acceleration=4
                elif event.key == pygame.K_SPACE:
                    self.game_model.bar.acceleration=0
                #elif event.key == pygame.K_SPACE and self.game_model.game_over:
                   #self.game_model.reset()
                break  # Avoid multiple key to be handled in a single frame draw

        return running
