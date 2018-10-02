import random
from monsterList import Monster,Player


minionMonster = Monster("Minion",10)
defaultMonster = Monster("Monster", 15)
bossMonster = Monster("Boss", 25)
singlePlayer = Player(input("What is your name? "), 20)

attack = random.randint(1,6)
initiative = random.randint(1,20)

def monsterAttack():
    print("It's now the monster's turn!")
    singlePlayer.health -= attack
    print("You are now at " + str(singlePlayer.health) + " hit points!")


if initiative >= 10:
    minionMonster.health -= attack
    print("You attacked them for: " + str(attack) + " point(s)!")
    print("The monster is now at: " + str(minionMonster.health) + " hit points!")
else:
    print("Evaded!")
    monsterAttack()








