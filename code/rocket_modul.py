# import main
import pygame

SETTING_BASE_SPEED = 5
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rocket_image = pygame.image.load('image/rocket.png')
rocket_image = pygame.transform.scale(rocket_image, (SCREEN_WIDTH/6, SCREEN_HEIGHT/3))
big_boom_image = pygame.image.load('image/vu_no_2.png')
big_boom_image = pygame.transform.scale(big_boom_image, (SCREEN_WIDTH/1.5, SCREEN_HEIGHT/1.5))
rocket_width  = big_boom_image.get_rect().width
rocket_height  = big_boom_image.get_rect().height
#===============================================

class Rocket:
    x_loc = 150
    y_loc =30
    x_loc = SCREEN_WIDTH // 2.5
    y_loc = SCREEN_HEIGHT - 1
    speed= 1.3
    hit = False
    boom_time = 0

    def draw(self):
        if self.boom_time > 0: # time nổ
            self.boom_time -= 1
            game_screen.blit(big_boom_image, [self.x_loc - rocket_width/2.5,-30])
            if self.boom_time == 0:
                self.hit = False
        
    def move(self):
        if self.boom_time <= 0:
            self.y_loc -= self.speed
            game_screen.blit(rocket_image, [self.x_loc,self.y_loc])
            if int(self.y_loc) == 155:
                self.boom_time = 40
                self.y_loc = SCREEN_HEIGHT
    
    