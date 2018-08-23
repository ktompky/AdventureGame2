import random
from monsterList import Monster


minionMonster = Monster("Minion",10)
defaultMonster = Monster("Monster", 15)
bossMonster = Monster("Boss", 25)

def AttackRoll():
    attack = random.randint(1,6)
    print(attack)


def twentySided():
    twentySide = random.randint(1,20)


print(minionMonster.health)
AttackRoll()
