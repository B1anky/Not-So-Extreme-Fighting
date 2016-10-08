from pygame import *
from pygame.locals import *
import MainMenu
import GameWindow
import Health
import sys
from gamePad import *

from Classes import *

import CharMenu
import zeroBuild
import jadeBuild
import koopaBuild
import captainBuild
import blueZeroBuild

#New Zero Fighting!

#Initializes fonts
font.init()

#Screen Resolution

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#Makes Screen
#Remeber fullscreen
screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

keepGoing = True
while keepGoing == True:

    #Defines initial values
    FPS = 60
    pushingPause = False

    #Loads images
    backgroundCheat = image.load("LaughingAnimuGirls.bmp").convert()
    bubble = image.load("bubble.png").convert_alpha()
    bubble = transform.scale(bubble,(74*3,65*3))
    player1WinText = image.load("Player1WinText.png").convert_alpha()
    player2WinText = image.load("Player2WinText.png").convert_alpha()

    #Create Surfaces
    player1Win = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1Win.set_alpha(0)
    player1Win.blit(player1WinText,(200,150))
    player2Win = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    player2Win.set_alpha(0)
    player2Win.blit(player2WinText,(200,150))
    

    #Creates Healthbar and Power Bar
    healthBar = Health.HealthBar()
    powerBar = Health.PowerBar()
    timer = Health.Timer()

    
    #Loads Sprites
        #Zero
    zeroIdleAnimList = zeroBuild.idleAnim()
    zeroWalkAnimList = zeroBuild.walkList()
    zeroStartStopAnimList = zeroBuild.startStopAnim()
    zeroJumpAnimList = zeroBuild.jumpAnim()
    zeroDashAnimList = zeroBuild.dashAnim()
    zeroAttack1List = zeroBuild.attackAnim()
    zeroTallest = zeroBuild.tallest()
    zeroWidest = zeroBuild.widest()
    zeroDefault = zeroBuild.default()
        #BlueZero
    blueZeroIdleAnimList = blueZeroBuild.idleAnim()
    blueZeroWalkAnimList = blueZeroBuild.walkList()
    blueZeroStartStopAnimList = blueZeroBuild.startStopAnim()
    blueZeroJumpAnimList = blueZeroBuild.jumpAnim()
    blueZeroDashAnimList = blueZeroBuild.dashAnim()
    blueZeroAttack1List = blueZeroBuild.attackAnim()
    blueZeroTallest = blueZeroBuild.tallest()
    blueZeroWidest = blueZeroBuild.widest()
    blueZeroDefault = blueZeroBuild.default()
        #Jade
    jadeIdleAnimList = jadeBuild.idleAnim()
    jadeWalkAnimList=jadeBuild.walkList()
    jadeStartStopAnimList = jadeBuild.startStopAnim()
    jadeJumpAnimList = jadeBuild.jumpAnim()
    jadeDashAnimList = jadeBuild.dashAnim()
    jadeAttack1List = jadeBuild.attackAnim()
    jadeTallest = jadeBuild.tallest()
    jadeWidest = jadeBuild.widest()
    jadeDefault = jadeBuild.default()
        #Koopa
    koopaIdleAnimList = koopaBuild.idleAnim()
    koopaWalkAnimList = koopaBuild.walkList()
    koopaStartStopAnimList = koopaBuild.startStopAnim()
    koopaJumpAnimList = koopaBuild.jumpAnim()
    koopaDashAnimList = koopaBuild.dashAnim()
    koopaAttack1List = koopaBuild.attackAnim()
    koopaTallest = koopaBuild.tallest()
    koopaWidest = koopaBuild.widest()
    koopaDefault = koopaBuild.default()
        #Captain
    captainIdleAnimList = captainBuild.idleAnim()
    captainWalkAnimList= captainBuild.walkList()
    captainStartStopAnimList = captainBuild.startStopAnim()
    captainJumpAnimList = captainBuild.jumpAnim()
    captainDashAnimList = captainBuild.dashAnim()
    captainAttack1List = captainBuild.attackAnim()
    captainTallest = captainBuild.tallest()
    captainWidest = captainBuild.widest()
    captainDefault = captainBuild.default()

    #Creates an instance of each character for each player
    zero1 = Character(zeroIdleAnimList,zeroWalkAnimList,zeroStartStopAnimList,zeroJumpAnimList,zeroDashAnimList,zeroAttack1List,\
                     0,zeroDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"right",zeroWidest,zeroTallest,\
                     1,20,0,0,0,0,200,SCREEN_HEIGHT-zeroTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"zero")

    jade1 = Character(jadeIdleAnimList,jadeWalkAnimList,jadeStartStopAnimList,jadeJumpAnimList,jadeDashAnimList,jadeAttack1List,\
                     0,jadeDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"right",jadeWidest,jadeTallest,\
                     1,20,0,0,0,0,200,SCREEN_HEIGHT-jadeTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"jade")

    koopa1 = Character(koopaIdleAnimList,koopaWalkAnimList,koopaStartStopAnimList,koopaJumpAnimList,koopaDashAnimList,koopaAttack1List,\
                     0,koopaDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"right",koopaWidest,koopaTallest,\
                     1,20,0,0,0,0,200,SCREEN_HEIGHT-koopaTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"koopa")

    captain1 = Character(captainIdleAnimList,captainWalkAnimList,captainStartStopAnimList,captainJumpAnimList,captainDashAnimList,captainAttack1List,\
                     0,captainDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"right",captainWidest,captainTallest,\
                     1,20,0,0,0,0,200,SCREEN_HEIGHT-captainTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"captain")

    zero2 = Character(blueZeroIdleAnimList,blueZeroWalkAnimList,blueZeroStartStopAnimList,blueZeroJumpAnimList,blueZeroDashAnimList,blueZeroAttack1List,\
                     0,blueZeroDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"left",blueZeroWidest,blueZeroTallest,\
                     1,20,0,0,0,0,SCREEN_WIDTH-200,SCREEN_HEIGHT-blueZeroTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"zero")

    jade2 = Character(jadeIdleAnimList,jadeWalkAnimList,jadeStartStopAnimList,jadeJumpAnimList,jadeDashAnimList,jadeAttack1List,\
                     0,jadeDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"left",jadeWidest,jadeTallest,\
                     1,20,0,0,0,0,SCREEN_WIDTH-200,SCREEN_HEIGHT-jadeTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"jade")

    koopa2 = Character(koopaIdleAnimList,koopaWalkAnimList,koopaStartStopAnimList,koopaJumpAnimList,koopaDashAnimList,koopaAttack1List,\
                     0,koopaDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"left",koopaWidest,koopaTallest,\
                     1,20,0,0,0,0,SCREEN_WIDTH-200,SCREEN_HEIGHT-koopaTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"koopa")

    captain2 = Character(captainIdleAnimList,captainWalkAnimList,captainStartStopAnimList,captainJumpAnimList,captainDashAnimList,captainAttack1List,\
                     0,captainDefault,5,0,0,0,0,0,0,0,0,0,0,0,0,"left",captainWidest,captainTallest,\
                     1,20,0,0,0,0,SCREEN_WIDTH-200,SCREEN_HEIGHT-captainTallest.ScaledHeight,\
                     2,23,False,False,False,False,False,False,"idle","ground",25,"zero",5,100,100.0,1.2,False,"captain")


    #Creates System
    system = System()

    #Creates Player(s)
    playerList = []

    mainLoop = MainMenu.mainMenu()
    mainLoop,char1,char2 = CharMenu.characterSelect()
    
    #Character Select
    if char1 == "koopa":
      player1Character = koopa1
    elif char1 == "captain":
      player1Character = captain1
    elif char1 == "jade":
      player1Character = jade1
    else:
      player1Character = zero1

    if char2 == "koopa":
      player2Character = koopa2
    elif char2 == "captain":
      player2Character = captain2
    elif char2 == "jade":
      player2Character = jade2
    else:
      player2Character = zero2

    #Creates Players
    player1 = Player(1,player1Character)
    player2 = Player(2,player2Character)
    playerList.append(player1)
    playerList.append(player2)
    mainLoop,x,y = MainMenu.stageMenu()
    stage = GameWindow.stageSelect(x,y)
    background = image.load(stage).convert()
    fullScreenBool = True
    mixer.music.stop()
    
    #Gets correct stage music
    if stage == "Stage1.jpg":
        stageSong = "CreepyWoodsMusic.ogg"
    elif stage == "Stage2.jpg":
        stageSong = "MortalCombatMusic.ogg"
    elif stage == "Stage3.jpg":
        stageSong = "HellMusic.ogg"
    elif stage == "Stage0.jpg":
        stageSong = "FullMoonMusic.ogg"
    elif stage == "Stage5.jpg":
        stageSong = "AbandonedTownMusic.ogg"
    elif stage == "Stage6.jpg":
        stageSong = "ChinatownMusic.ogg"
    elif stage == "Stage7.jpg":
        stageSong = "DigitalWorldMusic.ogg"
    elif stage == "Stage8.jpg":
        stageSong = "AncientSpringMusic.ogg"
    elif stage == "Stage9.jpg":
        stageSong = "RoadMusic.ogg"

    mixer.music.load(stageSong)
    mixer.music.play()

    #initializes game pads
    joystick1 = None
    joystick2 = None
    joystick_count = joystick.get_count()
    if joystick_count > 0:
        joystick1 = joystick.Joystick(0)
    if joystick_count > 1:
        joystick2 = joystick.Joystick(1)

    timer.stopWatch.reset()
    
    #Main Loop
    while system.mainLoop == True:
        gamePad(joystick1, joystick2)
        #Event Handler
        for Event in event.get():

            #Exit
            if Event.type == QUIT:
                quit()
                sys.exit()

            #Press Key
            elif Event.type == KEYDOWN:

                #A (Player 1)
                if Event.key == K_a:
                    player1.pushingLeft = True

                #D (Player 1)
                if Event.key == K_d:
                    player1.pushingRight = True

                #W (Player 1)
                if Event.key == K_w:
                    player1.pushingUp = True

                #S (Player 1)
                if Event.key == K_s:
                    player1.pushingDown = True

                #F (Player 1)
                if Event.key == K_f:
                    player1.pushingRightDash = True

                #CapsLock (Player 1)
                if Event.key == K_CAPSLOCK:
                    player1.pushingLeftDash = True

                #Squigly Key (Player 1)
                if Event.key == K_BACKQUOTE:
                    print(player1.character)

                #E (Player 1)
                if Event.key == K_e:
                    player1.pushingAttack1 = True

                #P
                if Event.key == K_p:
                    pushingPause = True

                if len(playerList) > 1:
                    
                    #Left (Player 2)
                    if Event.key == K_LEFT:
                        player2.pushingLeft = True

                    #Right (Player 2)
                    if Event.key == K_RIGHT:
                        player2.pushingRight = True

                    #Up (Player 2)
                    if Event.key == K_UP:
                        player2.pushingUp = True

                    #Down (Player 2)
                    if Event.key == K_DOWN:
                        player2.pushingDown = True

                    #Keypad 0 (Player 2)
                    if Event.key == K_KP0:
                        player2.pushingRightDash = True

                    #Right Ctrl (Player 2)
                    if Event.key == K_RCTRL:
                        player2.pushingLeftDash = True

                    #Home (Player 2)
                    if Event.key == K_HOME:
                        print(player2.character)

                    #Right Shift (Player 2)
                    if Event.key == K_RSHIFT:
                        player2.pushingAttack1 = True

            #Release Key

            elif Event.type == KEYUP:
                
                if Event.key == K_ESCAPE:
                    quit()
                    sys.exit()
                        
                if Event.key == K_t and fullScreenBool == True:
                    screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False

                elif Event.key == K_t and fullScreenBool == False:
                    screen = display.set_mode(\
                        (SCREEN_WIDTH,SCREEN_HEIGHT),FULLSCREEN)
                    fullScreenBool = True

                #A (Player 1)
                if Event.key == K_a:
                    player1.pushingLeft = False

                #D (Player 1)
                if Event.key == K_d:
                    player1.pushingRight = False

                #W (Player 1)
                if Event.key == K_w:
                    player1.pushingUp = False

                #S (Player 1)
                if Event.key == K_s:
                    player1.pushingDown = False

                #P
                if Event.key == K_p:
                  pushingPause = False

                if len(playerList) > 1:
                    
                    #Left (Player 2)
                    if Event.key == K_LEFT:
                        player2.pushingLeft = False

                    #Right (Player 2)
                    if Event.key == K_RIGHT:
                        player2.pushingRight = False

                    #Up (Player 2)
                    if Event.key == K_UP:
                        player2.pushingUp = False

                    #Down (Player 2)
                    if Event.key == K_DOWN:
                        player2.pushingDown = False

            #Game pad keys for moving
            elif Event.type == JOYAXISMOTION:
                
                if joyLeft(joystick1):
                    player1.pushingLeft = True

                if joyRight(joystick1):
                    player1.pushingRight = True

                if not joyLeft(joystick1):
                    player1.pushingLeft = False

                if not joyRight(joystick1):
                    player1.pushingRight = False

                if len(playerList) > 1 and joystick_count > 1:
                    
                    if joyLeft(joystick2):
                        player2.pushingLeft = True

                    if joyRight(joystick2):
                        player2.pushingRight = True

                    if not joyLeft(joystick2):
                        player2.pushingLeft = False

                    if not joyRight(joystick2):
                        player2.pushingRight = False

            elif Event.type == JOYBUTTONDOWN:

                if joystick1.get_button(0) == 1:
                    player1.pushingUp = True

                if joystick1.get_button(1) == 1:
                    player1.pushingDown = True

                if joystick1.get_button(2) == 1:
                    player1.pushingAttack1 = True

                if joystick1.get_button(4) == 1:
                    player1.pushingLeftDash = True

                if joystick1.get_button(5) == 1:
                    player1.pushingRightDash = True

                if len(playerList) > 1 and joystick_count > 1:
                    
                    if joystick2.get_button(0) == 1:
                        player2.pushingUp = True

                    if joystick2.get_button(1) == 1:
                        player2.pushingDown = True

                    if joystick2.get_button(2) == 1:
                        player2.pushingAttack1 = True

                    if joystick2.get_button(4) == 1:
                        player2.pushingLeftDash = True

                    if joystick2.get_button(5) == 1:
                        player2.pushingRightDash = True

            elif Event.type == JOYBUTTONUP:

                if joystick1.get_button(0) == 0:
                    player1.pushingUp = False 

                if joystick1.get_button(2) == 0:
                    player1.pushingDown = False

                if len(playerList) > 1 and joystick_count > 1:
                    
                    if joystick2.get_button(0) == 0:
                        player2.pushingUp = False

                    if joystick2.get_button(2) == 0:
                        player2.pushingDown = False

        if joystick_count > 0:  
            if joystick1.get_button(6) == 1 and joystick1.get_button(7) == 1:
                    quit()
                    sys.exit()

            if joystick1.get_button(6) == 1 and fullScreenBool == True:
                    screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False
                    
            if joystick1.get_button(6) == 1 and fullScreenBool == False:
                    screen = display.set_mode((\
                        SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)
                    fullScreenBool = True

        if joystick_count > 1:        
            if joystick2.get_button(6) == 1 and joystick2.get_button(7) == 1:
                    quit()
                    sys.exit()

            if joystick2.get_button(6) == 1 and fullScreenBool == True:
                    screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                    fullScreenBool = False
                    

            if joystick2.get_button(6) == 1 and fullScreenBool == False:
                    screen = display.set_mode((\
                        SCREEN_WIDTH,SCREEN_HEIGHT), FULLSCREEN)
                    fullScreenBool = True
                    
        #Movement
                 
        #(Player 1) A (Left)
        if player1.pushingLeft == True and player1.pushingRight == False:
            if player1.character.status != "dashing":
                player1.character.moveLeft()
                
        #(Player 1) D (Right)
        if player1.pushingRight == True and player1.pushingLeft == False:
            if player1.character.status != "dashing":
                player1.character.moveRight()

        #(Player 1) W (Up)
        if player1.pushingUp == True:
            player1.pushingUp = False
            player1.character.jump()

        #(Player 1) S (Down)
        if player1.pushingDown == True and player1.character.status == "idle":
            player1.character.isCrouched = True
        else:
            player1.character.isCrouched = False

        #(Player 1) CapsLock/F (Dash)
        if player1.pushingRightDash == True:
            player1.pushingRightDash = False
            player1.character.rightDash()
        if player1.pushingLeftDash == True:
            player1.pushingLeftDash = False
            player1.character.leftDash()

        #(Player 1) E (Attack 1)
        if player1.pushingAttack1 == True:
            player1.pushingAttack1 = False
            player1.character.attack()

        if len(playerList) > 1:
            #(Player 2) RightArrow (Right)
            if player2.pushingRight == True and player2.pushingLeft == False:
                if player2.character.status != "dashing":
                    player2.character.moveRight()

            #(Player 2) LeftArrow (Left)
            if player2.pushingLeft == True and player2.pushingRight == False:
                if player2.character.status != "dashing":
                    player2.character.moveLeft()

            #(Player 2) UpArrow (Up)
            if player2.pushingUp == True:
                player2.pushingUp = False
                player2.character.jump()

            #(Player 2) DownArrow (Down)
            if player2.pushingDown == True and \
            player2.character.status == "idle":
                player2.character.isCrouched = True
            else:
                player2.character.isCrouched = False

            #(Player 2) LeftCtrl/Keypad0 (Dash)0.
            if player2.pushingRightDash == True:
                player2.pushingRightDash = False

                player2.character.rightDash()
            if player2.pushingLeftDash == True:
                player2.pushingLeftDash = False
                player2.character.leftDash()

            #(Player 2) RightShift (Attack 1):
            if player2.pushingAttack1 == True:
                player2.pushingAttack1 = False
                player2.character.attack()

        #Draws Background
        screen.blit(background,(0,0))
        healthBar.drawHealth()
        powerBar.drawPowerBar(player1.character.power,player2.character.power)
        timer.drawTimer()

        #Updates Player
        for item in playerList:
            item.character.update(pushingPause,playerList,system,screen,healthBar,bubble)

        #Updates Player Halo
        system.updateHalo(playerList,screen)

        #If Win
        if timer.countDown == 0 or healthBar.p1H <= 200 or healthBar.p2H <= 0:
            #Calls back to the system class method
            system.gameWinScreen(healthBar,system,player1Win,player2Win,screen)

        #Locks FPS
        time.Clock().tick(FPS)

        #Updates screen
        display.flip()
