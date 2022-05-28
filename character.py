import random
import re
from urllib.parse import parse_qs
import pandas as pd
from item import items
import colorama
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

startHelmet=items("helmet","Starter Helmet", 5, 0, 5, 0, -5, -5)
startChestplate=items("chestplate","Starter Chestplate", 5, 0, 5, 0, -5, -5)
startLeggings=items("leggings","Starter Leggings", 5, 0, 5, 0, -5, -5)
startBoots=items("boots","Starter Boots", 5, 0, 5, 0, -5, -5)

startStaff=items("weapon", "Wizard Staff", 0, 10, 0, 10, -2, 2)
startSword=items("weapon", "Warrior Sword", 0, -5, 0, 0, 8, -4)
startDagger=items("weapon", "Rogue's Dagger", 0, -2, 0, -2, 6, 6)

null=items("weapon", "null", 0, 0, 0, 0, 0, 0)
nullBoots=items("boots", "null boots", 0, 0, 0, 0, 0, 0)

class characters: #class is used to make an object
    def __init__(self, rpgclass:str, name:str, maxhp:int, hp:int, maxmana:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, xp:int, xpcontainer:int, level:int, coins:int, weapon, helmet, chestplate, leggings, boots, inv:list):
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
        return characters("Mage", name, 85, 85, 125, 125, 15, 25, 15, 20, 0, 20, 0, 25, startStaff, startHelmet, startChestplate, startLeggings, startBoots, [])

    def rogueSetup(name):
        return characters("Rogue", name, 100, 100, 70, 70, 18, 15, 18, 25, 0, 20, 0, 25, startDagger, startHelmet, startChestplate, startLeggings, startBoots, [])

    def warriorSetup(name):
        return characters("Warrior", name, 110, 110, 50, 50, 22, 12, 22, 14, 0, 20, 0, 25, startSword, startHelmet, startChestplate, startLeggings, startBoots, [])
        
    def testSetup(name):
        return characters("Human", name, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, startStaff, startHelmet, startChestplate, startLeggings, startBoots, [null, nullBoots])

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
                

    def stats(self):
        print()
        print("----------------"+self.name+"'s Stats----------------")
        print("Class: "+self.rpgclass)
        print("Level "+str(self.level)+" <-> "+str(self.xp)+"/"+str(self.xpcontainer)+" XP until next level")
        print(Fore.LIGHTYELLOW_EX+"Coins: "+str(self.coins))
        print(Fore.LIGHTRED_EX+"❤  Health: "+str(self.hp)+"/"+str(self.maxhp)+Style.RESET_ALL+"     Helmet: "+str(self.helmet.name))
        print(Fore.BLUE+"🕮  Mana: "+str(self.mana)+"/"+str(self.maxmana)+Style.RESET_ALL+"       Chestplate: "+str(self.chestplate.name))
        print(Fore.LIGHTGREEN_EX+"❈ Defense: "+str(self.defense)+Style.RESET_ALL+"           Leggings: "+str(self.leggings.name))
        print(Fore.BLUE+"✎ Intelligence: "+str(self.intelligence)+Style.RESET_ALL+"        Boots: "+str(self.boots.name))
        print(Fore.RED+"❁ Strength: "+str(self.strength)+Style.RESET_ALL+"         Weapon: "+str(self.weapon.name))
        print("✦ Speed: "+str(self.speed))
        print()


    def showInv(self):
        weaponstr=""
        armorstr=""
        otherstr=""
        for i in self.inv:
            if i.typeofitem=="boots" or i.typeofitem=="leggings" or i.typeofitem=="helmet" or i.typeofitem=="chestplate":
                armorstr+="\n"+"    "+i.name
        for i in self.inv:
            if i.typeofitem=="weapon":
                weaponstr+="\n"+"    "+i.name
        for i in self.inv:
            if i.typeofitem=="usable":
                otherstr+="\n"+"    "+i.name
        print("Armor:"+armorstr)
        print("Weapons:"+weaponstr)
        print("Others:"+otherstr)

    def itemInfo(self, itemname):
        for i in self.inv:
            if itemname.lower()==i.name.lower():
                i.info()
                break
            elif itemname.lower()==self.helmet.name.lower():
              self.helmet.info()
              break
            elif itemname.lower()==self.chestplate.name.lower():
              self.chestplate.info()
              break
            elif itemname.lower()==self.leggings.name.lower():
              self.leggings.info()
              break
            elif itemname.lower()==self.boots.name.lower():
              self.boots.info()
              break
            elif itemname.lower()==self.weapon.name.lower():
              self.weapon.info()
              break
            else:
              print("This item doesn't exist or You don't have it")


    def equip(self, itemname):
        for i in self.inv:
            eqitem=""
            if itemname.lower()==i.name.lower():
                if i.typeofitem=="helmet":
                    eqitem="helmet"
                    self.inv.remove(i)
                elif i.typeofitem=="chestplate":
                    eqitem="chestplate"
                    self.inv.remove(i)
                elif i.typeofitem=="leggings":
                    eqitem="leggings"
                    self.inv.remove(i)
                elif i.typeofitem=="boots":
                    eqitem="boots"
                    self.inv.remove(i)
                elif i.typeofitem=="weapon":
                    eqitem="weapon"
                    self.inv.remove(i)
                return [i ,eqitem]

    def recieve(self, eqeditem):
      typeofitem=eqeditem[1]
      if typeofitem=="helmet":
          self.helmet=eqeditem[0]
      elif typeofitem=="chestplate":
          self.chestplate=eqeditem[0]
      elif typeofitem=="leggings":
          self.leggings=eqeditem[0]
      elif typeofitem=="boots":
          self.boots=eqeditem[0]
      elif typeofitem=="weapon":
          self.weapon=eqeditem[0]
      else:
        print("Item cannot be equipped or doesn't exist")


player=characters.testSetup("name")
player.stats()
# print(player.inv)
# player.recieve(player.equip("null boots"))
# print(player.inv)
# player.stats()
player.itemInfo("starter helmet")
