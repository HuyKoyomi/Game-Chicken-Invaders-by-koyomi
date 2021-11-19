import pygame
import os
import sys
import button
pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614

game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game by Koyomi')
background_image = pygame.image.load('image/bg.jpg').convert()
logo_image = pygame.transform.scale(pygame.image.load('image/logo.png'), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
play_image = pygame.transform.scale(pygame.image.load('image/play.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
quit_image = pygame.transform.scale(pygame.image.load('image/quit.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
setting_image = pygame.transform.scale(pygame.image.load('image/setting.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
contact_image = pygame.transform.scale(pygame.image.load('image/contact.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
option_image = pygame.transform.scale(pygame.image.load('image/option.png'), (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))

music_image =  pygame.transform.scale(pygame.image.load('image/music_button.png'), (SCREEN_WIDTH/12, SCREEN_HEIGHT/12))
naruto_sound = pygame.mixer.Sound('music/naruto.mp3')
music_one_time = True   # chạy nhạc 1 lần

play_button=button.Button(400, 350, play_image)
setting_button=button.Button(400, 400, setting_image)
option_button=button.Button(400, 450, option_image)
contact_button=button.Button(400, 500, contact_image)
quit_button=button.Button(400, 550, quit_image)

run=True
while run:

    if music_one_time:
        naruto_sound.play()
        music_one_time = False
             
    game_screen.blit(background_image, [0, 0])
    game_screen.blit(logo_image, [250,50])
    game_screen.blit(music_image, [850,550])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    if quit_button.draw()==True:
        pygame.quit()
        sys.exit() 

    if contact_button.draw()==True:
        pygame.quit()
        os.system('py imformation.py')
        sys.exit() 

    if option_button.draw() == True:
        pygame.quit()
        os.system('py imformation.py')
        sys.exit() 
    
    if setting_button.draw() == True:
        pygame.quit()
        os.system('py setting_main.py')
        sys.exit() 

    if play_button.draw()==True: 
        pygame.quit()
        os.system('python game_main.py')
        os.system('py menu_main.py')
        sys.exit()

    pygame.display.update()

pygame.quit()