import GameWindow
from pygame import *
import time

init()

CONVERT_POWER = 2.9833

class Stopwatch:

    def __init__(self):
        self.startTime = time.time()

    def reset(self):
        self.startTime = time.time()

    def getTime(self):
        return(int(format(time.time() - self.startTime,'.0f')))

class Timer:
    def __init__(self):
        self.countDown = 99
        self.countDown = None
        self.stopWatch = Stopwatch()
        self.myfont = font.SysFont("Helvetica", 50)

    def drawTimer(self):
        
        self.countDown = 99 - self.stopWatch.getTime()
        if self.countDown <= 0:
            self.countDown = 0
            
        draw.circle(GameWindow.screen, (225,225,225), (500,16), 44,0)
        draw.circle(GameWindow.screen, (0,0,0), (500,16), 40,0)
        label = self.myfont.render(str(self.countDown), 1, (255, 204, 0))
        if self.countDown >= 10:
            GameWindow.screen.blit(label, (471, 2))
        else:
            GameWindow.screen.blit(label, (487, 2))

class HealthBar:
    def __init__(self):
        self.countDown = 99
        self.p1H = 450
        self.p2H = 450
        self.p1Coord = 12
        self.p2Coord = 538
        self.myfont = font.SysFont("Small Fonts", 55)

    ##Narrative: Draws the health bars and sets the fight timer to 99 ticks
    ##Preconditions: Initalize the countdown attribute
    ##Post conditions:Health bars and timer are drawn onto the top of the screen
    def drawHealth(self):

        #Player 1 HealthBar
        draw.rect(GameWindow.screen,(225,225,225),(9,5,455,25),0)
        draw.rect(GameWindow.screen,(225,0,0),(12,7,450,20),0)
        draw.rect(GameWindow.screen,(0,255,0),(self.p1Coord,7,self.p1H,20),0)
        draw.rect(GameWindow.screen,(225,225,225),(0,5,9,25),0)
        draw.polygon(GameWindow.screen,(225,225,225),[(9,5),(49,5),(9,30)])
    
        #Player 2 HealthBar
        draw.rect(GameWindow.screen,(225,225,225),(535,5,455,25),0)
        draw.rect(GameWindow.screen,(225,0,0),(538,7,450,20),0)
        draw.rect(GameWindow.screen,(0,255,0),(self.p2Coord,7,self.p2H+20,20),0)
        draw.rect(GameWindow.screen,(225,225,225),(535+455,5,10,25),0)
        draw.polygon(GameWindow.screen,(225,225,225),[(535+455-40,5),(535+455,5),(535+455,30)])

        #Timer
        draw.circle(GameWindow.screen, (0,0,0), (500,16), 40,0)
        label = self.myfont.render(str(self.countDown), 1, (255, 204, 0))
        GameWindow.screen.blit(label, (479, 4))

    ##Narrative: Player 1 Health Bar
    ##Preconditions: Health Bar drawn onto the screen
    ##Post conditions: Damage is deducted from the health bar
    def player1Dam(self,dam):
        self.p1Bar = self.p1H - dam
        self.p1H -= dam
        self.p1Coord = self.p1Coord - dam

    ##Narrative: Player 2 Health Bar
    ##Preconditions: Health Bar drawn onto the screen
    ##Post conditions: Damage is deducted from the health bar
    def player2Dam(self,dam):
        self.p2Bar = self.p2H - dam
        self.p2H -= dam
        self.p2Coord = self.p2Coord + dam

class PowerBar:
    ##Narrative: Draws the power bars
    ##Preconditions: Main game window must be intialized
    ##Post conditions: Power bars are drawn and updated on screen
    def drawPowerBar(self,player1Power=100,player2Power=100):
        self.player1Power = player1Power
        self.player2Power = player2Power
        
        #Update Player 1 Powerbar Length
        self.p1Width = self.player1Power * CONVERT_POWER

        #Player 1 Powerbar
        draw.rect(GameWindow.screen,(225,225,225),(150,30,455/1.5,25/2),0)
        draw.rect(GameWindow.screen,(122,145,169),(153,31,455/1.5-5,25/2-4),0)
        draw.rect(GameWindow.screen,( 46, 46,254),(153,31,self.p1Width,25/2-4),0)
        draw.polygon(GameWindow.screen,(225,225,225),[(150,30),(175,30),\
                                                      (150,30+25/2)])

        #Update Player 2 Powerbar Length
        self.p2Width = self.player2Power * CONVERT_POWER

        #Player 2 PowerBar
        draw.rect(GameWindow.screen,(225,225,225),(542,30,455/1.5,25/2),0)
        draw.rect(GameWindow.screen,(122,145,169),(545,31,455/1.5-5,25/2-4),0)
        draw.rect(GameWindow.screen,( 46, 46,254),(545+(100*CONVERT_POWER)\
                                                   ,31,-self.p2Width,25/2-4),0)
        draw.polygon(GameWindow.screen,(225,225,225),[(517+455/1.5,30),\
                                                      (542+455/1.5,30),\
                                                      (542+455/1.5,30+25/2)])
            

    
