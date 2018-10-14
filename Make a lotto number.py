'''
Title: This Program will create lottery numbers to use
Author: Riley Carpenter
Other Projects Used: Lotto Chance by Riley Carpenter
'''
import sys
import os
import random
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
def clear_screen():    
    os.system(clearorcls)

clear_screen()
desirednoballchance = float(input("Without a megaball what do you want your chances of winning to be? "))
desiredballchance = float(input("With a megaball what do you want your chances of winning to be? "))
noballchance = 0.0
ballchance = 0.0

while desirednoballchance != noballchance and desiredballchance != ballchance:
    firstnumber = random.randint(1,70)
    secondnumber = random.randint(1,70)
    while secondnumber == firstnumber:
        secondnumber = random.randint(1,70)
    thirdnumber = random.randint(1,70)
    while thirdnumber == secondnumber or thirdnumber == firstnumber:
        thirdnumber = random.randint(1,70)
    fourthnumber = random.randint(1,70)
    while fourthnumber == thirdnumber or fourthnumber == secondnumber or fourthnumber == firstnumber:
        fourthnumber = random.randint(1,70)
    fifthnumber = random.randint(1,70)
    while fifthnumber == fourthnumber or fifthnumber == thirdnumber or fifthnumber == secondnumber or fifthnumber == firstnumber:
        fifthnumber = random.randint(1,70)
    megaballnumber = random.randint(1,25)
    totalnumbers1 = 0
    totalnumbers = 0
    totalnumbers2 = 1
    firstguess = random.randint(1,76)
    secondguess = random.randint(1,76)
    thirdguess = random.randint(1,76)
    fourthguess = random.randint(1,76)
    fifthguess = random.randint(1,76)
    megaguess = random.randint(1,51)


    while firstguess != firstnumber and secondguess != secondnumber and thirdguess != thirdnumber and fourthguess != fourthnumber and fifthnumber != fifthguess:
        firstguess = random.randint(1,76)
        secondguess = random.randint(1,76)
        thirdguess = random.randint(1,76)
        fourthguess = random.randint(1,76)
        fifthguess = random.randint(1,76)
        megaguess = random.randint(1,51)
        totalnumbers1 += 1
        totalnumbers += 1
        print("Times you would have played currently is",totalnumbers)
        clear_screen()
    firstguess = random.randint(1,76)
    secondguess = random.randint(1,76)
    thirdguess = random.randint(1,76)
    fourthguess = random.randint(1,76)
    fifthguess = random.randint(1,76)
    megaguess = random.randint(1,51)
    while firstguess != firstnumber and secondguess != secondnumber and thirdguess != thirdnumber and fourthguess != fourthnumber and fifthnumber != fifthguess and megaguess != megaballnumber:
        firstguess = random.randint(1,76)
        secondguess = random.randint(1,76)
        thirdguess = random.randint(1,76)
        fourthguess = random.randint(1,76)
        fifthguess = random.randint(1,76)
        megaguess = random.randint(1,51)
        totalnumbers2 += 1
        totalnumbers += 1
        print("Times you would have played currently is",totalnumbers)
        clear_screen()
    else:
        clear_screen()
        if totalnumbers1 == 0:
            totalnumbers1 = 1
        if totalnumbers2 == 0:
            totalnumbers2 = 1
        noballchance = (1 / totalnumbers1) * 100
        ballchance = (1 / totalnumbers2) * 100
else:
    print("The numbers you need to win at",str(desirednoballchance) + "% chance without a megaball are:")
    print(firstnumber,secondnumber,thirdnumber,fourthnumber,fifthnumber)
    print("And the megaball number you would need to get a",str(desiredballchance) + "% chance is:")
    print(megaballnumber)
    print("")
    print("Good luck and have fun!")
