from Classes import sprite
import pygame


def idleAnim():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeStand1 = sprite("jadeStand1",jadeSheet,66,99,2,88,3,0,-100)
    jadeStand2 = sprite("jadeStand2",jadeSheet,101,132,4,87,3,0,-100)
    jadeStand3 = sprite("jadeStand3",jadeSheet,132,163,4,87,3,0,-100)

    return [jadeStand1,jadeStand2,jadeStand3]

def walkList():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeWalk3 = sprite("jadeWalk3",jadeSheet,140,164,89,168,3,0,-100)
    jadeWalk4 = sprite("jadeWalk4",jadeSheet,173,208,89,167,3,0,-100)
    jadeWalk5 = sprite("jadeWalk5",jadeSheet,213,241,89,167,3,0,-100)
    jadeWalk6 = sprite("jadeWalk6",jadeSheet,246,271,89,169,3,0,-100)

    return [jadeWalk3,jadeWalk4,jadeWalk5,jadeWalk6]

def startStopAnim():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeWalk1 = sprite("jadeWalk1",jadeSheet,57,92,90,168,3,0,-100)
    jadeWalk2 = sprite("jadeWalk2",jadeSheet,101,128,88,167,3,0,-100)
    
    return [jadeWalk1,jadeWalk2]

def jumpAnim():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeJump1 = sprite("jadeJump1",jadeSheet,290,325,99,164,3,0,-100)
    jadeJump2 = sprite("jadeJump2",jadeSheet,329,365,101,199,3,0,-100)
    jadeJump3 = sprite("jadeJump3",jadeSheet,378,414,116,179,3,0,-100)
    jadeJump4 = sprite("jadeJump4",jadeSheet,424,455,115,172,3,0,-100)
    jadeJump5 = sprite("jadeJump5",jadeSheet,465,498,102,209,3,0,-100)

    return [jadeJump3,jadeJump3,jadeJump3,jadeJump3,jadeJump5]

    
    #jadeCrouch1 = sprite("jadeCrouch1",jadeSheet,239,275,47,87,3)


def dashAnim():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
##    jadeBackflip1 = sprite("jadeBackflip1",jadeSheet,169,226,296,366,4,0,-100)
##    jadeBackflip2 = sprite("jadeBackflip2",jadeSheet,282,361,343,382,4,0,-50)
    jadeDash1 = sprite("jadeDash1",jadeSheet,548,620,119,175,3,0,0)
    return [jadeDash1,jadeDash1]

def attackAnim():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeStaff1 = sprite("jadeStaff1",jadeSheet,225,299,186,256,3,0,-70)
    jadeStaff2 = sprite("jadeStaff2",jadeSheet,400,484,303,375,3,0,-70)
    jadeStaff3 = sprite("jadeStaff3",jadeSheet,493,568,309,379,3,0,-70)

    return [jadeStaff1,jadeStaff2,jadeStaff3]

def widest():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeBackflip3 = sprite("jadeBackflip3",jadeSheet,142,217,189,254,3,0,0)
    return jadeBackflip3

def tallest():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeJump3 = sprite("jadeJump5",jadeSheet,423,455,114,172,3,0,0)
    return jadeJump3

def default():
    jadeSheet = pygame.image.load("jadeSheet.png").convert_alpha()
    jadeStand1 = sprite("jadeStand1",jadeSheet,66,99,2,88,3,0,0)
    return jadeStand1






    
    
    
