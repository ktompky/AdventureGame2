import random
from character_list import Monster,Player



singleMonster = Monster("Monster", 15)
singlePlayer = Player(input("What is your name? "), 20)
attack = random.randint(1,6)
initiative = random.randint(1,20)


def startGame():
    print("Hello %s" % singlePlayer.name)
    print("Rolling for initiative....")


def monsterAttack():
    print("It's now the monster's turn!")
    singlePlayer.health -= attack
    print("They attacked you for %s" % attack)
    print("You are now at %s hit points!" % singlePlayer.health)
    playerAttack()


def playerAttack():
    
    if initiative >= 10:
        print("Your initiative roll was %s so you get to attack! " % initiative)
        singleMonster.health -= attack
        print("You attacked them for:  %s point(s)." % attack)
        print("The monster is now at: %s hit points." % singleMonster.health)
        monsterAttack()

    else:
        print("Evaded!")
        print("Your initiative roll was %s " % initiative)
        monsterAttack()

while singleMonster.health and singlePlayer.health != 0:
    playerAttack()
    monsterAttack()

if __name__ == '__main__':
    startGame()
    









