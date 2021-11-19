import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

defense_image =  pygame.image.load('image/ray.png').convert_alpha()
defense_image = pygame.transform.scale(defense_image, (SCREEN_WIDTH/6, SCREEN_HEIGHT/6))
boss_image = pygame.transform.scale(pygame.image.load('image/ga_boss.png'), (SCREEN_WIDTH/3, SCREEN_HEIGHT/3))
boss_died_image = pygame.transform.scale(pygame.image.load('image/vu_no_3.png'), (SCREEN_WIDTH/3, SCREEN_HEIGHT/3))
boss_defense_image = pygame.transform.scale(defense_image, (SCREEN_WIDTH/1.5, SCREEN_HEIGHT/1.5 )) 
boss_width = boss_image.get_rect().width
boss_height = boss_image.get_rect().height
boss_missile_image = pygame.transform.scale(pygame.image.load('image/trung_ga.png'), (SCREEN_WIDTH / 15, SCREEN_HEIGHT/9))
danger_image = pygame.image.load('image/danger_boss.png').convert_alpha()
boss_missile_width = boss_missile_image.get_rect().width
boss_missile_height = boss_missile_image.get_rect().height

class Boss:
    x_loc = 250
    y_loc = -500
    speed = 1.5
    hit = False
    direction = 'left'
    hp = 100.00
    time_appear = True
    time_died = 0
    time_defense = 500
    hit_time = 0
    off_time = random.randint(100,200)
    ray_time = 0
    statu = 'disappear'

    def check_boss_appear(self,base,chicken_list,num):
        if base.score >= num *  40:
            for i in chicken_list:
                i.hit = True 
            if self.hp > 0: self.statu = 'appear'   
            

    def draw_boss(self):
        if self.time_died > 0:
            self.time_died  -= 1 
            game_screen.blit(boss_died_image ,[self.x_loc,self.y_loc])
        else:
            if self.hit == False:
                game_screen.blit(boss_image,[self.x_loc,self.y_loc])

    def move(self):
        if self.time_appear == True:
            game_screen.blit(danger_image, [300,200]) # in ra thông bao sắp hết khiên
            if self.y_loc <= 50:
                self.y_loc += 1
            else: 
                self.time_appear = False  
        else : 
            if  self.hit is False:    
                if self.direction == 'left':
                    self.x_loc -= self.speed
                elif self.direction == 'right':
                    self.x_loc += self.speed
                elif self.direction == 'up':
                    self.y_loc -= self.speed
                elif self.direction == 'down':
                    self.y_loc += self.speed

            # If the UFO goes off the screen left, reset x coordinate and change direction
                if self.x_loc < 0:
                    self.x_loc = 0
                    self.direction = 'right'

            # If the UFO goes off the screen right, reset x coordinate and change direction
                elif self.x_loc > SCREEN_WIDTH - boss_width:
                    self.x_loc = SCREEN_WIDTH - boss_width
                    self.direction = 'left'

                # If the UFO goes too high, reset y coordinate and change direction
                elif self.y_loc < 20:
                    self.y_loc = 20
                    self.direction = 'down'

                # If the UFO goes too low, reset y coordinate and change direction
                elif self.y_loc > 240:
                    self.y_loc = 240
                    self.direction = 'up'

            # If none of the above, then random chance of changing direction
                else:
                    if self.direction == 'up' or self.direction == 'down':
                        ufo_direction_chance = random.randint(0, 20)
                    else:
                        ufo_direction_chance = random.randint(0, 80)
                    
                    if ufo_direction_chance == 1:
                        self.direction= random.choice(['left', 'right', 'up', 'down','left', 'right', 'up'])

    def boss_defense(self):
        if round(self.hp) == 10 or round(self.hp) == 50 or round(self.hp) == 70:
            self.time_defense = 400
            self.hp -= 1
        if self.time_defense > 0:
            game_screen.blit(boss_defense_image, [self.x_loc -160, self.y_loc -100 ])
        if self.time_defense == 0 and self.hit is False:
            if random.randint(0, 2000) == 1:
                self.time_defense = random.randint(200, 400)
        # nêu ray đã có thì --1
        elif self.time_defense > 0:
            self.time_defense -= 1

class Boss_missile:
    fired = False
    firing =  False
    x_loc = 0
    y_loc = 0
    speed = 2

    def draw_boss_missile(self) :
        if self.firing:
            game_screen.blit(boss_missile_image, [ self.x_loc , self.y_loc])
            game_screen.blit(boss_missile_image, [ self.x_loc + 150 , self.y_loc])
            game_screen.blit(boss_missile_image, [ self.x_loc - 150 , self.y_loc])
            

    def boss_hit(self,boss):
        if boss.hit == False:  # chi ufo con song moi dc nha dan
            if self.fired  == False and random.randint(1,200) == 1:
                self.fired = True
            # nếu nhả đạn
        if self.fired == True and  self.firing == False:
            self.x_loc = boss.x_loc + boss_width / 2.5
            self.y_loc = boss.y_loc + boss_height
            self.firing = True


    def move(self):
        if self.firing:
            self.y_loc += self.speed
            if self.y_loc > SCREEN_HEIGHT:
                self.fired = False
                self.firing = False

    
    
    