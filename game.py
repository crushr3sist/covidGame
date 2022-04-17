from pygame_functions import *


import spriteInit
import yourturn
import random
import npcTurn
import time
import mainMenu

mainMenu.menuScreen()

windowX = 1920
windowY = 1080
screenSize(windowX, windowY, 0, -10)


lifeImg = [makeSprite("life.png"), makeSprite("life.png"), makeSprite("life.png")]


driver = spriteInit.spriteRef()


setBackgroundImage("grid11.jpg")


spriteInit.spriteInit()


pygame.mouse.set_visible(False)


moveSprite(driver.doctor, driver.docX, driver.docY, 1)
showSprite(driver.doctor)
moveSprite(driver.maskBox, driver.docX + 187, driver.docY - 20, 1)
showSprite(driver.maskBox)


maskCount = makeLabel(
    "Mask Amount: " + str(driver.maskNum),
    24,
    0,
    0,
    fontColour="black",
    font="Arial",
    background="clear",
)

scoreCount = makeLabel(
    "Score: " + str(driver.score),
    24,
    0,
    24,
    fontColour="black",
    font="Arial",
    background="clear",
)

difficultyCount = makeLabel(
    "Level: " + str(driver.level),
    24,
    (windowX / 3) * 2,
    0,
    fontColour="black",
    font="Arial",
    background="clear",
)

showLabel(maskCount)
showLabel(scoreCount)
showLabel(difficultyCount)


oneTimeLevel2Background = True
oneTimeLevel3Background = True


run = True
while run:
    for x in range(3):
        hideSprite(lifeImg[x])
    for x in range(driver.lifeAmount):
        moveSprite(lifeImg[x], 10 + (50 * x), 70, 1)
        showSprite(lifeImg[x])
        if x == driver.lifeAmount:
            try:
                hideSprite(lifeImg[x])
            except:
                showSprite(lifeImg[x - 1])

    (driver.level, oneTimeLevel2Background, oneTimeLevel3Background) = yourturn.levelUp(
        driver.level, driver.score, oneTimeLevel2Background, oneTimeLevel3Background
    )

    (driver.docX, driver.docY, driver.turnPassed, driver.doctor) = yourturn.movement(
        driver.docX, driver.docY, driver.velocity, driver.turnPassed, driver.doctor
    )

    moveSprite(driver.doctor, driver.docX, driver.docY, 1)
    showSprite(driver.doctor)

    (driver.patientActive, driver.patients) = npcTurn.npcTurn(
        driver.level,
        driver.patientActive,
        driver.houseX,
        driver.houseY,
        driver.patients,
    )

    (driver.maskNum, driver.score) = yourturn.maskUsage(
        driver.maskNum, driver.score, driver.doctor, driver.maskBox
    )
    for i in range(6):
        (
            driver.patientAge[i],
            driver.patientActive[i],
            driver.lifeAmount,
        ) = npcTurn.patientControlling.deadPatient(
            driver.patientAge[i],
            driver.patients[i],
            driver.patientActive[i],
            driver.lifeAmount,
        )
        (
            driver.patientActive[i],
            driver.patientAge[i],
        ) = npcTurn.patientControlling.ageingPatients(
            driver.patientActive[i], driver.patientAge[i]
        )
        (
            driver.doctor,
            driver.patients[i],
            driver.maskNum,
            driver.patientActive[i],
            driver.patientAge[i],
            driver.score,
        ) = npcTurn.patientControlling.healPatient(
            driver.doctor,
            driver.patients[i],
            driver.maskNum,
            driver.patientActive[i],
            driver.patientAge[i],
            driver.score,
        )
    if driver.lifeAmount < 1:
        hideSprite(lifeImg[0])
        endgame = makeLabel(
            "Game Over",
            142,
            windowX / 4,
            windowY / 10,
            fontColour="red",
            font="Arial",
            background="black",
        )
        showLabel(endgame)
        time.sleep(5)
        run = False

    changeLabel(maskCount, "Mask Amount: " + str(driver.maskNum))
    changeLabel(scoreCount, "Score: " + str(driver.score))
    changeLabel(difficultyCount, "Level: " + str(driver.level))
    time.sleep(0.1)

end()
