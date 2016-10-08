import GameWindow
import MainMenu
import sys
from pygame import *
from gamePad import *



jadeBox = [0,74,216,387]
captainBox = [216,99,212,354]
koopaBox = [425,118,250,337]
zeroBox = [670,94,317,390]

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

     
class playerRect:
    def __init__(self,val,player1):
        self.myfont = pygame.font.SysFont("Terminal", 29)
        self.val = val
        self.player1 = player1
        if player1 == True:
            self.char = "jade"
            self.color = (255,0,0)
        else:
            self.char="zero"
            self.color = (0,0,255)
        self.x = val[0]
        self.y = val[1]
        self.w = val[2]
        self.h = val[3]
        self.yLabel = val[1]
    def setVal(self,val,char):
        self.val = val
        self.x = val[0]
        self.y = val[1]
        self.w = val[2]
        self.h = val[3]
        self.yLabel = val[1]
        self.char = char
    def draw(self):
        pygame.draw.rect(GameWindow.screen,self.color,\
                         (self.x,self.y,self.w,self.h),8)
    def drawLabel(self):
        if self.player1==True:
            pygame.draw.rect(GameWindow.screen,(255,0,0),\
                (self.x,self.y,100,25),0)
            label = self.myfont.render("Player1", 1, (255, 225, 225))
            GameWindow.screen.blit(label, (self.x+6, self.y+6))
            
        else:
            pygame.draw.rect(GameWindow.screen,(0,0,225),\
                (self.x+100,self.yLabel,100,25),0)
            label = self.myfont.render("Player2", 1, (255, 225, 225))
            GameWindow.screen.blit(label, (self.x+106, self.yLabel+6))


p1Box = playerRect(jadeBox,True)
p2Box = playerRect(zeroBox,False)

def characterSelect():
    charPause = True
    running=True
    joystick1 = None
    joystick2 = None
    fullScreenBool = False
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick1 = pygame.joystick.Joystick(0)
    if joystick_count > 1:
        joystick2 = pygame.joystick.Joystick(1)
    
    blinkCtr = 0
    while charPause == True:
        
        surface = pygame.image.load("characterMenu.png")
        GameWindow.screen.blit(surface,(0,0))
        #pygame.draw.rect(GameWindow.screen,(255,0,0),(x,y,w,h),8)
        p1Box.drawLabel()
        p2Box.drawLabel()
        p1Box.draw()
        p2Box.draw()
        
        
        if p1Box.val == p2Box.val:
            if blinkCtr >= 0 and blinkCtr < 25:
                p2Box.y = p2Box.y + 600
            else:
                p2Box.y = p2Box.val[1]
        else:
            p2Box.y = p2Box.val[1] 
        
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()
            
            if joystick_count > 0 and joystick1.get_button(0) == 1:
                charPause = False
                
            if joystick_count > 1 and joystick2.get_button(0) == 1:
                charPause = False
                
            if keys[pygame.K_RETURN]:
                charPause = False

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
                
            if keys[pygame.K_a] or joyLeft(joystick1):
                if p1Box.x == zeroBox[0]:
                    p1Box.setVal(koopaBox,"koopa")
                elif  p1Box.x == koopaBox[0]:
                    p1Box.setVal(captainBox,"captain")
                elif p1Box.x == captainBox[0]:
                    p1Box.setVal(jadeBox,"jade")
                else:
                    p1Box.setVal(zeroBox,"zero") 
                    
            if keys[pygame.K_d] or joyRight(joystick1):
                if p1Box.x == jadeBox[0]:
                    p1Box.setVal(captainBox,"captain")
                elif  p1Box.x == captainBox[0]:
                    p1Box.setVal(koopaBox,"koopa")
                elif p1Box.x == koopaBox[0]:
                    p1Box.setVal(zeroBox,"zero")
                else:
                    p1Box.setVal(jadeBox,"jade")

            if keys[pygame.K_RIGHT] or joyRight(joystick2):
                if p2Box.x == jadeBox[0]:
                    p2Box.setVal(captainBox,"captain")
                elif  p2Box.x == captainBox[0]:
                    p2Box.setVal(koopaBox,"koopa")
                elif p2Box.x == koopaBox[0]:
                    p2Box.setVal(zeroBox,"zero")
                else:
                    p2Box.setVal(jadeBox,"jade")

            if keys[pygame.K_LEFT] or joyLeft(joystick2):
                if p2Box.x == zeroBox[0]:
                    p2Box.setVal(koopaBox,"koopa")
                elif  p2Box.x == koopaBox[0]:
                    p2Box.setVal(captainBox,"captain")
                elif p2Box.x == captainBox[0]:
                    p2Box.setVal(jadeBox,"jade")
                else:
                    p2Box.setVal(zeroBox,"zero")

        if blinkCtr < 50:
            blinkCtr+=1
        else:
            blinkCtr = 0
        pygame.display.flip()

    return running,p1Box.char,p2Box.char
