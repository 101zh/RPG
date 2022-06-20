import random
import character
from character import characters
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
      attackDict[self.name.lower()]= self

bonk=attacks("Bonk", 0, 0, 0, 10, 15, "Physical", ["You hit the enemy's arm dealing ", "You bludgeon the enemy's head dealing", "You missed..."])
slash=attacks("Slash", 0, 0, 0, 10, 30, "Physical", ["You cut the enemy dealing ", "You hit the enemy's eye dealing", "You missed..."])