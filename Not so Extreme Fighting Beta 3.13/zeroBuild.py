from Classes import sprite
import pygame
#Creates sprites

        #Zero

def idleAnim():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroStand =sprite("zeroStand",zeroSpriteSheet,5,48,5,52,5,0,0)
    
    return [zeroStand]

def walkList():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    
    zeroWalk3 =sprite("zeroWalk3",zeroSpriteSheet,206,254,164,210,5,0,0)
    zeroWalk4 =sprite("zeroWalk4",zeroSpriteSheet,261,307,163,210,5,0,0)
    zeroWalk5 = sprite("zeroWalk5",zeroSpriteSheet,315,359,161,209,5,0,0)
    zeroWalk6 = sprite("zeroWalk6",zeroSpriteSheet,367,407,161,209,5,0,0)
    zeroWalk7 = sprite("zeroWalk7",zeroSpriteSheet,419,464,164,211,5,0,0)
    zeroWalk8 = sprite("zeroWalk8",zeroSpriteSheet,475,524,165,210,5,0,0)
    zeroWalk9 = sprite("zeroWalk9",zeroSpriteSheet,531,576,166,212,5,0,0)
    zeroWalk10 = sprite("zeroWalk10",zeroSpriteSheet,583,633,165,212,5,0,0)
    zeroWalk11 = sprite("zeroWalk11",zeroSpriteSheet,640,686,164,212,5,0,0)
    zeroWalk12 = sprite("zeroWalk12",zeroSpriteSheet,695,738,163,212,5,0,0)
    zeroWalk13 = sprite("zeroWalk13",zeroSpriteSheet,745,787,163,212,5,0,0)
    zeroWalk14 = sprite("zeroWalk14",zeroSpriteSheet,795,840,164,212,5,0,0)

    return [zeroWalk3,zeroWalk4,zeroWalk5,zeroWalk6,zeroWalk7,\
            zeroWalk8,zeroWalk9,zeroWalk10,zeroWalk11,\
            zeroWalk12,zeroWalk13,zeroWalk14]

def startStopAnim():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroWalk1 = sprite("zeroWalk1",zeroSpriteSheet,93,144,164,208,5,0,0)
    zeroWalk2 = sprite("zeroWalk2",zeroSpriteSheet,151,201,165,210,5,0,0)

    return [zeroWalk1,zeroWalk2]

def jumpAnim():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroJump1 = sprite("zeroJump1",zeroSpriteSheet,14,53,89,137,5,0,0)
    zeroJump2 = sprite("zeroJump2",zeroSpriteSheet,59,103,85,141,5,0,0)
    zeroJump3 = sprite("zeroJump3",zeroSpriteSheet,110,153,85,141,5,0,0)
    zeroJump4 = sprite("zeroJump4",zeroSpriteSheet,163,206,84,141,5,0,0)
    zeroJump5 = sprite("zeroJump5",zeroSpriteSheet,213,256,84,140,5,0,0)
    zeroJump6 = sprite("zeroJump6",zeroSpriteSheet,263,303,84,136,5,0,0)
    zeroJump7 = sprite("zeroJump7",zeroSpriteSheet,308,348,84,139,5,0,0)
    zeroJump8 = sprite("zeroJump8",zeroSpriteSheet,353,389,84,148,5,0,0)
    zeroJump9 = sprite("zeroJump9",zeroSpriteSheet,398,433,75,152,5,0,0)
    zeroJump10 = sprite("zeroJump10",zeroSpriteSheet,443,478,72,151,5,0,0)
    zeroJump11 = sprite("zeroJump11",zeroSpriteSheet,488,528,90,149,5,0,0)

    return [zeroJump1,zeroJump2,zeroJump3,zeroJump4,zeroJump5,zeroJump6,\
            zeroJump7,zeroJump8,zeroJump9,zeroJump10,zeroJump11]

def dashAnim():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroDash1 = sprite("zeroDash1",zeroSpriteSheet,541,611,104,149,5,-5,0)
    zeroDash2 = sprite("zeroDash2",zeroSpriteSheet,620,727,112,148,5,-5,0)
    zeroDash3 = sprite("zeroDash3",zeroSpriteSheet,734,865,112,150,5,-5,0)

    return [zeroDash1,zeroDash2,zeroDash3]

def attackAnim():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroSword1 = sprite("zeroSword1",zeroSpriteSheet,7,46,298,344,5,0,0)
    zeroSword2 = sprite("zeroSword2",zeroSpriteSheet,52,98,294,344,5,-6,0)
    zeroSword3 = sprite("zeroSword3",zeroSpriteSheet,102,151,283,346,5,-3,-4)
    zeroSword4 = sprite("zeroSword4",zeroSpriteSheet,157,235,283,346,5,-3,-17)
    zeroSword5 = sprite("zeroSword5",zeroSpriteSheet,242,329,283,343,5,-5,-15)
    zeroSword6 = sprite("zeroSword6",zeroSpriteSheet,337,428,295,343,5,-9,-6)
    zeroSword7 = sprite("zeroSword7",zeroSpriteSheet,437,520,294,343,5,-2,-6)
    zeroSword8 = sprite("zeroSword8",zeroSpriteSheet,527,597,298,343,5,-1,0)
    zeroSword9 = sprite("zeroSword9",zeroSpriteSheet,607,666,298,342,5,0,0)
    zeroSword10 = sprite("zeroSword10",zeroSpriteSheet,677,729,297,342,5,0,0)
    zeroSword11 = sprite("zeroSword11",zeroSpriteSheet,737,782,297,342,5,0,0)

    return [zeroSword1,zeroSword2,zeroSword3,zeroSword4,\
            zeroSword5,zeroSword6,zeroSword7,zeroSword8,\
            zeroSword9,zeroSword10,zeroSword11]
def widest():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroStand = sprite("zeroStand",zeroSpriteSheet,5,48,5,52,5,0,0)
    
    return zeroStand

def tallest():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroStand = sprite("zeroStand",zeroSpriteSheet,5,48,5,52,5,0,0)
    
    return zeroStand

def default():
    zeroSpriteSheet = pygame.image.load("Zero Sprite Sheet.gif").convert_alpha()
    zeroStand = sprite("zeroStand",zeroSpriteSheet,5,48,5,52,5,0,0)
    
    return zeroStand
