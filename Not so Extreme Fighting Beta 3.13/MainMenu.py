#===============================================================================
#   Main Loop For Main Menu
#===============================================================================

import GameWindow
import MainMenu
import sys
from pygame import *
from gamePad import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

##Narrative: Creates the main menu
##Preconditions: New_Zero_Fighting module calls mainMenu()
##Post conditions: Creates the screen with all drawn objects and images
def mainMenu():
    pygame.init()
    pygame.draw.rect(GameWindow.screen,(0,0,0),(20,20,20,20),0)
    running=True
    menuPause = True
    menuFlame = 1
    flameCtr = 0
    blinkCtr = 0
    x=420
    y=350
    w=200
    h=30
    fullScreenBool = False

    #initializes game pad for main menu
    joystick1 = None
    joystick2 = None
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick1 = pygame.joystick.Joystick(0)
    if joystick_count > 1:
        joystick2 = pygame.joystick.Joystick(1)

    mixer.music.load("MainThemeMusic.ogg")
    mixer.music.play()
    while menuPause == True:
        gamePad(joystick1, joystick2)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            #Continues through the main menu so long as 'enter' on a keyboard
            #is pressed or if start button pn game pad is pressed
            if joystick_count > 0 and joystick1.get_button(7) == 1:
                menuPause = False

            if joystick_count > 1 and joystick2.get_button(7) == 1:
                menuPause = False

            if keys[pygame.K_RETURN]:
                menuPause = False

            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                sys.exit()
                quit()

            if keys[pygame.K_t] and fullScreenBool == True:
                screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                fullScreenBool = False

            elif keys[pygame.K_t] and fullScreenBool == False:
                screen = display.set_mode(\
                    (SCREEN_WIDTH,SCREEN_HEIGHT),FULLSCREEN)
                fullScreenBool = True

            if joystick_count > 0:  
                if joystick1.get_button(6) == 1 and joystick1.get_button(7)\
                 == 1:
                        quit()
                        sys.exit()

                if joystick1.get_button(6) == 1 and fullScreenBool == True:
                    GameWindow.screen = pygame.display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False

                if joystick1.get_button(6) == 1 and fullScreenBool == False:
                    GameWindow.screen = pygame.display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)
                    fullScreenBool = True

            if joystick_count > 1:
                if joystick2.get_button(6) == 1 and joystick2.get_button(7)\
                     == 1:
                            quit()
                            sys.exit()

                if joystick2.get_button(6) == 1 and fullScreenBool == True:
                    GameWindow.screen = pygame.display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False

                if joystick2.get_button(6) == 1 and fullScreenBool == False:
                    GameWindow.screen = pygame.display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)
                    fullScreenBool = True
                
        pygame.display.flip()
        if menuFlame ==1:
            surface = pygame.image.load("Menu1.JPG")
            GameWindow.screen.blit(surface,(0,0))
        elif menuFlame == 2:
            surface = pygame.image.load("Menu2.JPG")
            GameWindow.screen.blit(surface,(0,0))
        elif menuFlame == 3:
            surface = pygame.image.load("Menu3.JPG")
            GameWindow.screen.blit(surface,(0,0))
        elif menuFlame == 4:
            surface = pygame.image.load("Menu4.JPG")
            GameWindow.screen.blit(surface,(0,0))   
        else:
            menuFlame = 0
        if flameCtr % 4 ==0:
            menuFlame+=1
        flameCtr+=1

        if blinkCtr >= 0 and blinkCtr < 25:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x,y,w,h),0)
        elif blinkCtr >= 25 and blinkCtr < 50:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+21,y,195,30),0)
        elif blinkCtr >= 50 and blinkCtr < 75:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+36,y,185,30),0)
        elif blinkCtr >= 75 and blinkCtr < 100:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+50,y,175,30),0)
        elif blinkCtr >= 100 and blinkCtr < 125:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+65,y,165,30),0)
        elif blinkCtr >= 125 and blinkCtr < 150:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+85,y,155,30),0)
        elif blinkCtr >= 150 and blinkCtr < 175:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+116,y,145,30),0)
        elif blinkCtr >= 175 and blinkCtr < 200:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+131,y,135,30),0)
        elif blinkCtr >= 200 and blinkCtr < 225:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+143,y,125,30),0)
        elif blinkCtr >= 225 and blinkCtr < 250:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+164,y,170,30),0)
        elif blinkCtr >= 250 and blinkCtr < 275:
             pygame.draw.rect(GameWindow.screen,(0,0,0),(x+185,y,1,30),0)
        elif blinkCtr >= 275 and blinkCtr < 300:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x,y,w,h),0)
        elif blinkCtr >= 300 and blinkCtr < 325:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x+185,y,w,h),0)
        elif blinkCtr >= 325 and blinkCtr < 350:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x,y,w,h),0)
        elif blinkCtr >= 350 and blinkCtr < 375:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x+185,y,w,h),0)
        elif blinkCtr >= 375 and blinkCtr < 400:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x,y,w,h),0)
        elif blinkCtr >= 400 and blinkCtr < 425:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x+185,y,w,h),0)
        elif blinkCtr >= 425 and blinkCtr < 450:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x,y,w,h),0)
        elif blinkCtr >= 450 and blinkCtr < 475:
            pygame.draw.rect(GameWindow.screen,(0,0,0),(x+185,y,w,h),0)
        else:
            blinkCtr=0
        blinkCtr+=1
    return running

##Narrative: Stage Selection screen is made; keyboard and joystick
## input is allowed
##Preconditions: Main menu window must be made 
##Post conditions: User selects their desired stage
def stageMenu():
    running = True
    stagePause = True
    x=378
    y=250
    fullScreenBool = False

    #initializes game pad for stage select
    joystick1 = None
    joystick2 = None
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick1 = pygame.joystick.Joystick(0)
    if joystick_count > 1:
        joystick2 = pygame.joystick.Joystick(1)

    mixer.music.load("StageSelectMusic.mp3")
    mixer.music.play()

    while stagePause == True:
        gamePad(joystick1, joystick2)
        surface = pygame.image.load("StageSelect.JPG")
        GameWindow.screen.blit(surface,(0,0))
        pygame.draw.rect(GameWindow.screen,(255,204,0),(x,y,250,150),5)
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()

            if joystick_count > 0 and joystick1.get_button(0) == 1:
                stagePause = False
                
            if joystick_count > 1 and joystick2.get_button(0) == 1:
                stagePause = False
                
            if keys[pygame.K_RETURN]:
                stagePause = False

            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                sys.exit()
                quit()

            if keys[pygame.K_t] and fullScreenBool == True:
                screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                fullScreenBool = False

            elif keys[pygame.K_t] and fullScreenBool == False:
                screen = display.set_mode(\
                    (SCREEN_WIDTH,SCREEN_HEIGHT),FULLSCREEN)
                fullScreenBool = True

            if joystick_count > 0:  
                if joystick1.get_button(6) == 1 and \
                joystick1.get_button(7) == 1:
                        quit()
                        sys.exit()

                if joystick1.get_button(6) == 1 and fullScreenBool == True:
                    GameWindow.screen = pygame.display.set_mode((\
                        SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False

                if joystick1.get_button(6) == 1 and fullScreenBool == False:
                    GameWindow.screen = pygame.display.set_mode((\
                        SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)
                    fullScreenBool = True

            if joystick_count > 1:
                if joystick2.get_button(6) == 1 and \
                joystick2.get_button(7) == 1:
                        quit()
                        sys.exit()

                if joystick2.get_button(6) == 1 and fullScreenBool == True:
                    GameWindow.screen = pygame.display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False

                if joystick2.get_button(6) == 1 and fullScreenBool == False:
                    GameWindow.screen = pygame.display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)
                    fullScreenBool = True
 
            if keys[pygame.K_w] or joyUp(joystick1) or joyUp(joystick2):
                if y == 250:
                    y=95
                elif y == 95:
                    y=405
                else:
                    y=250

            if keys[pygame.K_s] or joyDown(joystick1) or joyDown(joystick2):
                if y == 250:
                    y=405
                elif y == 95:
                    y=250
                else:
                    y=95

            if keys[pygame.K_a] or joyLeft(joystick1) or joyLeft(joystick2):
                if x == 105:
                    x = 652
                elif x == 652:
                    x=378
                else:
                    x = 105

            if keys[pygame.K_d] or joyRight(joystick1) or joyRight(joystick2):
                if x == 105:
                    x = 378
                elif x == 378:
                    x=652
                else:
                    x = 105
        pygame.display.flip()
        
        
    return running,x,y
