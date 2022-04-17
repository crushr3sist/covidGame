# random generation
import random
from pygame_functions import *
import spriteInit


def npcTurn(level, active, houseX, houseY, patients):
    # rolls dice, likeliness works according to difficulty
    if random.randint(1, 6) >= level + 2:
        # rolls dice, spawns a sick patient to the rolled position
        spawn = random.randint(0, 5)
        # if statement checks if the sprite is already shown
        if active[spawn] == 0:
            # the rest of these statements are used for mapping the sick patient to the X and Y position that it is supposed to be assigned to
            if spawn < 3:
                spawnX = 0
            else:
                spawnX = 1

            if spawn < 3:
                spawnY = spawn

            else:
                spawnY = spawn - 3
            # tells the program that the patient is now active, gives the sprite an age, and shows it in its assigned position
            active[spawn] = 1
            moveSprite(patients[spawn], houseX[spawnX] + 25, houseY[spawnY] + 25, 1)
            showSprite(patients[spawn])
    return active, patients


# class of objects, made for patients, purpose is categorization
class patientControlling:
    # made for giving patients age
    def ageingPatients(active, age):
        if active == 1:
            age += 1
        return active, age

    # know when patients are dead
    def deadPatient(deadAge, deadPatient, deadActive, lifeAmt):
        if deadAge > 19:
            deadAge = 0
            deadActive = 0
            hideSprite(deadPatient)
            lifeAmt -= 1
        return deadAge, deadActive, lifeAmt

    def healPatient(doc, patients, masks, active, age, score):
        if touching(doc, patients) and masks > 0:
            # if the patients are touching the doctor, and he has enough masks, he will cure the patient
            hideSprite(patients)
            masks -= 1
            active = 0
            age = 0
            score += 100
        return doc, patients, masks, active, age, score
