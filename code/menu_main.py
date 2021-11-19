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
logo_image = pygame.image.load('image/logo.png')
logo_image = pygame.transform.scale(logo_image, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
play_image=pygame.image.load('image/play.png')
play_image = pygame.transform.scale(play_image, (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
quit_image = pygame.image.load('image/quit.png')
quit_image = pygame.transform.scale(quit_image, (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
setting_image = pygame.image.load('image/setting.png')
setting_image = pygame.transform.scale(setting_image, (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
contact_image = pygame.image.load('image/contact.png')
contact_image = pygame.transform.scale(contact_image, (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))
option_image = pygame.image.load('image/option.png')
option_image = pygame.transform.scale(option_image, (SCREEN_WIDTH/5, SCREEN_HEIGHT/15))


play_button=button.Button(400, 350, play_image)
option_button=button.Button(400, 400, option_image)
setting_button=button.Button(400, 450, setting_image)
contact_button=button.Button(400, 500, contact_image)
quit_button=button.Button(400, 550, quit_image)

run=True
while run:
    # game_screen.fill((202, 228, 241))
    
    game_screen.blit(background_image, [0, 0])
    game_screen.blit(logo_image, [250,50])

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
        os.system('py imformation.py')
        sys.exit() 

    if play_button.draw()==True: 
        pygame.quit()
        os.system('python game_main.py')
        os.system('py menu_main.py')
        sys.exit()

    pygame.display.update()
    
pygame.quit()