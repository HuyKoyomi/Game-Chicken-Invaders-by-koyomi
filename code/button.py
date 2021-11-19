import pygame
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Button:
    def __init__(self, x, y, image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x, y)
        self.click=False
    def draw(self):
        acttion=False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click=True
                acttion=True
        if pygame.mouse.get_pressed()[0]==0:
            self.click=False
        game_screen.blit(self.image, (self.rect.x, self.rect.y))
        return acttion
