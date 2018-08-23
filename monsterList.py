class Monster:
  def __init__(self,name,health):
    self.name = name
    self.health = health
    
  def Growl():
    print("Grrrrrrrrr!!!!")


minionMonster = Monster("Minion",10)
defaultMonster = Monster("Monster", 15)
bossMonster = Monster("Boss", 25)
