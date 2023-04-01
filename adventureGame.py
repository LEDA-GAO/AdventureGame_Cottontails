import time
import random


def print_pause(strListToPrint):
    for strToPrint in strListToPrint:
        print(strToPrint)
        time.sleep(3)


def check_choice(choiceNumber):
    choiceCheck = input("(Please enter a number from 1 to "
                        + str(choiceNumber) + ")")
    while (not choiceCheck.isdigit()):
        print("You can only enter an integer. ")
        choiceCheck = input("(Please enter the number again).  ")
    while int(choiceCheck) < 1 or int(choiceCheck) > choiceNumber:
        print("You can only enter number from 1 to " + str(choiceNumber) + ".")
        choiceCheck = input("(Please enter the number again).  ")
    return int(choiceCheck)


def check_result(getFruit, happyEnding):
    if getFruit:
        if happyEnding:
            print_pause(["Happy Ending: ",
                         "You and your mate return successfully"
                         " and bring enough food!",
                         "Every is so happy and you both are seen"
                         " as hero/heroine!",
                         "You both are written to cottontail chronicle"
                         "as a hero/heroine!"])
        else:
            print_pause(["Tragedy Ending: ",
                         "Other rabbits enjoy the fruits. ",
                         "Everyone will remember you because of your"
                         " bravery sacrifice. ",
                         "You are written to cottontail chronicle as"
                         " a hero/heroine!"])
        reply = input("Would you like to play again? (y/n)")
        while reply != "y" and reply != "n":
            reply = input("Please enter again. Only y/n is accepted. ")
    else:
        print_pause(["Game Over"])
        reply = input("Would you like to play again? (y/n)")
        while reply != "y" and reply != "n":
            reply = input("Please enter again. Only y/n is accepted. ")
    return reply


def chance_caught(weightList):
    caught = random.choices([True, False], weights=weightList)
    return caught[0]


def grasslandIntro():
    senarioList = []
    senarioList.append("You are standing in an open grassland, "
                       "filled with grass and bushes with delicious fruit. ")
    senarioList.append("You really want to eat these fruits and share them "
                       "with your buddies. ")
    senarioList.append("It is a nice day and it seems like it is"
                       " quite peaceful around. "
                       "The only sound you can hear is some weak,"
                       " high yelping far away in the sky. ")
    senarioList.append("There are some bushes in front of you in a"
                       " distance about 15 meters. "
                       "The fruits on them look so delicious!")
    senarioList.append("There is a rabbit hole on your right side in"
                       " a distance about 10 meters. ")
    senarioList.append("Enter 1 to hop towards the bushes and enjoy"
                       " the delicious fruits.")
    senarioList.append("Enter 2 to hop towards to the hole and go"
                       " back to your burrow.")
    senarioList.append("Enter 3 to stay here and keep eating the grass.")
    print_pause(senarioList)
    grasslandChoice = check_choice(3)
    return grasslandChoice


def bush():
    senarioList = []
    senarioList.append("You jump towards the bushes and start to"
                       " enjoy the fruits. ")
    senarioList.append("A fox jumps towards you from the back of bushes. ")
    senarioList.append("Enter 1 to run back to the hole as fast as you can. ")
    senarioList.append("Enter 2 to jump high and kick on the face of fox. ")
    print_pause(senarioList)
    bushChoice = check_choice(2)
    if bushChoice == 1:
        caughtIf = chance_caught([3, 1])
        if caughtIf:
            print_pause(["Unfortunately, You are caught by the fox"
                         " though you run hard. "])
            return True
        else:
            print_pause(["Luckily, You escape succefully and"
                         " come back to your burrow!"])
    else:
        caughtIf = chance_caught([2, 1])
        if caughtIf:
            print_pause(["Unfortunately, Your attack is not strong enough. ",
                         "You are caught by the fox. "])
            return True
        else:
            print_pause(["Your brave behavior works and buys you some time. ",
                         "You escape succefully and come back"
                         " to your burrow!"])
    return False


def eat_grass():
    senarioList = []
    senarioList.append("You stay where you are and keep enjoying the grass. ")
    animalList = ["golden eagle", "fox"]
    predator = random.choice(animalList)
    if predator == "golden eagle":
        senarioList.append("Suddenly, you notice a golden eagle dives"
                           " towards you with an incredible speed!")
    else:
        senarioList.append("Suddenly, you notice a fox jumps towards you!")
    senarioList.append("Enter 1 to run back to the hole as fast as you can. ")
    senarioList.append("Enter 2 to jump high and kick the "+predator)
    print_pause(senarioList)
    eatGrassChoice = check_choice(2)
    if eatGrassChoice == 1:
        caughtIf = chance_caught([3, 1])
        if caughtIf:
            print_pause(["Unfortunately, You are caught by the "
                         + predator + " though you run hard. "])
            return True
        else:
            print_pause(["Luckily, You escape succefully and come"
                         " back to your burrow!"])
    else:
        caughtIf = chance_caught([2, 1])
        if caughtIf:
            print_pause(["Unfortunately, Your attack is not strong enough. ",
                         "You are caught by the "+predator+". "])
            return True
        else:
            print_pause(["Your brave behavior works and buys you some time. ",
                         "You escape succefully and come back"
                         " to your burrow!"])
    return False


def burrow():
    senarioList = []
    senarioList.append("You come back to your cozy burrow. ")
    senarioList.append("You see your rabbit buddies and tell"
                       " them how good the fruits look like. ")
    senarioList.append("All of you want to eat that fruits and"
                       " you guys decide to collaborate. ")
    senarioList.append("Some rabbits will help watching the surrounding"
                       " and send alert from different holes. ")
    senarioList.append("You and your mate will take the duty of"
                       " collecting the fruits.")
    senarioList.append("You and your buddies start the fruit mission. ")
    senarioList.append("You and your mate come out carefully from the "
                       "burrow to the grassland.")
    print_pause(senarioList)


def grassland():
    senarioList = []
    senarioList.append("After the other rabbits send clear signal, ")
    senarioList.append("you two run towards the bushes to"
                       " collect the fruits. ")
    senarioList.append("After a while, you heard the sound that"
                       " the other rabbits thump their feet. ")
    senarioList.append("You know it is the alert that predetors"
                       " are approaching. ")
    senarioList.append("Enter 1 to run back to the hole as fast"
                       " as you can with your mate. ")
    senarioList.append("Enter 2 to collect a little more because"
                       " you want others have enough fruits. ")
    print_pause(senarioList)
    yourChoice = check_choice(2)
    if yourChoice == 1:
        print_pause(["Thanks to the alert sent by other rabbits"
                     ", you react fast. ",
                     "You and your mate both come back to your burrow!"])
        happyEnding = True
    else:
        caughtIf = chance_caught([2, 1])
        if caughtIf:
            print_pause(["You stay too long. When the predator almost"
                         " catch your mate, ",
                         "you sacrifice for your mate and are caught"
                         " by predator. ",
                         "Your mate brings enough fruits to others. "])
            happyEnding = False
        else:
            print_pause(["Though You let your mate run first and stay"
                         " to collect more fruits. ",
                         "you are strong enough and run quickly. "
                         "You escape succefully and come back to"
                         " your burrow!"])
            happyEnding = True
    return happyEnding


def play_game():
    getFruit = False
    happyEnding = False
    print_pause(["You find yourself becoming a cute cottontail rabbit. "])
    yourChoiceGrass = grasslandIntro()
    if yourChoiceGrass == 1:
        caughtBush = bush()
        if caughtBush:
            return getFruit, happyEnding
    elif yourChoiceGrass == 3:
        caughtEatGrass = eat_grass()
        if caughtEatGrass:
            return getFruit, happyEnding
    burrow()
    happyEnding = grassland()
    getFruit = True
    return getFruit, happyEnding


fruit, result = play_game()
playAgain = check_result(fruit, result)
while playAgain == "y":
    fruit, result = play_game()
    playAgain = check_result(fruit, result)
