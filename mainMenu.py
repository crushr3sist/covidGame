# title screen

from pygame_functions import *
import time

# function made for killing sprites
def kill(box, doc, house, patient, logo, play, quitt):
    killSprite(box)
    killSprite(doc)
    killSprite(house)
    killSprite(patient)
    killSprite(logo)
    killSprite(play)
    killSprite(quitt)


# main menu screen
def menuScreen():
    # set screen dimensions
    screenSize(1000, 1000)
    # set background to cyan blue
    setBackgroundColour((2, 204, 214))
    # make all of the showcase sprites for the interface
    box = makeSprite("box11.png")
    doc = makeSprite("doctor.png")
    house = makeSprite("house.png")
    patient = makeSprite("patient.png")
    logo = makeSprite("bruh.png")
    play = makeSprite("play.png")
    quitt = makeSprite("quit.png")

    # move the showcase sprites into position
    moveSprite(logo, 500, 50, 1)
    moveSprite(box, 800, 250, 1)
    moveSprite(doc, 200, 250, 1)
    moveSprite(patient, 200, 750, 1)
    moveSprite(house, 800, 750, 1)
    moveSprite(play, 500, 350, 1)
    moveSprite(quitt, 500, 650, 1)

    # transform the sprites to appear properly
    transformSprite(logo, 0, 0.75)
    transformSprite(box, -10, 1)
    transformSprite(doc, -10, 1)
    transformSprite(patient, -10, 1)
    transformSprite(house, -10, 1)

    # make the sprites appear
    showSprite(box)
    showSprite(doc)
    showSprite(house)
    showSprite(patient)
    showSprite(logo)
    showSprite(play)
    showSprite(quitt)

    # preparing labels for instructions, sprites to help explain
    four = makeLabel(
        "The further you go, the harder it gets!",
        50,
        50,
        650,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    three = makeLabel(
        "Cure patients that are sick by handing",
        50,
        50,
        500,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    two = makeLabel(
        "Collect masks by walking over the box",
        50,
        50,
        400,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    one = makeLabel(
        "Press the arrow keys to move",
        50,
        50,
        300,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    five = makeLabel(
        "them masks (walking over them)",
        50,
        50,
        550,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    six = makeLabel(
        "Instructions:",
        150,
        50,
        25,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    seven = makeLabel(
        "Press any key to continue",
        50,
        50,
        750,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    four2 = makeLabel(
        "If you leave the patients for",
        50,
        50,
        50,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    four3 = makeLabel(
        "too long, they die!",
        50,
        50,
        100,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    three2 = makeLabel(
        "If a patient dies, you lose a heart",
        50,
        50,
        200,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    two2 = makeLabel(
        "Time is counted by movements, meaning",
        50,
        50,
        300,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )
    one2 = makeLabel(
        "you can decide your strategy to win!",
        50,
        50,
        350,
        fontColour="black",
        font="Helvetica",
        background="clear",
    )

    k = makeSprite("keys.png")
    p = makeSprite("patient.png")
    b = makeSprite("box11.png")

    # start loop
    run = True
    while run:
        # these for loops intend to have delay between the characters tilting
        # side to side, instead of using time.sleep
        for i in range(30):
            # this if statement causes intentional lag to not have them tilting insanely
            # fast
            if i == 29:
                print("Pay attention to the game window!")
            # tilt the sprites
            transformSprite(box, 20, 1)
            transformSprite(doc, 20, 1)
            transformSprite(patient, 20, 1)
            transformSprite(house, 20, 1)
            # if you press the quit button, the game ends
            if spriteClicked(quitt):
                end()
            # ends the main menu if you press play
            if spriteClicked(play):
                # kills sprites that arent needed anymore, optimising
                kill(box, doc, house, patient, logo, play, quitt)
                # ends loop
                run = False
                # breaks from for loop
                break
            # if esc is pressed, end the game
            if keyPressed("esc"):
                end()

        for i in range(30):
            # if statement to check if play has been pressed, in the last loop, the break
            # statement only breaks from that loop and goes into this one, this break
            # finally breaks from the menu
            if run == False:
                break
            if i == 29:
                print("Pay attention to the game window!")
            transformSprite(box, -20, 1)
            transformSprite(doc, -20, 1)
            transformSprite(patient, -20, 1)
            transformSprite(house, -20, 1)
            if spriteClicked(quitt):
                end()
            if spriteClicked(play):
                kill(box, doc, house, patient, logo, play, quitt)
                run = False
                break
            if keyPressed("esc"):
                end()

    # showing instructions
    showLabel(one)
    showLabel(two)
    showLabel(three)
    showLabel(four)
    showLabel(five)
    showLabel(six)

    # moving demo sprites into position
    moveSprite(k, 740, 320, 1)
    moveSprite(b, 875, 420, 1)
    moveSprite(p, 850, 580, 1)
    transformSprite(b, 0, 0.75)
    transformSprite(p, 0, 0.75)

    # showing sprites
    showSprite(k)
    showSprite(b)
    showSprite(p)

    # very simple loop so the player can read the instructions and play at their own pace
    run = True
    time.sleep(2)
    showLabel(seven)
    while run:
        if mousePressed() or keyPressed():
            run = False
    # killing not needed sprites
    killSprite(k)
    killSprite(b)
    killSprite(p)

    # killing off labels
    hideLabel(one)
    hideLabel(two)
    hideLabel(three)
    hideLabel(four)
    hideLabel(five)
    hideLabel(six)
    hideLabel(seven)

    # showing new instructions
    showLabel(one2)
    showLabel(two2)
    showLabel(three2)
    showLabel(four2)
    showLabel(four3)

    # another loop for new instructions
    run = True
    time.sleep(2)
    showLabel(seven)
    while run:
        if keyPressed() or mousePressed():
            run = False
    # hide rest of instructions
    hideLabel(one2)
    hideLabel(two2)
    hideLabel(three2)
    hideLabel(four2)
    hideLabel(four3)
    hideLabel(seven)
