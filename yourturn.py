from pygame_functions import *

# imports sprite data
import spriteInit

# loop intakes player movement variables and processes keypresses
def movement(x, y, velocity, turnPassed, doctor):
    leftdoc = makeImage("doctor.png")
    # allows intake from spriteInit variables
    driver = spriteInit.spriteRef()
    # signifies beginning of while loop
    done = 0
    while done == 0:
        # if esc is pressed, the program ends
        if keyPressed("esc"):
            end()
        # if any of the following arrow keys are pressed, the character moves to the respected direction
        if keyPressed("up"):
            y -= velocity
            done = 1
        if keyPressed("down"):
            y += velocity
            done = 1
        if keyPressed("left"):
            x -= velocity
            done = 1

        if keyPressed("right"):
            x += velocity
            done = 1

    # tells the program that a turn has passed
    turnPassed += 1
    # returns the x and y variables back to the main loop to move the player
    return x, y, turnPassed, doctor


# function for mask pickup
def maskUsage(maskNum, score, doc, maskBox):
    if touching(doc, maskBox):
        # adds 2 to the mask amount
        maskNum += 2
    # returns the mask amount to the main loop along with score
    return maskNum, score


def levelUp(level, score, oneTime2, oneTime3):
    if score <= 900:
        level = 1

    if score > 900:
        level = 2
        if oneTime2 == True:
            setBackgroundImage("grid11-2.jpg")
            oneTime2 = False

    if score > 2900:
        level = 3
        if oneTime3 == True:
            setBackgroundImage("grid11-3.jpg")
            oneTime3 = False

    return level, oneTime2, oneTime3
