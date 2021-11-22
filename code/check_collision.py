import pygame
import Base_modul
import Chicken_modul
import random
import sys
import rocket_modul
import boss_modul
pygame.init()
#======================================================================================
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
launch_sound = pygame.mixer.Sound('music/launch.ogg')
#======================================================================================
def check_base_missile_and_chicken(chicken,base_missile,base):
    # score_if_hit = 0
    if chicken.hit is False and base_missile.missile_firing == True:
        chicken_rect = pygame.Rect(chicken.x_loc, chicken.y_loc, Chicken_modul.chicken_width, Chicken_modul.chicken_height)
        base_missile_rect = pygame.Rect(base_missile.x_loc, base_missile.y_loc, Base_modul.base_width, Base_modul.base_height)
        if base_missile_rect.colliderect(chicken_rect): # nếu băn trúng
            base_missile.missile_firing = False
            if chicken.ray_time <= 0:
                chicken.hit = True
                chicken.hit_time = 100 #UFO_HIT_TIME
                chicken.off_time = 200
                launch_sound.play() # gọi file âm thanh
                base.score += 10
                              
#=======================================================================================
def update_chicken_hit(chicken):
    if chicken.hit_time > 0:
        chicken.hit_time -= 1    #giam dan thoi gian
        # trong thoi gian nay neu off time bằng 0 thi set up thoi gian hoi sinh
        if chicken.hit_time == 0:
            chicken.off_time = random.randint(200,1000)
    # đếm ngước time hồi sinh
    elif chicken.off_time > 0 and chicken.hit == True:
        chicken.off_time -= 1   #giam dan thoi gian
        #khi time hoi sinh da het
        if chicken.off_time == 0:
            chicken.hit = False
            if random.randint(1, 2) == 1: chicken.x_loc = 0
            else: chicken.x_loc = SCREEN_WIDTH - Chicken_modul.chicken_width
            chicken.y_loc = random.randint(Chicken_modul.CHICKEN_UPPER_Y, Chicken_modul.CHICKEN_LOWER_Y)

#====================================================================
def check_base_and_chicken_missile(base,chicken_missile): 
    base_rect = pygame.Rect(base.x_loc, base.y_loc, Base_modul.base_width,Base_modul.base_height)
    chicken_missile_rect = pygame.Rect(chicken_missile.x_loc, chicken_missile.y_loc, Chicken_modul.chicken_missile_width, Chicken_modul.chicken_missile_height)
    # check từng viện đan của ufo với xe
    if base_rect.colliderect(chicken_missile_rect) == True:
        base.hp -= 5   # giảm máu
        base.time_boom = 40
        chicken_missile.y_loc = SCREEN_HEIGHT   # xóa đạn ufo

#=========================================================
def check_base_and_chicken_thighs(base,chicken_thighs): 
    base_rect = pygame.Rect(base.x_loc, base.y_loc, Base_modul.base_width,Base_modul.base_height)
    chicken_thighs_rect = pygame.Rect(chicken_thighs.x_loc, chicken_thighs.y_loc, Chicken_modul.chicken_thighs_width, Chicken_modul.chicken_thighs_height)
    # check từng viện đan của ufo với xe
    if base_rect.colliderect(chicken_thighs_rect) == True:
        base.num_chicken_thighs += 1   # giảm máu
        chicken_thighs.y_loc = SCREEN_HEIGHT   # xóa đạn ufo
#========================================================
def check_roket_and_chicken(chicken,rocket,base):
    # score_if_hit = 0
    if rocket.boom_time >0 and chicken.hit is False :
        chicken_rect = pygame.Rect(chicken.x_loc, chicken.y_loc, Chicken_modul.chicken_width, Chicken_modul.chicken_height)
        rocket_rect = pygame.Rect(rocket.x_loc - rocket_modul.rocket_width / 2.5, 30, rocket_modul.rocket_width, rocket_modul.rocket_height )
        
        if rocket_rect.colliderect(chicken_rect): # nếu băn trúng
                chicken.hit = True
                chicken.hit_time = 100 #UFO_HIT_TIME
                chicken.off_time = 200
                base.score += 10

#============================================================
def check_base_missile_and_boss(boss,base_missile,base):
     if base_missile.missile_firing == True and boss.hit == False:
        base_missile_rect = pygame.Rect(base_missile.x_loc, base_missile.y_loc,Base_modul.base_missile_width,Base_modul.base_missile_height)
        boss_rect = pygame.Rect(boss.x_loc, boss.y_loc, boss_modul.boss_width, boss_modul.boss_height)
        if base_missile_rect.colliderect(boss_rect): # nếu băn trúng
            base_missile.missile_firing = False
            if boss.time_defense <= 0:
                boss.hp -= base_missile.sub_hp_boss
                base.score += 10

#====================================================================
def check_base_and_boss_missile(base,boss_missile): 
    base_rect = pygame.Rect(base.x_loc, base.y_loc, Base_modul.base_width,Base_modul.base_height)
    boss_missile_rect = pygame.Rect(boss_missile.x_loc,boss_missile.y_loc, boss_modul.boss_missile_width,boss_modul.boss_missile_height)
    boss_missile_rect1 = pygame.Rect(boss_missile.x_loc+150,boss_missile.y_loc, boss_modul.boss_missile_width,boss_modul.boss_missile_height)
    boss_missile_rect2 = pygame.Rect(boss_missile.x_loc-150,boss_missile.y_loc, boss_modul.boss_missile_width,boss_modul.boss_missile_height)
    # check từng viện đan của ufo với xe

    if base_rect.colliderect(boss_missile_rect) or base_rect.colliderect(boss_missile_rect1) or base_rect.colliderect(boss_missile_rect2):
        base.hp -= 0.5   # giảm máu
        base.time_boom = 10

#========================================================
def check_roket_and_boss(boss,rocket,base):
    if rocket.boom_time >0 and boss.hit is False :
        chicken_rect = pygame.Rect(boss.x_loc, boss.y_loc, Chicken_modul.chicken_width, Chicken_modul.chicken_height)
        rocket_rect = pygame.Rect(rocket.x_loc - rocket_modul.rocket_width / 2.5, 30, rocket_modul.rocket_width, rocket_modul.rocket_height )
        if rocket_rect.colliderect(chicken_rect): # nếu băn trúng
            boss.hp -= 0.3
            base.score += 1
            
#==============================================================
def check_base_and_boss(base,boss): 
    base_rect = pygame.Rect(base.x_loc, base.y_loc, Base_modul.base_width,Base_modul.base_height)
    boss_rect = pygame.Rect(boss.x_loc,boss.y_loc, boss_modul.boss_width,boss_modul.boss_height)
    # check boss với xe
    if base_rect.colliderect(boss_rect) :
        base.hp -= 0.3   # giảm máu
        base.time_boom = 10