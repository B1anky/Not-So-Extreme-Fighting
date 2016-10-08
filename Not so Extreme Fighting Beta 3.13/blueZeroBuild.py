from Classes import sprite
import pygame

#Creates sprite
    #BlueZero

def idleAnim():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroStand = sprite("blueZeroStand",blueZeroSpriteSheet,5,48,5,52,5,0,0)
    
    return [blueZeroStand]

def walkList():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    
    blueZeroWalk3 = sprite("blueZeroWalk3",blueZeroSpriteSheet,206,254,164,\
        210,5,0,0)
    blueZeroWalk4 = sprite("blueZeroWalk4",blueZeroSpriteSheet,261,307,163,\
        210,5,0,0)
    blueZeroWalk5 = sprite("blueZeroWalk5",blueZeroSpriteSheet,315,359,161,\
        209,5,0,0)
    blueZeroWalk6 = sprite("blueZeroWalk6",blueZeroSpriteSheet,367,407,161,\
        209,5,0,0)
    blueZeroWalk7 = sprite("blueZeroWalk7",blueZeroSpriteSheet,419,464,164,\
        211,5,0,0)
    blueZeroWalk8 = sprite("blueZeroWalk8",blueZeroSpriteSheet,475,524,165,\
        210,5,0,0)
    blueZeroWalk9 = sprite("blueZeroWalk9",blueZeroSpriteSheet,531,576,166,\
        212,5,0,0)
    blueZeroWalk10 = sprite("blueZeroWalk10",blueZeroSpriteSheet,583,633,165,\
        212,5,0,0)
    blueZeroWalk11 = sprite("blueZeroWalk11",blueZeroSpriteSheet,640,686,164,\
        212,5,0,0)
    blueZeroWalk12 = sprite("blueZeroWalk12",blueZeroSpriteSheet,695,738,163,\
        212,5,0,0)
    blueZeroWalk13 = sprite("blueZeroWalk13",blueZeroSpriteSheet,745,787,163,\
        212,5,0,0)
    blueZeroWalk14 = sprite("blueZeroWalk14",blueZeroSpriteSheet,795,840,164,\
        212,5,0,0)
    
    return [blueZeroWalk3,blueZeroWalk4,blueZeroWalk5,blueZeroWalk6,blueZeroWalk7,\
            blueZeroWalk8,blueZeroWalk9,blueZeroWalk10,blueZeroWalk11,\
            blueZeroWalk12,blueZeroWalk13,blueZeroWalk14]

def startStopAnim():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroWalk1 = sprite("blueZeroWalk1",blueZeroSpriteSheet,93,144,164,\
        208,5,0,0)
    blueZeroWalk2 = sprite("blueZeroWalk2",blueZeroSpriteSheet,151,201,165,\
        210,5,0,0)
    return [blueZeroWalk1,blueZeroWalk2]

def jumpAnim():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroJump1 = sprite("blueZeroJump1",blueZeroSpriteSheet,14,53,89,137,\
        5,0,0)
    blueZeroJump2 = sprite("blueZeroJump2",blueZeroSpriteSheet,59,103,85,141,\
        5,0,0)
    blueZeroJump3 = sprite("blueZeroJump3",blueZeroSpriteSheet,110,153,85,141,\
        5,0,0)
    blueZeroJump4 = sprite("blueZeroJump4",blueZeroSpriteSheet,163,206,84,141,\
        5,0,0)
    blueZeroJump5 = sprite("blueZeroJump5",blueZeroSpriteSheet,213,256,84,140,\
        5,0,0)
    blueZeroJump6 = sprite("blueZeroJump6",blueZeroSpriteSheet,263,303,84,136,\
        5,0,0)
    blueZeroJump7 = sprite("blueZeroJump7",blueZeroSpriteSheet,308,348,84,139,\
        5,0,0)
    blueZeroJump8 = sprite("blueZeroJump8",blueZeroSpriteSheet,353,389,84,148,\
        5,0,0)
    blueZeroJump9 = sprite("blueZeroJump9",blueZeroSpriteSheet,398,433,75,152,\
        5,0,0)
    blueZeroJump10 = sprite("blueZeroJump10",blueZeroSpriteSheet,443,478,72,\
        151,5,0,0)
    blueZeroJump11 = sprite("blueZeroJump11",blueZeroSpriteSheet,488,528,90,\
        149,5,0,0)
    return [blueZeroJump1,blueZeroJump2,blueZeroJump3,blueZeroJump4,blueZeroJump5,blueZeroJump6,\
            blueZeroJump7,blueZeroJump8,blueZeroJump9,blueZeroJump10,blueZeroJump11]

def dashAnim():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroDash1 = sprite("blueZeroDash1",blueZeroSpriteSheet,541,611,104,\
        149,5,-5,0)
    blueZeroDash2 = sprite("blueZeroDash2",blueZeroSpriteSheet,620,727,112,\
        148,5,-5,0)
    blueZeroDash3 = sprite("blueZeroDash3",blueZeroSpriteSheet,734,865,112,\
        150,5,-5,0)
    return [blueZeroDash1,blueZeroDash2,blueZeroDash3]

def attackAnim():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroSword1 = sprite("blueZeroSword1",blueZeroSpriteSheet,7,46,298,\
        344,5,0,0)
    blueZeroSword2 = sprite("blueZeroSword2",blueZeroSpriteSheet,52,98,294,\
        344,5,-6,0)
    blueZeroSword3 = sprite("blueZeroSword3",blueZeroSpriteSheet,102,151,283,\
        346,5,-3,-4)
    blueZeroSword4 = sprite("blueZeroSword4",blueZeroSpriteSheet,157,235,283,\
        346,5,-3,-17)
    blueZeroSword5 = sprite("blueZeroSword5",blueZeroSpriteSheet,242,329,283,\
        343,5,-5,-15)
    blueZeroSword6 = sprite("blueZeroSword6",blueZeroSpriteSheet,337,428,295,\
        343,5,-9,-6)
    blueZeroSword7 = sprite("blueZeroSword7",blueZeroSpriteSheet,437,520,294,\
        343,5,-2,-6)
    blueZeroSword8 = sprite("blueZeroSword8",blueZeroSpriteSheet,527,597,298,\
        343,5,-1,0)
    blueZeroSword9 = sprite("blueZeroSword9",blueZeroSpriteSheet,607,666,298,\
        342,5,0,0)
    blueZeroSword10 = sprite("blueZeroSword10",blueZeroSpriteSheet,677,729,\
        297,342,5,0,0)
    blueZeroSword11 = sprite("blueZeroSword11",blueZeroSpriteSheet,737,782,\
        297,342,5,0,0)
    return [blueZeroSword1,blueZeroSword2,blueZeroSword3,blueZeroSword4,\
            blueZeroSword5,blueZeroSword6,blueZeroSword7,blueZeroSword8,\
            blueZeroSword9,blueZeroSword10,blueZeroSword11]

def widest():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroStand = sprite("blueZeroStand",blueZeroSpriteSheet,5,48,5,52,5,0,0)
    
    return blueZeroStand

def tallest():
    blueZeroSpriteSheet =pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroStand = sprite("blueZeroStand",blueZeroSpriteSheet,5,48,5,52,5,0,0)

    return blueZeroStand

def default():
    blueZeroSpriteSheet = pygame.image.load("Blue Zero Sprite Sheet.gif")\
        .convert_alpha()
    blueZeroStand = sprite("blueZeroStand",blueZeroSpriteSheet,5,48,5,52,5,0,0)
    
    return blueZeroStand
