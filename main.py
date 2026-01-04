#importing stuff
import pygame
import random
from sys import exit

#importing images

#Buttons
class Button():
    def __init__(self,x,y,scale,image):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),(int(height*scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
        self.get_clicked = False

    def draw(self):
        action = False
        #mouse pos
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] ==1 and self.get_clicked == False:
                self.get_clicked = True
                if self.get_clicked == True:
                    action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.get_clicked = False

        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action

#Set-UP
pygame.init()
Clock = pygame.time.Clock()

#Dsplay window
scrn_width = 600
scrn_height = 400
screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("Jailscape")

#Game Colours
BG_Colour = (90,90,90)
White = (255,255,255)

#Text:
game_font = pygame.font.SysFont("arialblack.ttf",40)
text_surf_1 = game_font.render("TEXT", True, White)

#Rects

# Config

while True:

    screen.fill(BG_Colour)

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