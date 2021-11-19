import pygame
import os
import sys
import button
from display_on_screen import display_setting

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

pygame.display.set_caption('Game by Koyomi')
background_image = pygame.image.load('image/bg.jpg').convert()
game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

back_image = pygame.transform.scale(pygame.image.load('image/back.png'), (SCREEN_WIDTH/10, SCREEN_HEIGHT/10))

b1_image = pygame.transform.scale(pygame.image.load('image/button1.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/10))
b2_image = pygame.transform.scale(pygame.image.load('image/button2.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/10))
b3_image = pygame.transform.scale(pygame.image.load('image/button3.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/10))
sound = pygame.mixer.Sound('music/Asphyxia.mp3')
music_one_time = True   # chạy nhạc 1 lần

run=True
back_button = button.Button(30,30,back_image)
b1 = button.Button(70,300,b1_image)
b2 = button.Button(370,300,b2_image)
b3 = button.Button(670,300,b3_image)
#============================================================================================
def level1():
    with open("setting_imformation",'w') as file:     # doc file
        file.write('10')
def level2():
    with open("setting_imformation",'w') as file:     # doc file
        file.write('20')
def level3():
    with open("setting_imformation",'w') as file:     # doc file
        file.write('30')


#=========================================================================
while run:
    
    if music_one_time:
        sound.play()
        music_one_time = False
    game_screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    if b1.draw()==True:
        pygame.quit()
        level1()
        os.system('py menu_main.py')
        sys.exit()
    
    if b2.draw()==True:
        pygame.quit()
        level2()
        os.system('py menu_main.py')
        sys.exit()

    if b3.draw()==True:
        pygame.quit()
        level3()
        os.system('py menu_main.py')
        sys.exit()

    if back_button.draw()==True:
        pygame.quit()
        os.system('py menu_main.py')
        sys.exit()
    
    display_setting()

    pygame.display.update()
pygame.quit()
