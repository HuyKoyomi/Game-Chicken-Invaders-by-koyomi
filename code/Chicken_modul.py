import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

vu_no_image = pygame.image.load('image/vu_no.png')
vu_no_image = pygame.transform.scale(vu_no_image, (SCREEN_WIDTH/9, SCREEN_HEIGHT/9))
ga_1_image = pygame.transform.scale(pygame.image.load('image/ga1.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_2_image = pygame.transform.scale(pygame.image.load('image/ga2.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_3_image = pygame.transform.scale(pygame.image.load('image/ga3.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_4_image = pygame.transform.scale(pygame.image.load('image/ga4.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_5_image = pygame.transform.scale(pygame.image.load('image/ga5.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_6_image = pygame.transform.scale(pygame.image.load('image/ga6.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_7_image = pygame.transform.scale(pygame.image.load('image/ga7.png'), (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
ga_exploded_image = pygame.transform.scale(vu_no_image, (SCREEN_WIDTH/10, SCREEN_HEIGHT/10))


chicken_width = ga_1_image.get_rect().width
chicken_height = ga_1_image.get_rect().height 

chicken_left_x = SCREEN_WIDTH - chicken_width
chicken_right_x = 0
chicken_y = 0   

CHICKEN_DIRECTIONS = ['left', 'right', 'up', 'down']
CHICKEN_HIT_TIME  = 25      # thời gian chết trên màn hình
CHICKEN_OFF_TIME_MAX = 200     # thời gian chờ hồi sinh # hoac random
CHICKEN_OFF_TIME_MIN = 100      # thời gian chờ hồi sinh # hoac random
CHICKEN_UPPER_Y = 20        # độ cao max UFO xuất hiện
CHICKEN_LOWER_Y = 240      # đọ cao min UFO xuất hiện

RANDOM_VERTICAL_CHANGE = 20 # tỷ lê nâng ngang (1/x)
RANDOM_HORIZONTAL_CHANGE = 80 # tỷ lê nâng dọc (1/x)
#-------------------------------------------------------------------------------------------
chicken_missile_image = pygame.image.load('image/trung_ga.png')
chicken_missile_image = pygame.transform.scale(chicken_missile_image, (SCREEN_WIDTH/50, SCREEN_HEIGHT/40))

chicken_missile_width = chicken_missile_image.get_rect().width
chicken_missile_height = chicken_missile_image.get_rect().height 
#-------------------------------------------------------------------------------------------
chicken_ray_image_1 = pygame.image.load('image/ufo ray 1.png').convert_alpha()
chicken_ray_image_2 = pygame.image.load('image/ufo ray 2.png').convert_alpha()
ray_width = chicken_ray_image_1.get_rect().width
#--------------------------------------------------------------------
chicken_thighs_image = pygame.image.load('image/dui_ga.png').convert_alpha()
chicken_thighs_image = pygame.transform.scale(chicken_thighs_image, (SCREEN_WIDTH/35, SCREEN_HEIGHT/17))
chicken_thighs_width = chicken_thighs_image.get_rect().width   
chicken_thighs_height = chicken_thighs_image.get_rect().height 
#----------------------------------------------------------------------
class chicken:
    
    x_loc = 0
    y_loc = 0
    direction = 'left'
    speed = 1.5 
    hit = False
    hit_time = 0
    off_time = random.randint(CHICKEN_OFF_TIME_MIN,CHICKEN_OFF_TIME_MAX)
    ray_time = 0
    color = 1

    #----------------------------------------------------------------------------------
    # chọn hình ảnh con gà
    def random_chicken(self):
        self.x_loc = random.choice([chicken_left_x,chicken_right_x])
        self.color = random.randint(1,7)
        self.y_loc = random.randint(CHICKEN_UPPER_Y,CHICKEN_LOWER_Y)
    # vẽ gà
    def draw_chicken(self):

        if self.hit_time > 0 :
            game_screen.blit(ga_exploded_image, [self.x_loc , self.y_loc] )     
        elif self.hit is False:  
            if self.color == 1: game_screen.blit(ga_1_image, [self.x_loc , self.y_loc])
            if self.color == 2: game_screen.blit(ga_2_image, [self.x_loc , self.y_loc])
            if self.color == 3: game_screen.blit(ga_3_image, [self.x_loc , self.y_loc])
            if self.color == 4: game_screen.blit(ga_4_image, [self.x_loc , self.y_loc])
            if self.color == 5: game_screen.blit(ga_5_image, [self.x_loc , self.y_loc])
            if self.color == 6: game_screen.blit(ga_6_image, [self.x_loc , self.y_loc])
            if self.color == 7: game_screen.blit(ga_7_image, [self.x_loc , self.y_loc])
  
    # di chuyển gà
    def move(self):
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
            elif self.x_loc > SCREEN_WIDTH - chicken_width:
                self.x_loc = SCREEN_WIDTH - chicken_width
                self.direction = 'left'

            # If the UFO goes too high, reset y coordinate and change direction
            elif self.y_loc < CHICKEN_UPPER_Y:
                self.y_loc = CHICKEN_UPPER_Y
                self.direction = 'down'

            # If the UFO goes too low, reset y coordinate and change direction
            elif self.y_loc > CHICKEN_LOWER_Y:
                self.y_loc = CHICKEN_LOWER_Y
                self.direction = 'up'

        # If none of the above, then random chance of changing direction
            else:
                if self.direction == 'up' or self.direction == 'down':
                    ufo_direction_chance = random.randint(0, RANDOM_VERTICAL_CHANGE) 
                else:
                    ufo_direction_chance = random.randint(0, RANDOM_HORIZONTAL_CHANGE)
                
                if ufo_direction_chance == 1:
                    self.direction= random.choice(CHICKEN_DIRECTIONS)
        pass

    # ve khien
    def chicken_defense(self):
        if self.ray_time > 0 and self.hit == False:
            if self.ray_time % 4 == 0 or self.ray_time % 5 == 0:
                game_screen.blit(chicken_ray_image_1, [self.x_loc + 25, self.y_loc + chicken_height])
            else:
                game_screen.blit(chicken_ray_image_2, [self.x_loc + 25, self.y_loc + chicken_height])
    # sử dụng khiên
    def use_ray(self):
        # nếu ufo còn sống và ray_time == 0 => radom
        if self.ray_time == 0 and self.hit is False: 
            if random.randint(0, 1000) == 1:
                self.ray_time = random.randint(200, 600)
        # nêu ray đã có thì --1
        elif self.ray_time > 0:
            self.ray_time -= 1

#====================================================================================
class chicken_missile :
    fired = False
    firing =  False
    x_loc = 0
    y_loc = 0
    speed = 2.5

    def draw_chicken_missile(self) :
        if self.firing:
            game_screen.blit(chicken_missile_image, [ self.x_loc , self.y_loc])
            

    def chicken_hit(self,chicken):
        if chicken.hit == False:  # chi ufo con song moi dc nha dan
            if self.fired  == False and random.randint(1,400) == 1:
                self.fired = True
            # nếu nhả đạn
        if self.fired == True and  self.firing == False:
            self.x_loc = chicken.x_loc + 15
            self.y_loc = chicken.y_loc + chicken_height
            self.firing = True

    def move(self):
        if self.firing:
            self.y_loc += self.speed
            if self.y_loc > SCREEN_HEIGHT:
                self.fired = False
                self.firing = False

#=======================================================================
class chicken_thighs:
    fired = False
    firing = False
    x_loc = 0
    y_loc = 0 
    appear_one_time= True
    speed = 1.5

    def random_chicken_thighs(self,chicken):
        if chicken.hit == True and self.appear_one_time:  # chi ufo con song moi dc nha dan
            self.appear_one_time = False  
            if self.fired == False and random.randint(1,2) == 1:
                self.fired = True
        if chicken.hit == False :  self.appear_one_time = True
            # nếu nhả đạn
        if self.fired == True and  self.firing == False:
            self.x_loc = chicken.x_loc
            self.y_loc = chicken.y_loc
            self.firing = True

        if self.firing == True:
            game_screen.blit(chicken_thighs_image, [ self.x_loc, self.y_loc])
            self.move()    # dung chung voi ham

    def move(self):
        self.y_loc += self.speed
        if self.y_loc > SCREEN_HEIGHT:
            self.fired = False
            self.firing = False
    