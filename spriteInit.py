#opening of sprites
from pygame_functions import *

#spawns bouses at the specific locations according to the houseX, houseY locations
def spriteInit():
    driver = spriteRef()
    house = [makeSprite('house.png'), makeSprite('house.png'), makeSprite('house.png'), makeSprite('house.png'), makeSprite('house.png'), makeSprite('house.png')]
    #changes the x and y variables and maps the houses accordingly
    for xConfig in range(2):
        if xConfig==1:  
            x = 3
        else:
            x = 0
        for yConfig in range(3):
            yConfig-=1
            moveSprite(house[yConfig+x], driver.houseX[xConfig], driver.houseY[yConfig], 1)
    #shows houses after spawned into position
    for i in range (6):
            i-=1
            showSprite(house[i+1])

#all of the variables in the program
class spriteVars:
    def __init__(self):
        #velocity for the game
        self.velocity = 177
        #doctor sprite
        self.doctor = makeSprite('doctor.png')
        #doc x and y position (default)
        self.docX = 424
        self.docY = 135
        #house x and y positions
        self.houseX = [955,1309]
        self.houseY = [123,477,831]
        #patient sprites
        self.patients = [makeSprite('patient.png'),makeSprite('patient.png'),makeSprite('patient.png'),makeSprite('patient.png'),makeSprite('patient.png'), makeSprite('patient.png')]
        #mask box that player collects masks from
        self.maskBox = makeSprite('box11.png')
        #amount of masks the character is holding
        self.maskNum = 0
        #life amount of the character
        self.lifeAmount = 3
        #score
        self.score = 0
        #tracks turns passed
        self.turnPassed = 0
        #patient age
        self.patientAge = [0,0,0,0,0,0]
        #track if the patient is active
        self.patientActive = [0,0,0,0,0,0]
        #initiates the levels, starts at 1
        self.level = 1

#this function made for referring to spriteVars variables
def spriteRef():
    return spriteVars()

#ignore this function, it is work in progress
#def spriteChange(left, right, spriteL, spriteR):
#    if left:
#        hideSprite(spriteR)
#        showSprite(spriteL)
#        pos = "left"
#    if right:
#        hideSprite(spriteL)
#        showSprite(spriteR)
#        pos = "right"
#    return spriteL, spriteR, pos
    