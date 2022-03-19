import random
import pandas as pd
from item import items

class characters: #class is used to make an object
    def __init__(self, rpgclass:str, name:str, maxhp:int, hp:int, maxmana:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, xp:int, xpcontainer:int, level:int, coins:int, weapon:str, helmet:str, chestplate:str, leggings:str, boots:str, inv:list):
        self.rpgclass = rpgclass
        self.name = name
        self.maxhp = maxhp #self refers to the object
        self.hp = hp
        self.maxmana = maxmana
        self.mana = mana
        self.defense = defense
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.xp = xp
        self.xpcontainer = xpcontainer
        self.level = level
        self.coins = coins
        self.weapon= weapon
        self.helmet=helmet
        self.chestplate=chestplate
        self.leggings=leggings
        self.boots=boots
        self.inv=inv

    def mageSetup(name):
        Mage=characters("Mage", name, 85, 85, 125, 125, 15, 25, 15, 20, 0, 20, 0, 25, )
        return Mage

    def rogueSetup(name):
        Rogue=characters("Rogue", name, 100, 100, 70, 70, 18, 15, 18, 25, 0, 20, 0, 25)
        return Rogue

    def warriorSetup(name):
        Warrior=characters("Warrior", name, 110, 110, 50, 50, 22, 12, 22, 14, 0, 20, 0, 25)
        return Warrior

    def createCharacter():
        name = input("What is your name? ")
        while True:
            print("What class would you like to be? ")
            print("You can be a Mage, Rogue, or a Warrior")
            rpgclass=input("")
            rpgclass=rpgclass.lower()
            if rpgclass=="mage":
                return characters.mageSetup(name)
            elif rpgclass=="rogue":
                return characters.rogueSetup(name)
            elif rpgclass=="warrior":
                return characters.warriorSetup(name)
            else:
                print("That isn't a valid choice")
                print()
                

    def stats(player):
        print()
        print("----------------"+player.name+"'s Stats----------------")
        print("Class: "+player.rpgclass)
        print("Level "+str(player.level)+" <-> "+str(player.xp)+"/"+str(player.xpcontainer)+" XP until next level")
        print("Coins: "+str(player.coins))
        print("Health: "+str(player.hp)+"/"+str(player.maxhp))
        print("Mana: "+str(player.mana)+"/"+str(player.maxmana))
        print("Speed: "+str(player.speed))
        print("Defense: "+str(player.defense))
        print("Intelligence: "+str(player.intelligence))
        print("Strength: "+str(player.strength))
        print()

