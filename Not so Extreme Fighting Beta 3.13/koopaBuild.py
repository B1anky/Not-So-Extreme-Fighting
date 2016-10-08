from Classes import sprite
import pygame

#KOOPASHEET CRED: nonononomo
#http://www.deviantart.com/art/Star-Mario-Red-ninjakoopa-Sprites-368850154

def idleAnim():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaStand1 = sprite("koopaStand1",koopaSheet,1102,1141,29,82,3,0,150)
    koopaStand2 = sprite("koopaStand2",koopaSheet,1056,1094,28,82,3,0,150)
    koopaStand3 = sprite("koopaStand3",koopaSheet,1009,1048,30,82,3,0,150)
    return [koopaStand1,koopaStand2,koopaStand3]

def startStopAnim():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaWalk1 = sprite("koopaWalk1",koopaSheet,994,1033,91,144,3,0,150)
    koopaWalk2 = sprite("koopaWalk2",koopaSheet,1036,1080,92,144,3,0,150)
    return [koopaWalk1,koopaWalk2]

def walkList():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaWalk3 = sprite("koopaWalk3",koopaSheet,1096,1143,94,144,3,0,140)
    koopaWalk4 = sprite("koopaWalk2",koopaSheet,1036,1080,92,144,3,0,140)
    koopaWalk5 = sprite("koopaWalk1",koopaSheet,994,1033,91,144,3,0,140)
    return [koopaWalk3,koopaWalk4,koopaWalk5]
    

def crouchAnim():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaCrouch1 = sprite("koopaCrouch1",koopaSheet,822,860,311,361,3,0,0)
    koopaCrouch2 = sprite("koopaCrouch2",koopaSheet,878,907,324,356,3,0,0)
    koopaCrouch3 = sprite("koopaCrouch3",koopaSheet,916,943,327,353,3,0,0)
    koopaCrouch4 = sprite("koopaCrouch4",koopaSheet,1101,1134,151,176,3,0,0)
    return [koopaCrouch1,koopaCrouch2,koopaCrouch3,koopaCrouch4]

def jumpAnim():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaJump1 = sprite("koopaJump1",koopaSheet,1031,1078,250,299,3,0,180)
    koopaJump2 = sprite("koopaJump2",koopaSheet,1031,1078,250,299,3,0,180)
    koopaJump3 = sprite("koopaJump3",koopaSheet,965,1016,242,296,3,0,180)
    koopaJump4 = sprite("koopaJump4",koopaSheet,965,1016,242,296,3,0,180)
    koopaJump5 = sprite("koopaJump5",koopaSheet,845,889,243,290,3,0,180)
    return [koopaJump1,koopaJump2,koopaJump3,koopaJump4,koopaJump5]

def dashAnim():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
##    koopaDash1 = sprite("koopaDash1",koopaSheet,822,860,311,361,3,0,0)
##    koopaDash2 = sprite("koopaDash2",koopaSheet,878,907,324,356,3,0,0)
##    koopaDash3 = sprite("koopaDash3",koopaSheet,916,943,327,353,3,0,0)
##    koopaDash4 = sprite("koopaDash4",koopaSheet,1101,1134,151,176,3,0,0)
    koopaDash5 = sprite("koopaDash5",koopaSheet,1058,1086,152,176,3,0,240)
    koopaDash6 = sprite("koopaDash6",koopaSheet,1058,1086,152,176,3,0,240)
    koopaDash7 = sprite("koopaDash7",koopaSheet,1018,1046,152,176,3,0,240)
    koopaDash8 = sprite("koopaDash8",koopaSheet,1018,1046,152,176,3,0,240)
##    koopaDash9 = sprite("koopaDash9",koopaSheet,970,1002,151,176,3,0,0)
##    koopaDash10 = sprite("koopaDash10",koopaSheet,970,1002,151,176,3,0,0)
##    koopaDash11 = sprite("koopaDash11",koopaSheet,1018,1046,152,176,3,0,0)
##    koopaDash12 = sprite("koopaDash12",koopaSheet,1057,1086,152,176,3,0,0)
##    koopaDash13 = sprite("koopaDash13",koopaSheet,1101,1134,151,176,3,0,0)
##    return [koopaDash1,koopaDash2,koopaDash3,koopaDash4,koopaDash5,\
##            koopaDash6,koopaDash7,koopaDash8,koopaDash9,koopaDash10,\
##            koopaDash11,koopaDash12,koopaDash13]
    return [koopaDash5,koopaDash6,koopaDash7,koopaDash8]
def attackAnim():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaAttack1 = sprite("koopaAttack1",koopaSheet,341,365,252,286,5,0,140)
    koopaAttack2 = sprite("koopaAttack2",koopaSheet,371,399,252,286,5,0,140)
    koopaAttack3 = sprite("koopaAttack3",koopaSheet,404,432,252,286,5,0,140)
    return [koopaAttack1,koopaAttack2,koopaAttack3]

def widest():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaJump1 = sprite("koopaJump1",koopaSheet,1072,1124,229,338,3,0,0)
    return koopaJump1

def tallest():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaJump1 = sprite("koopaJump1",koopaSheet,1072,1124,229,338,3,0,0)
    return koopaJump1

def default():
    koopaSheet = pygame.image.load("koopaSheet.png").convert_alpha()
    koopaStand1 = sprite("koopaStand1",koopaSheet,1096,1135,21,74,3,0,0)
    return koopaStand1
    
    
    
    
