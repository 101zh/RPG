import random
import item
from item import items
attackDict={}

class attacks:
    def __init__(self, name:str, burn:int, freeze:int, stun:int, flinch:int, damage:int, type:str, descrip:list):
      self.burn=burn
      self.name=name
      self.freeze=freeze
      self.stun=stun
      self.flinch=flinch
      self.damage=damage
      self.type=type
      self.descrip=descrip
      # self.specfunc=specfunc
      # self.specfuncinput=specfuncinput
      attackDict[self.name.replace(" ","").lower()]= self

zed= attacks("               ", 0, 0, 0, 0, 0, "", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing ", "You missed..."])

bonk=attacks("Bonk           ", 0, 0, 0, 5, 25, "Physical", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing ", "You missed..."])
slash=attacks("Slash          ", 0, 0, 0, 5, 35, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing ", "You missed..."])
cut=attacks("Cut            ", 0, 0, 0, 5, 25, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing ", "You missed..."])

dagger=attacks("Dagger Throw   ", 0, 0, 0, 40, 15, "Physical", ["The dagger hit his skin ", "You hit the enemy's eye dealing ", "You missed..."])
bash=attacks("Shield Bash    ", 0, 0, 0, 30, 30, "Physical", ["Your shield hits the enemy and pushes him back dealing ", "You sprint at full speed knocking over your enemy dealing ", "You missed..."])

ember=attacks("Embers         ", 33, 0, 0, 5, 20, "Magic", ["The enemy's is burned by your embers dealing ", "You light the enemy's face on fire dealing ", "The embers couldn't reach the enemy"])
fireball= attacks("Fireball       ", 75, 0, 0, 5, 55, "Magic", ["The enemy's foot gets hit by a fireball dealing ", "You hit the enemy dead on dealing ", "You launched the fireball only to miss"])

# attacks("               ", 0, 0, 0, 5, 25, "Physical", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing ", "You missed..."])
# attacks("Bonk           ", 0, 0, 0, 5, 25, "Physical", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing ", "You missed..."])
# attacks("Slash          ", 0, 0, 0, 5, 35, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing ", "You missed..."])
# attacks("Cut            ", 0, 0, 0, 5, 25, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing ", "You missed..."])
# attacks("Dagger Throw   ", 0, 0, 0, 40, 15, "Physical", ["The dagger hit his skin ", "You hit the enemy's eye dealing ", "You missed..."])
# attacks("Shield Bash    ", 0, 0, 0, 30, 30, "Physical", ["Your shield hits the enemy and pushes him back dealing ", "You sprint at full speed knocking over your enemy dealing ", "You missed..."])
# attacks("Embers         ", 33, 0, 0, 5, 20, "Magic", ["The enemy's is burned by your embers dealing ", "You light the enemy's face on fire dealing ", "The embers couldn't reach the enemy"])
# attacks("Fireball       ", 75, 0, 0, 5, 55, "Magic", ["The enemy's foot gets hit by a fireball dealing ", "You hit the enemy dead on dealing ", "You launched the fireball only to miss"])
