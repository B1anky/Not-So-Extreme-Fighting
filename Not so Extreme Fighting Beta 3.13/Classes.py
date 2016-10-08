from pygame import *
import Health

SCREEN_WIDTH=1000
SCREEN_HEIGHT=600
##healthBar = Health.HealthBar()
##powerBar = Health.PowerBar()
##timer = Health.Timer()

#Class for creating Sprites
    #Class for creating Sprites
class sprite:
    def __init__(self,name,spriteSheet,spriteLeft,spriteRight,spriteTop,\
        spriteBottom,scale,adjustX,adjustY):
        self.Name = name
        self.spriteSheet = spriteSheet
        self.Left = spriteLeft
        self.Right = spriteRight
        self.Top = spriteTop
        self.Bottom = spriteBottom
        self.Scale = scale
        self.Width = self.Right-self.Left
        self.Height = self.Bottom-self.Top
        self.spriteSheet.set_clip(Rect(self.Left,self.Top,self.Width,self.Height))
        self.Picture = self.spriteSheet.subsurface(self.spriteSheet.get_clip())
        self.ScaledWidth = self.Width * self.Scale
        self.ScaledHeight = self.Height * self.Scale
        self.Picture = transform.scale(self.Picture,\
            (self.ScaledWidth,self.ScaledHeight))
        self.adjustX = adjustX
        self.adjustY = adjustY

    ##Narrative: Makes sprite Scale times bigger
    ##Preconditions: Initialize scale, width, height, and picture
    ##Post conditions: Sprite is enlarged or minimized based on preferences
    def scale(self,scale):
        self.Scale = scale
        self.ScaledWidth = self.Width * self.Scale
        self.ScaledHeight = self.Height * self.Scale
        self.Picture = transform.scale(self.Picture,\
            (self.ScaledWidth,self.ScaledHeight))


#===============================================================================
#===============================================================================

#Class for creating chatacters
class Character:
    def __init__(self,idleAnimList,walkAnimList,\
                 startStopAnimList,\
                 jumpAnimList,dashAnimList,attack1AnimList,\
                 drawX,spriteDefault,animTimer,walkAnimCtr,\
                 walkAnimCount,idleAnimCtr,idleAnimCount,\
                 startStopAnimCtr,startStopAnimCount,\
                 jumpAnimCtr,jumpAnimCount,dashAnimCtr,\
                 dashAnimCount,attack1AnimCtr,attack1AnimCount,\
                 face,widestSprite,\
                 tallestSprite,speed,maxSpeed,rightSpeed,\
                 leftSpeed,upSpeed,downSpeed,x,y,\
                 jumps,jumpHeight,canLeaveScreen,\
                 isOffBottom,isOffTop,isOffRight,\
                 isOffLeft,isOffScreen,\
                 status,isOn,attackTime,\
                 name,speedStat,power,maxPower,\
                 damageStat,isCrouched,who):
    
        #Sprite Lists
        self.idleAnimList = idleAnimList
        self.walkAnimList = walkAnimList
        self.startStopAnimList = startStopAnimList
        self.jumpAnimList = jumpAnimList
        self.dashAnimList = dashAnimList
        self.attack1AnimList = attack1AnimList

        #Animation
        self.drawX = drawX
        self.sprite = spriteDefault
        self.animTimer = animTimer
        self.walkAnimCtr = walkAnimCtr
        self.walkAnimCount = walkAnimCount
        self.idleAnimCtr = idleAnimCtr
        self.idleAnimCount = idleAnimCount
        self.startStopAnimCtr = startStopAnimCtr
        self.startStopAnimCount = startStopAnimCount
        self.jumpAnimCtr = jumpAnimCtr
        self.jumpAnimCount = jumpAnimCount
        self.dashAnimCtr = dashAnimCtr
        self.dashAnimCount = dashAnimCount
        self.attack1AnimCtr = attack1AnimCtr
        self.attack1AnimCount = attack1AnimCount
        self.face = face
        self.widestSprite = widestSprite
        self.tallestSprite = tallestSprite

        #Movement
        self.speed = 1
        self.maxSpeed = maxSpeed
        self.rightSpeed = rightSpeed
        self.leftSpeed = leftSpeed
        self.upSpeed = upSpeed
        self.downSpeed = downSpeed
        self.dy = (self.upSpeed - self.downSpeed)
        self.dx = (self.leftSpeed - self.rightSpeed)
        self.x = x
        self.y = y
        self.jumps = jumps
        self.jumpsLeft = self.jumps
        self.jumpHeight = jumpHeight
        self.canLeaveScreen = canLeaveScreen
        self.isOffBottom = isOffBottom
        self.isOffTop = isOffTop
        self.isOffRight = isOffRight
        self.isOffLeft = isOffLeft
        self.isOffScreen = isOffScreen
        self.status = status
        self.isOn = isOn
        self.attackTime = attackTime
        self.attackTimeLeft = 0

        #Stats
        self.name = name
        self.speedStat = speedStat
        self.power = power
        self.maxPower = maxPower
        self.damageStat = damageStat
        self.isCrouched = isCrouched
        self.who = who
        
    ##Narrative: Character will be able to move right
    ##Preconditions: Speed attributes must be initialized
    ##Post conditions: Character is able to walk right based
    ## on their unique walk speed
    def moveRight(self):
        if self.rightSpeed < self.maxSpeed:
            self.rightSpeed += (self.speedStat * self.speed)

    ##Narrative: Character will be able to move left
    ##Preconditions: Speed attributes must be initialized
    ##Post conditions: Character is able to walk left based on
    ## their unique walk speed
    def moveLeft(self):
        if self.leftSpeed < self.maxSpeed:
            self.leftSpeed += (self.speedStat * self.speed)

    ##Narrative: Character is able to jump
    ##Preconditions: Initialize jump attributes
    ##Post conditions: Character is able to jump up to two times
    def jump(self):
        if self.isOn == "ground" or self.jumpsLeft > 0:
            self.jumpAnimCount = 0
            self.downSpeed = 0
            self.upSpeed = self.jumpHeight
            self.y -= 1
            self.jumpsLeft -= 1
            self.isOn = "nothing"

    ##Narrative:Character is able to dash left based on character direction
    ##Preconditions: Initialize speed, status, and power
    ##Post conditions: 25 power is used to dash left
    def leftDash(self):
        if self.status != "jumping" and self.power >= 25:
            self.power -= 25
            self.rightSpeed = 0
            self.upSpeed = 0
            self.downSpeed = 0
            self.status = "dashing"
            self.leftSpeed = 40

    ##Narrative:Character is able to dash right basedon character direction
    ##Preconditions: Initialize speed, status, and power
    ##Post conditions: 25 power is used to dash right
    def rightDash(self):
        if self.status != "jumping" and self.power >= 25:
            self.power -= 25
            self.rightSpeed = 0
            self.upSpeed = 0
            self.downSpeed = 0
            self.status = "dashing"
            self.rightSpeed = 40

    ##Narrative: Character is able to attack
    ##Preconditions: Attack attributes must be initialized
    ##Post conditions: Character attacks, 25 power is used
    def attack(self):
        if self.power - 25 >= 0 and self.attackTimeLeft <= \
        self.attackTime/3:
            if self.status != "dashing":
                self.power -= 25
                self.status = "attacking"
                self.attackTimeLeft = self.attackTime
                self.attack1AnimCtr = 0
                self.attack1AnimCount = 0

    ##Narrative: Gravity allows for user to fall back into place
    ##Preconditions: Initialize up and down speeds
    ##Post conditions: Characters lands after jumping
    def gravity(self):
        if self.isOn == "nothing" and self.status != "dashing":
            if self.downSpeed < 20:
                self.downSpeed += 1    
            elif self.upSpeed > 0:
                self.upSpeed -= 1

    ##Narrative: Slows the player down after a key is left go of
    ##Preconditions: Initialize speed attributes
    ##Post conditions: Rules for being on the ground or in the air are made
    def slowDown(self,playerList):
        #Rules for on ground or in air
        for item in playerList:
            if self.isOn == "ground" or self.isOn == "nothing":
                if item.pushingRight == False:
                    if self.rightSpeed > 0:
                        self.rightSpeed -= 1
                if item.pushingLeft == False:
                    if self.leftSpeed > 0:
                        self.leftSpeed -=1

    ##Narrative: Makes the character replenish power every tick
    ##Preconditions: Initialize power and make full power 100
    ##Post conditions: Power is replenished 
    def generatePower(self):
        if self.power + 0. <= self.maxPower:
            self.power += 0.5
        else:
            self.power = 100
            
    ##Narrative: The player's status is updated depending on the key 
    ## or button pressed
    ##Preconditions: Initialized attributes concerning character movement
    ##Post conditions: Status is updated 
    def updateStatus(self):
        if self.attackTimeLeft > 0:
            self.attackTimeLeft -= 1
            self.status = "attacking"
        elif self.isOn == "nothing":
            self.status = "jumping"
        elif (self.rightSpeed == 0 and self.leftSpeed == 0) or \
            self.rightSpeed == self.leftSpeed:
            self.status = "idle"
        elif self.status != "dashing":
            if (self.rightSpeed != 0 or self.leftSpeed != 0) and \
                self.rightSpeed != self.leftSpeed:
                self.status = "walking"

    ##Narrative: Updates where the character is on
    ##Preconditions: Ground attribute
    ##Post conditions: Status is updated
    def updateIsOn(self):
        if self.isOn != "ground":
            if self.y > SCREEN_HEIGHT - self.tallestSprite.ScaledHeight:
                self.isOn = "ground"
                self.downSpeed = 0
                self.upSpeed = 0
                self.jumpsLeft = self.jumps

    ##Narrative: Handles all animation for characters
    ##Preconditions: Sprites and their attributes
    ##Post conditions: Character is animated
    def animation(self):
        
        #Walking Animation
        if self.status == "walking":

            #Start/Stop Animations
            if self.startStopAnimCount != (len(self.startStopAnimList)):
                self.sprite=self.startStopAnimList[self.startStopAnimCount]
                self.startStopAnimCtr += 1
                if self.startStopAnimCtr == self.animTimer:
                    self.startStopAnimCount += 1
                    self.startStopAnimCtr = 0
            else:
                self.sprite = self.walkAnimList[self.walkAnimCount]
                self.walkAnimCtr += 1
                if self.walkAnimCtr == self.animTimer:
                    self.walkAnimCount += 1
                    if self.walkAnimCount > (len(self.walkAnimList) - 1):
                        self.walkAnimCount = 0
                    self.walkAnimCtr = 0

        #Idle Animation
        elif self.status == "idle":
            self.startStopAnimCount = 0
            self.sprite = self.idleAnimList[self.idleAnimCount]
            self.idleAnimCtr += 1
            if self.idleAnimCtr/2 == self.animTimer:
                self.idleAnimCount += 1
                if self.idleAnimCount > (len(self.idleAnimList) - 1):
                    self.idleAnimCount = 0
                self.idleAnimCtr = 0

        #Jumping Animation
        elif self.status == "jumping":
            self.sprite = self.jumpAnimList[self.jumpAnimCount]
            self.jumpAnimCtr += 1
            if self.jumpAnimCtr == self.animTimer:
                self.jumpAnimCount += 1
                if self.jumpAnimCount > (len(self.jumpAnimList) - 1):
                    self.jumpAnimCount -= 1
                self.jumpAnimCtr = 0

        #Dashing Animation
        elif self.status == "dashing":
            self.sprite = self.dashAnimList[self.dashAnimCount]
            self.dashAnimCtr += 1
            if self.dashAnimCtr == self.animTimer*2:
                self.dashAnimCount += 1
                if self.dashAnimCount > (len(self.dashAnimList) - 1):
                    self.dashAnimCount -= 1
                self.dashAnimCtr = 0

        #Attacking Animation
        elif self.status == "attacking":
            self.sprite = self.attack1AnimList[self.attack1AnimCount]
            self.attack1AnimCtr += 1
            if self.attack1AnimCtr == self.animTimer:
                self.attack1AnimCount += 1
                if self.attack1AnimCount > (len(self.attack1AnimList) - 1):
                    self.attack1AnimCount -= 1
                self.attack1AnimCtr = 0

        if self.status != "dashing":
            self.dashAnimCount = 0
            self.dashAnimCtr = 0
                
    ##Narrative: Handles possibility of character walking off the screen
    ##Preconditions: Window height and width
    ##Post conditions:Character remains within the boundaries of the window
    def updateIsOffScreen(self):

        #Right of screen
        if (self.x + self.widestSprite.ScaledWidth)+self.dx>= SCREEN_WIDTH:
            self.isOffRight = True
        else:
            self.isOffRight = False

        #Left of screen
        if self.x + self.dx <= 0:
            self.isOffLeft = True
        else:
            self.isOffLeft = False

        #Top of screen
        if self.y + self.dy < 0:
            self.isOffTop = True
        else:
            self.isOffTop = False

        #Bottom of screen
        if (self.y + self.tallestSprite.ScaledHeight) + self.dy > \
            SCREEN_HEIGHT:
            self.isOffBottom = True
        else:
            self.isOffBottom = False

        #Update isOffSceen
        if self.isOffRight == True or self.isOffLeft == True or \
            self.isOffTop == True or self.isOffBottom == True:
            self.isOffScreen = True
        else:
            self.isOffScreen = False
            
    ##Narrative: Updates the coordinates of the character
    ##Preconditions: Coordinate attributes
    ##Post conditions: Collision is updated and accounted for
    def updateCoords(self,system,playerList):

        #Updates whether or not the player is off the screen
        self.updateIsOffScreen()
        
        #Update Cracters Colliding
        system.updateCharacterCollision(playerList)

        #Updates dx and dy
        self.dx = (self.rightSpeed - self.leftSpeed)
        self.dy = (self.upSpeed - self.downSpeed)

        #If character can go off the screen
        if self.canLeaveScreen == True:
            self.x += self.dx
            self.y += self.dy

        #If character can't go off the screen
        else:
            if self.isOffScreen == True:
                if self.isOffRight == True:
                    self.rightSpeed = 0
                elif self.isOffLeft == True:
                    self.leftSpeed = 0
                if self.isOffBottom == True:
                    self.downSpeed  = 0
                            
            #Updates dx and dy
            self.dx = (self.rightSpeed - self.leftSpeed)
            self.dy = (self.downSpeed - self.upSpeed)

            self.x += self.dx
            self.y += self.dy

    ##Narrative: Draws character onto the screen using their sprite images
    ##Preconditions: Character sprites
    ##Post conditions:Character is drawn on the specified window coordinate
    def draw(self,screen,bubble):          
        if self.face == "right":
            screen.blit(self.sprite.Picture,(self.x+self.sprite.adjustX,\
                self.y+self.sprite.adjustY))
        elif self.face == "left":
            if self.sprite.adjustX != 0:
                self.drawX = self.x - 100
            else:
                self.drawX = self.x
            screen.blit(transform.flip((self.sprite.Picture),True,False),\
                                (self.drawX,self.y+self.sprite.adjustY))
        if self.isCrouched == True:
          if self.power - 4 >= 0:
            self.power -= 0.50
            if self.who == "zero" or self.who == "captain":
                screen.blit(bubble,(self.x,self.y))
            elif self.who == "koopa":
                screen.blit(bubble,(self.x-40,self.y+100))
            elif self.who == "jade":
                screen.blit(bubble,(self.x-50,self.y-120))
          else:
            self.isCrouched = False
            self.power = 0
            
    ##Narrative: Runs through all character updates
    ##Preconditions: Attributes that need to be updated
    ##Post conditions: Character is updated
    def update(self,pushingPause,playerList,system,screen,healthBar,bubble):
      if pushingPause == False:
        self.generatePower()
        self.slowDown(playerList)
        self.updateStatus()
        system.updateFace(playerList)
        self.updateIsOn()
        self.gravity()
        self.updateCoords(system,playerList)
        self.animation()
      self.draw(screen,bubble)
      if pushingPause == False:
        system.damage(playerList,healthBar)

    def __str__(self):
        return("\n\nSprite Lists:"+\
               "\nidleAnimList: "+str(self.idleAnimList)+\
               "\nwalkAnimList: "+str(self.walkAnimList)+\
               "\nstartStopAnimList: "+str(self.startStopAnimList)+\
               "\njumpAnimList: "+str(self.jumpAnimList)+\

               "\n\nAnimation"+\
               "\nanimTimer: "+str(self.animTimer)+\
               "\nwalkAnimCtr: "+str(self.walkAnimCtr)+\
               "\nwalkAnimCount: "+str(self.walkAnimCount)+\
               "\nidleAnimCtr: "+str(self.idleAnimCtr)+\
               "\nidleAnimCount: "+str(self.idleAnimCount)+\
               "\njumpAnimCtr: "+str(self.jumpAnimCtr)+\
               "\njumpAnimCount: "+str(self.jumpAnimCount)+\
               "\ndashAnimCtr: "+str(self.dashAnimCtr)+\
               "\ndashAnimCount: "+str(self.dashAnimCount)+\
               "\nface: "+str(self.face)+\
               "\nwidestSprite: "+str(self.widestSprite)+\
               "\ntallestSprite: "+str(self.tallestSprite)+\
               "\ncurrentSprite: "+str(self.sprite.Name)+\

               "\n\nMovement"+\
               "\nspeed: "+str(self.speed)+\
               "\nmaxSpeed: "+str(self.maxSpeed)+\
               "\nrightSpeed: "+str(self.rightSpeed)+\
               "\nleftSpeed: "+str(self.leftSpeed)+\
               "\nupSpeed: "+str(self.upSpeed)+\
               "\ndownSpeed: "+str(self.downSpeed)+\
               "\ndy: "+str(self.dy)+\
               "\ndx: "+str(self.dx)+\
               "\nx: "+str(self.x)+\
               "\ny: "+str(self.y)+\
               "\njumps: "+str(self.jumps)+\
               "\njumpsLeft: "+str(self.jumpsLeft)+\
               "\ncanLeaveScreen: "+str(self.canLeaveScreen)+\
               "\nisOffBottom: "+str(self.isOffBottom)+\
               "\nisOffTop: "+str(self.isOffTop)+\
               "\nisOffRight: "+str(self.isOffRight)+\
               "\nisOffLeft: "+str(self.isOffLeft)+\
               "\nstatus: "+str(self.status)+\
               "\nisOn: "+str(self.isOn)+\

               "\n\nStats"+\
               "\nname: "+str(self.name))

#===============================================================================
#===============================================================================

#Player class
class Player(Character):

    def __init__(self,number,character="",pushingRight=False,\
                pushingLeft=False,pushingUp=False,pushingDown=False,\
                pushingRightDash=False,pushingLeftDash=False,pushingAttack1=False):
        self.number = number
        self.character = character
        self.pushingRight = pushingRight
        self.pushingLeft = pushingLeft
        self.pushingUp = pushingUp
        self.pushingDown = pushingDown
        self.pushingRightDash = pushingRightDash
        self.pushingLeftDash = pushingLeftDash
        self.pushingAttack1 = pushingAttack1

#===============================================================================
#===============================================================================

 #System Class: handles all collisions and ui
class System:

    def __init__(self,fontList=["Digital Desolation",24]):
        self.fontList = fontList
        self.defaultFont = font.SysFont(self.fontList[0],self.fontList[1])
        self.alphSurface = 0
        self.alphaText = 0
        self.mainLoop = True
        self.result = "none"

    ##Narrative: Draws text of player 1 and player 2 above their head
    ##Preconditions: Player 1 and Player 2 are drawn to screen
    ##Post conditions: Blits the text to the player's head
    def updateHalo(self,playerList,screen):
        for item in playerList:
            if item.character.who == "zero" or item.character.who == "captain":
                screen.blit(self.defaultFont.render("Player "+str(item.number),\
                    100,(255,255,255)),(item.character.x+50,item.character.y-25))
            elif item.character.who == "jade":
                screen.blit(self.defaultFont.render("Player "+str(item.number),\
                    100,(255,255,255)),(item.character.x+5,item.character.y-145))
            elif item.character.who == "koopa":
                screen.blit(self.defaultFont.render("Player "+str(item.number),\
                    100,(255,255,255)),(item.character.x+50,item.character.y+130))

    ##Narrative: Updates the direction the character is facing 
    ##Preconditions: The character for Player 1 and Player 2
    ##Post conditions: Character direction is changed depending 
    ## on their side of the screen
    def updateFace(self,playerList):
        player1 = playerList[0]
        player2 = playerList[1]
        if player1.character.x > player2.character.x:
            player1.character.face = "left"
            player2.character.face = "right"
        else:
            player1.character.face = "right"
            player2.character.face = "left"

    ##Narrative: Damage calculator
    ##Preconditions: Character attack sprites such as punches or kicks
    ##Post conditions: Damage is inflicted; if player is blocking, 
    ## turn damage into weaker "chip" damage
    def damage(self,playerList,healthBar):
        player1=playerList[0]
        player2=playerList[1]
        if player1.character.attackTimeLeft > 0:
            damageDone = player1.character.damageStat
            if player2.character.isCrouched == True:
                damageDone *= .1
            if player1.character.face == "right":
                if player1.character.x+\
                player1.character.sprite.ScaledWidth > \
                player2.character.x and player1.character.y \
                + player1.character.sprite.ScaledHeight + \
                player1.character.dy > player2.character.y and \
                player1.character.y + player1.character.dy < \
                player2.character.y + \
                player2.character.sprite.ScaledHeight:
                    healthBar.player2Dam(damageDone)
                    if player2.character.isCrouched == False:
                        player2.character.rightSpeed += 2
            elif player1.character.face == "left":
                if player1.character.drawX < player2.character.x+\
                player2.character.sprite.ScaledWidth and \
                player1.character.y + \
                player1.character.sprite.ScaledHeight + \
                player1.character.dy > player2.character.y and \
                player1.character.y + player1.character.dy < \
                player2.character.y + \
                player2.character.sprite.ScaledHeight:
                    healthBar.player2Dam(damageDone)
                    if player2.character.isCrouched == False:
                        player2.character.leftSpeed += 2
        if player2.character.attackTimeLeft > 0:
            damageDone = player2.character.damageStat
            if player1.character.isCrouched == True:
                damageDone *= .1
            if player2.character.face == "right":
                if player2.character.x+\
                player2.character.sprite.ScaledWidth > \
                player1.character.x and player2.character.y \
                + player2.character.sprite.ScaledHeight + \
                player2.character.dy > player1.character.y and \
                player2.character.y + player2.character.dy < \
                player1.character.y + \
                player1.character.sprite.ScaledHeight:
                    healthBar.player1Dam(damageDone)
                    if player1.character.isCrouched == False:
                        player1.character.rightSpeed += 2
            elif player2.character.face == "left":
                if player2.character.drawX < \
                player1.character.x+player1.character.sprite.ScaledWidth\
                 and player2.character.y + \
                 player2.character.sprite.ScaledHeight + \
                 player2.character.dy > player1.character.y and \
                 player2.character.y + player2.character.dy < \
                 player1.character.y + \
                 player1.character.sprite.ScaledHeight:
                    healthBar.player1Dam(damageDone)
                    if player1.character.isCrouched == False:
                        player1.character.leftSpeed += 2

    ##Narrative: Updates character collision
    ##Preconditions: Player 1 and Player 2 coordinates
    ##Post conditions: Sprites don't phase through each other
    def updateCharacterCollision(self,playerList):
        player1 = playerList[0]
        player2 = playerList[1]
        if player1.character.x + player1.character.sprite.ScaledWidth\
            + player1.character.dx > player2.character.x and \
            player1.character.x + player1.character.dx < player2.character.x\
            + player2.character.sprite.ScaledWidth:
            if player1.character.y + player1.character.sprite.ScaledHeight\
                + player1.character.dy > player2.character.y and \
                player1.character.y + player1.character.dy < \
                player2.character.y + player2.character.sprite.ScaledHeight: 
                if player1.character.face == "right":
                  player1.character.rightSpeed = 0
                if player1.character.face == "left":
                  player1.character.leftSpeed = 0
        if player2.character.x + player2.character.sprite.ScaledWidth\
            + player2.character.dx > player1.character.x and \
            player2.character.x + player2.character.dx < \
            player1.character.x + player1.character.sprite.ScaledWidth:
            if player2.character.y + player2.character.sprite.ScaledHeight\
                + player2.character.dy > player1.character.y and \
                player2.character.y + player2.character.dy < \
                player1.character.y + player1.character.sprite.ScaledHeight: 
                if player2.character.face == "right":
                  player2.character.rightSpeed = 0
                if player2.character.face == "left":
                  player2.character.leftSpeed = 0
    
    ##Narrative: Starts the beginning of the end of the game
    ##Preconditions: Player 1 or Player 2 health must be 0 or below
    ##Post conditions: Calls fadeToBlack() function
    def gameWinScreen(self,healthBar,system,player1Win,player2Win,screen):
      if healthBar.p2H < healthBar.p1H-200:
          self.result = "p1"
      else:
          self.result = "p2"
      system.fadeInText(player1Win,player2Win,screen)

    ##Narrative: Creates the end game screen
    ##Preconditions: gameWinScreen() function calls this
    ##Post conditions: Increases opacity of winScreen to block main screen
    def fadeInText(self,player1Win,player2Win,screen):
        if self.alphaText < 255:
            self.alphaText += 2.5
        else:
            time.delay(2000)
            self.mainLoop = False
        if self.result == "p1":
          player1Win.set_alpha(self.alphaText)
          screen.blit(player1Win,(0,0))
        elif self.result == "p2":
          player2Win.set_alpha(self.alphaText)
          screen.blit(player2Win,(0,0))
