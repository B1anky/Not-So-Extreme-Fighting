import pygame
import random
pygame.init()

black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode((1000,600))
pygame.display.set_icon(pygame.image.load('Logo.png'))
pygame.display.set_caption("Not So Extreme Fighting")

##Narrative: User chooses between 9 background stages
##Preconditions: User input going through the main menu
##Post conditions: A stage is chosen
def stageSelect(x,y):
    stage=""
    if x==105:
        if y==95:
            stage = "Stage1.jpg"
        elif y== 250:
            stage = "Stage7.jpg"
        else:
            stage = "Stage3.jpg"
    elif x == 378:
        if y== 95:
            stage = "Stage5.jpg"
        elif y == 250:
            stage = "Stage8.jpg"
        else:
            stage = "Stage0.jpg"
    else:
        if y== 95:
            stage = "Stage6.jpg"
        elif y== 250:
            stage = "Stage2.jpg"
        else:
            stage = "Stage9.jpg"
    return stage

##Narrative: Draws chosen stage onto the screen
##Preconditions: User input of stage
##Post conditions: Background is changed, stage is set for the fight     
def drawWindow():
    screen.blit(background,(0,0))
    
