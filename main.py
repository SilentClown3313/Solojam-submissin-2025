#importing stuff
import pygame
import random
from sys import exit

#importing images
#start_img = pygame.image.load("C:\Solojam-submissin-2025\IMG\Start_button.png")

#Buttons
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y

    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))

#Set-UP
pygame.init()
Clock = pygame.time.Clock()

#Dsplay window
scrn_width = 1200
scrn_height = 600
screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("Pong practice")

#Game state variables:
game_paused = False

#Game Colours
BG_Colour = (90,90,90)
White = (255,255,255)

#Text:
game_font = pygame.font.SysFont("arialblack.ttf",40)
text_surf_1 = game_font.render("Press SPACE to PAUSE", True, White)

#RECTS


# Config


while True:

    screen.fill(BG_Colour)

    # chek game state:
    if game_paused == False:
        pass
    else:
        screen.fill(White)
        pygame.display.set_caption("Pause Menu")

    #Exitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = not game_paused

    #Drawing stuff on the screen


    #updating the game
    pygame.display.flip()
    Clock.tick(60)