#-------------------------------------------------------------------------------
    #NOT-SO EXTREME FIGHTING
    #  Ruben Hernandez, Michael Melnik, Alex Miller, Brett Sackstein 

    #   Build Captain Falcon Module
#-------------------------------------------------------------------------------
# CaptFalcSheet cred: InfinitysEnd
# http://infinitysend.deviantart.com/art/SSB-Melee-Captain-Falcon-26122435

from Classes import sprite
import pygame

def idleAnim():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainStand1 = sprite("captainStand1",captainSheet,19,61,21,78,5,0,-45)
    return [captainStand1]

def walkList():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainWalk3 = sprite("captainWalk3",captainSheet,495,565,111,165,5,0,-20)
    captainWalk4 = sprite("captainWalk4",captainSheet,578,620,111,165,5,0,-20)
    captainWalk5 = sprite("captainWalk5",captainSheet,209,278,115,165,5,0,-20)
    captainWalk6 = sprite("captainWalk6",captainSheet,286,356,114,165,5,0,-20)
    return [captainWalk3,captainWalk4,\
            captainWalk5,captainWalk6]

def startStopAnim():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainWalk1 = sprite("captainWalk1",captainSheet,367,414,111,165,5,0,-20)
    captainWalk2 = sprite("captainWalk2",captainSheet,419,488,115,165,5,0,-20)
    return [captainWalk1,captainWalk2]

    
def jumpAnim():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainJump1 = sprite("captainJump1",captainSheet,26,79,111,162,5,0,-40)
    captainJump2 = sprite("captainJump2",captainSheet,247,286,11,85,5,0,-40)
    captainJump3 = sprite("captainJump3",captainSheet,306,341,395,468,5,0,-40)
    captainJump4 = sprite("captainJump4",captainSheet,26,79,111,162,5,0,-40)
    return [captainJump1,captainJump2,captainJump2,captainJump2,\
            captainJump3,captainJump3]

def dashAnim():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainDash1 = sprite("captainJab1",captainSheet,21,106,408,446,5,0,0)
    return [captainDash1]

def attackAnim():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainPunch1 = sprite("captainPunch1",captainSheet,26,79,111,162,5,0,-70)
    captainPunch2 = sprite("captainPunch2",captainSheet,414,516,194,260,5,0,-70)
    captainPunch3 = sprite("captainPunch3",captainSheet,530,640,195,260,5,0,-70)
    captainPunch4 = sprite("captainPunch4",captainSheet,270,391,194,260,5,0,-70)
    return [captainPunch1,captainPunch2,captainPunch3,captainPunch4]

def widest():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainStand1 = sprite("captainStand1",captainSheet,19,61,21,78,5,0,0)
    return captainStand1

def tallest():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainJump4 = sprite("captainJump4",captainSheet,26,79,111,162,5,0,0)
    return captainJump4

def default():
    captainSheet = pygame.image.load("CaptFalcSheet.gif").convert_alpha()
    captainStand1 = sprite("captainStand1",captainSheet,19,61,21,78,5,0,0)
    return captainStand1

