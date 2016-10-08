import pygame

##REFERENCE: http://www.pygame.org/docs/ref/joystick.html
##Interprets gamepad input and converts it to readable lists and tuples
##Narrative: Initializes game pads as objects
##Preconditions: Game pad must be plugged in to USB
##Post conditions: Reads the I/O of computer for game pads and updates values
def gamePad(joystick1, joystick2):
    joystick_count = pygame.joystick.get_count()
  
    if joystick_count > 0:
      joystick1.init()
      name = joystick1.get_name()
      axes = joystick1.get_numaxes()
      for i in range( axes ):
          axis = joystick1.get_axis( i )
      buttons = joystick1.get_numbuttons()
      for i in range( buttons ):
          button = joystick1.get_button( i )
      hats = joystick1.get_numhats()
      for i in range( hats ):
          hat = joystick1.get_hat( i )
    
    if joystick_count > 1:
      joystick2.init()
      name = joystick2.get_name()
      axes = joystick2.get_numaxes()
      for i in range( axes ):
          axis = joystick2.get_axis( i )
      buttons = joystick2.get_numbuttons()
      for i in range( buttons ):
          button = joystick2.get_button( i )
      hats = joystick2.get_numhats()
      for i in range( hats ):
          hat = joystick2.get_hat( i )

    #Button list maps to the following on the game pad itself
    #get_button(0) = A button
    #get_button(1) = B button
    #get_button(2) = X button
    #get_button(3) = Y button
    #get_button(4) = LB button
    #get_button(5) = RB button
    #get_button(6) = back button
    #get_button(7) = start button
    #get_button(8) = left joystick downpress
    #get_button(9) = right joystick downpress

##Narrative: Determines which way a joystick's axis should face
##Preconditions: joystick(s) must not be None type
##Post conditions: Returns tuple of joystick's axes
def axround(axis):
    if axis > .5:
        return 1
    if axis < -.5:
        return -1

    return 0

##Narrative: Updates the axes of game pads
##Preconditions: Game pad must not be None type
##Post conditions: Updates game pad's axes
def getAxisDir(joy):
    #if joy stick does not exist, return 0,0 (false)
    if joy == None:
      return 0,0

    ax0 = joy.get_axis(0) #up down lanalog
    ax1 = joy.get_axis(1) #left right lanalog
    ax2 = joy.get_axis(2) #triggers
    ax3 = joy.get_axis(3) #up down ranalog
    ax4 = joy.get_axis(4) #left right ranalog

    ax0 = axround(ax0)
    ax1 = axround(ax1)
    ax2 = axround(ax2)
    ax3 = axround(ax3)
    ax4 = axround(ax4)

    return (ax0, ax1)

##Narrative: Moves up based on D-Pad or joystick
##Preconditions: Game pad must not be None type
##Post conditions: Returns true for moving upwards
def joyUp(joy):
    if joy == None:
        return False
    if joy.get_hat(0) == (0, 1) or getAxisDir(joy) == (0, -1):
        return True
    return False

##Narrative: Moves up based on D-Pad or joystick
##Preconditions: Game pad must not be None type
##Post conditions: Returns true for moving downwards
def joyDown(joy):
    if joy == None:
        return False
    if joy.get_hat(0) == (0, -1) or getAxisDir(joy) == (0, 1):
        return True
    return False

##Narrative: Moves up based on D-Pad or joystick
##Preconditions: Game pad must not be None type
##Post conditions: Returns true for moving right
def joyRight(joy):
    if joy == None:
        return False
    if joy.get_hat(0) == (1, 0) or getAxisDir(joy) == (1,0):
        return True
    return False

##Narrative: Moves up based on D-Pad or joystick
##Preconditions: Game pad must not be None type
##Post conditions: Returns true for moving left
def joyLeft(joy):
    if joy == None:
        return False
    if joy.get_hat(0) == (-1, 0) or getAxisDir(joy) == (-1,0):
        return True
    return False