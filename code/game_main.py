import pygame
import random
import sys

from Chicken_modul import chicken_thighs, chicken,chicken_missile 
from Base_modul import Base, Base_missile,Base_defense
from check_collision import check_base_missile_and_chicken, check_roket_and_chicken,update_chicken_hit,check_base_and_chicken_missile,check_base_and_chicken_thighs
from check_collision import check_base_missile_and_boss,check_base_and_boss_missile,check_roket_and_boss,check_base_and_boss
from rocket_modul import Rocket, rocket_width
from display_on_screen import display_on_screen,display_boss_hp,display_game_over,display_winner
from boss_modul import Boss,Boss_missile
import Base_modul

NUM_OF_CHICKEN = 0 

SETTING_BASE_SPEED = 7
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

LIGHT_YELLOW = (255, 255, 204)
winner_image =  pygame.image.load('image/winner.png')
winner_image  = pygame.transform.scale(winner_image , (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
font1 = pygame.font.SysFont('Algerian', 50)     # font chữ

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Chicken Invaders") # koyomi
clock = pygame.time.Clock()
pygame.key.set_repeat(10,20)   # giu nut se tang toc do

#-----------------------------------
background_image = pygame.image.load('image/bg.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

spaceship_hit_sound = pygame.mixer.Sound('music/spaceship_hit.ogg')
boom_sound = pygame.mixer.Sound('music/boom_sound.mp3')

# lay data de setting game
def read_setting_imformation():
    with open("setting_imformation") as file:     # doc file
        return int(file.read())

def main():
    #======================================================================================
    # khởi tạo biến
    chicken_list = []
    chicken_missile_list = []
    chicken_thighs_list = []
    for i in range(NUM_OF_CHICKEN):
        tmp = chicken()
        tmp.random_chicken()    
        chicken_list.append(tmp)
        tmp1 = chicken_missile()
        chicken_missile_list.append(tmp1)
        tmp2 = chicken_thighs()
        chicken_thighs_list.append(tmp2)
    
    # khởi tạo xe + đạn xe tăng + ten lua
    base = Base()
    base_missile = Base_missile()
    base_defense = Base_defense()
    rocket = Rocket() 

    # boss
    boss = Boss()
    boss_missile = Boss_missile()
    

    #====================================================================
    while True:

        game_screen.blit(background_image, [0, 0])

        # xe tăng + đạn + di chuyen dan 
        if base.game_over == "false":
            base.draw_base()
            base_missile.draw_base_missile()
            base_missile.move()
            base_defense.draw_defense(base)
            base.update_roket_and_defense(base_defense)
        else: display_game_over(base)
        
        base.check_game_over()
        base.check_winner(boss)
        
        
        boss.check_boss_appear(base,chicken_list,NUM_OF_CHICKEN)
        if boss.statu == 'appear':
            boss.draw_boss()
            boss.move()
            boss.boss_defense()
            boss_missile.draw_boss_missile()
            boss_missile.move()
            boss_missile.boss_hit(boss)
            check_base_missile_and_boss(boss,base_missile,base)
            check_base_and_boss_missile(base,boss_missile)
            check_base_and_boss(base,boss)
            
            display_boss_hp(boss)
        else: display_winner(base)
        
        # vẽ gà + trung ga
        for i in range(len(chicken_list)):
            chicken_list[i].draw_chicken()
            chicken_list[i].move()
            chicken_missile_list[i].chicken_hit(chicken_list[i])
            chicken_missile_list[i].draw_chicken_missile()
            chicken_missile_list[i].move()
            chicken_list[i].use_ray()
            chicken_list[i].chicken_defense()
            chicken_thighs_list[i].random_chicken_thighs(chicken_list[i])
            check_base_and_chicken_thighs(base,chicken_thighs_list[i])
        
        # check event
        for i in chicken_list:
            check_base_missile_and_chicken(i,base_missile,base)
            check_roket_and_chicken(i,rocket,base)
            update_chicken_hit(i)
        
        for i in chicken_missile_list:
            if base_defense.time <=0:
                check_base_and_chicken_missile(base,i)

        if rocket.hit == True:
            rocket.draw()
            rocket.move()
            check_roket_and_boss(boss,rocket,base)
        
        display_on_screen(base)
        
        #==========================================================================
        for even in pygame.event.get():
            
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # set up nút điều khiển
            key_pressed = pygame.key.get_pressed()
             # set up di chuyen sang trai
            if key_pressed[pygame.K_LEFT] and base.game_over == "false":
                base.x_loc -= SETTING_BASE_SPEED
                if base.x_loc < 0:      # Không di chuyến quá phạm vi màn hình
                    base.x_loc = 0
            # set up di chuyen sang phai
            if key_pressed[pygame.K_RIGHT]and base.game_over == "false":
                base.x_loc += SETTING_BASE_SPEED
                if base.x_loc > SCREEN_WIDTH - Base_modul.base_width:
                    base.x_loc = SCREEN_WIDTH - Base_modul.base_width

            if key_pressed[pygame.K_DOWN]and base.game_over == "false":
                base.y_loc += SETTING_BASE_SPEED
                if base.y_loc > SCREEN_HEIGHT - Base_modul.base_height:
                    base.y_loc = SCREEN_HEIGHT - Base_modul.base_height

            if key_pressed[pygame.K_UP]and base.game_over == "false":
                base.y_loc -= SETTING_BASE_SPEED
                if base.y_loc < 0:
                    base.y_loc = 0
            # set up nut space
            if key_pressed[pygame.K_SPACE]  and base_missile.missile_firing  is False  and base.game_over == "false":
                base_missile.missile_firing = True
                base_missile.x_loc = base.x_loc + 10
                base_missile.y_loc = base.y_loc - Base_modul.base_missile_height
                spaceship_hit_sound.play()
            # # set up nut R
            if key_pressed[pygame.K_r] and base.rocket > 0 and rocket.hit == False and base.game_over == "false":
                rocket.hit = True
                base.rocket -= 1
                rocket.x_loc = base.x_loc - 40
                boom_sound.play()
        
        pygame.display.update()
        clock.tick(120)

    return

NUM_OF_CHICKEN = read_setting_imformation()
main()
