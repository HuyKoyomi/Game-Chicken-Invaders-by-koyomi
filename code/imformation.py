import pygame
import os
import sys
import button

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 614
background_image = pygame.image.load('image/bg.jpg').convert()
game_screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game by Koyomi')
back_image = pygame.image.load('image/back.png')
back_image = pygame.transform.scale(back_image, (SCREEN_WIDTH/10, SCREEN_HEIGHT/10))
imformtion_image = pygame.image.load('image/imformation.PNG')
imformtion_image = pygame.transform.scale(imformtion_image, (SCREEN_WIDTH/1.5, SCREEN_HEIGHT/1.5))

run=True
back_button = button.Button(30,30,back_image)
while run:
    
    game_screen.blit(background_image, [0, 0])
    game_screen.blit(imformtion_image, [150, 100])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
       
    if back_button.draw()==True:
        pygame.quit()
        os.system('py menu_main.py')
        sys.exit()

    pygame.display.update()
pygame.quit()
