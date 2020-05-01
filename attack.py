import random
from character_list import Monster,Player



singleMonster = Monster("Monster", 15)
singlePlayer = Player(input("What is your name? "), 20)

def roll_initiative():
    return random.randint(1,20)


def startGame():
    print("Hello %s" % singlePlayer.name)
    print("Rolling for initiative....")
    initiative = roll_initiative()
    print("Your initiative roll was %s " % initiative)
    if initiative >= 10:
        playerTurn()
    else:
        monsterTurn()


def monsterTurn():
    print("It's the monster's turn!")
    attack = random.randint(1,6)
    singlePlayer.health -= attack
    print("They attacked you for %s" % attack)
    print("You are now at %s hit points!" % singlePlayer.health)
    if singlePlayer.health >= 1:
        playerTurn()
    else:
        print("You've been killed.")


def playerTurn():
    print("It's your turn!")
    attack = random.randint(1,6)
    singleMonster.health -= attack
    print("You attacked them for:  %s point(s)." % attack)
    print("The monster is now at: %s hit points." % singleMonster.health)
    if singleMonster.health >= 1:
        monsterTurn()
    else:
        print("You killed it.")




    

if __name__ == '__main__':
    startGame()
    









