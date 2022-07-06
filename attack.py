import random

from colorama import Fore
import item
from item import items
attackDict={}

class attacks:
    def __init__(self, name:str, burn:int, freeze:int, stun:int, flinch:int, damage:int,manacost:int, type:str, descrip:list, color):
      self.burn=burn
      self.name=name
      self.freeze=freeze
      self.stun=stun
      self.flinch=flinch
      self.damage=damage
      self.manacost=manacost
      self.type=type
      self.descrip=descrip
      self.color=color
      # self.specfunc=specfunc
      # self.specfuncinput=specfuncinput
      attackDict[self.name.replace(" ","").lower()]= self

attacks("               ", 0, 0, 0, 0, 0,0, "nonexistent", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing ", "You missed..."],Fore.WHITE)

attacks("Pounce         ", 0, 0, 0, 10, 15, 0, "Physical", ["You pounce upon the enemy dealing ", "You bellyflop onto the enemy dealing ", "You missed...", " bouces on you dealing ", " covers you in slime as the pouce upon you dealing ", " missed..."], Fore.WHITE)
attacks("Bonk           ", 0, 0, 0, 5, 25,0, "Physical", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing ", "You missed...", " bonks you on the head dealing ", " bludgeon your head dealing ", " missed... "],Fore.WHITE)
attacks("Slash          ", 0, 0, 0, 5, 30,0, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing ", "You missed...", " cuts you dealing ", " cuts your leg as blood trickles down dealing ", " missed..."],Fore.WHITE)
attacks("Cut            ", 0, 0, 0, 5, 25,0, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing ", "You missed..."], Fore.WHITE)

attacks("Dagger Throw   ", 0, 0, 0, 40, 15,0, "Physical", ["The dagger is lodged in its arm ", "You hit the enemy's eye dealing ", "You missed..."], Fore.LIGHTRED_EX)
attacks("Shield Bash    ", 0, 0, 0, 30, 30,0, "Physical", ["Your shield hits the enemy and pushes him back dealing ", "You sprint at full speed knocking over your enemy dealing ", "You missed..."], Fore.LIGHTGREEN_EX)

attacks("Embers         ", 33, 0, 0, 5, 20,20, "Magic", ["The enemy's is burned by your embers dealing ", "You light the enemy's face on fire dealing ", "The embers couldn't reach the enemy"], Fore.RED)
attacks("Fireball       ", 75, 0, 0, 5, 55,45, "Magic", ["The enemy's foot gets hit by a fireball dealing ", "You hit the enemy dead on dealing ", "You launched the fireball only to miss"], Fore.RED)


