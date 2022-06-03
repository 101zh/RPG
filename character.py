import random
import re
from urllib.parse import parse_qs
import pandas as pd
from item import items
import colorama
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
import item
from item import itemDict

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
        itemDict["rogue's dagger"].amount=0
        itemDict["warrior's sword"].amount=0
        return characters("Mage", name, 85, 85, 125, 125, 15, 25, 15, 20, 0, 20, 0, 25, itemDict["wizard's staff"], itemDict["starter helmet"], itemDict["starter chestplate"], itemDict["starter leggings"], itemDict["starter boots"], [])

    def rogueSetup(name):
        return characters("Rogue", name, 100, 100, 70, 70, 18, 15, 18, 25, 0, 20, 0, 25, itemDict["rogue's dagger"], itemDict["starter helmet"], itemDict["starter chestplate"], itemDict["starter leggings"], itemDict["starter boots"], [])

    def warriorSetup(name):
        return characters("Warrior", name, 110, 110, 50, 50, 22, 12, 22, 14, 0, 20, 0, 25, itemDict["warrior's sword"], itemDict["starter helmet"], itemDict["starter chestplate"], itemDict["starter leggings"], itemDict["starter boots"], [])
        
    def testSetup(name):
        inv=[]
        for key, value in itemDict.items():
            temp = value
            temp.amount=1
            inv.append(temp)
        return characters("Human", name, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, itemDict["null"], itemDict["starter helmet"], itemDict["starter chestplate"], itemDict["starter leggings"], itemDict["starter boots"], inv)

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
                armorstr+="\n"+"    "+i.name+" x"+str(i.amount)
        for i in self.inv:
            if i.typeofitem=="weapon":
                weaponstr+="\n"+"    "+i.name+" x"+str(i.amount)
        for i in self.inv:
            if i.typeofitem=="usable":
                otherstr+="\n"+"    "+i.name+" x"+str(i.amount)
        print("Armor:"+armorstr)
        print("Weapons:"+weaponstr)
        print("Others:"+otherstr)

    def itemInfo(self, itemname):
        found=False
        for i in itemDict:
            if itemname.lower()==i.name.lower():
                i.info()
                found=True
            
        if not found==True:
            print("This item doesn't exist")


    def equip(self, itemname):
        for i in self.inv:
            if itemname.lower()==i.name.lower():
                if i.amount>1:
                    i.amount-=1
                    if i.typeofitem=="helmet":
                        if self.helmet in self.inv:
                            pos=self.inv.index(self.helmet)
                            self.inv[pos].amount+=1
                        else:
                            self.helmet.amount=1
                            self.inv.append(self.helmet)
                        i.amount=0
                        self.helmet=i
                    elif i.typeofitem=="chestplate":
                        if self.chestplate in self.inv:
                            pos=self.inv.index(self.chestplate)
                            self.inv[pos].amount+=1
                        else:
                            self.chestplate.amount=1
                            self.inv.append(self.chestplate)
                        i.amount=0
                        self.chestplate=i
                    elif i.typeofitem=="leggings":
                        if self.leggings in self.inv:
                            pos=self.inv.index(self.leggings)
                            self.inv[pos].amount+=1
                        else:
                            self.leggings.amount=1
                            self.inv.append(self.leggings)
                        i.amount=0
                        self.leggings=i
                    elif i.typeofitem=="boots":
                        if self.boots in self.inv:
                            pos=self.inv.index(self.boots)
                            self.inv[pos].amount+=1
                        else:
                            self.boots.amount=1
                            self.inv.append(self.boots)
                        i.amount=0
                        self.boots=i
                    elif i.typeofitem=="weapon":
                        if self.weapon in self.inv:
                            pos=self.inv.index(self.weapon)
                            self.inv[pos].amount+=1
                        else:
                            self.weapon.amount=1
                            self.inv.append(self.weapon)
                        i.amount=0
                        self.weapon=i
                    else:
                        print("Item cannot be equipped")
                else:
                    self.inv.remove(i)
                    if i.typeofitem=="helmet":
                        if self.helmet in self.inv:
                            pos=self.inv.index(self.helmet)
                            self.inv[pos].amount+=1
                        else:
                            self.helmet.amount=1
                            self.inv.append(self.helmet)
                        i.amount=0
                        self.helmet=i
                    elif i.typeofitem=="chestplate":
                        if self.chestplate in self.inv:
                            pos=self.inv.index(self.chestplate)
                            self.inv[pos].amount+=1
                        else:
                            self.chestplate.amount=1
                            self.inv.append(self.chestplate)
                        i.amount=0
                        self.chestplate=i
                    elif i.typeofitem=="leggings":
                        if self.leggings in self.inv:
                            pos=self.inv.index(self.leggings)
                            self.inv[pos].amount+=1
                        else:
                            self.leggings.amount=1
                            self.inv.append(self.leggings)
                        i.amount=0
                        self.leggings=i
                    elif i.typeofitem=="boots":
                        if self.boots in self.inv:
                            pos=self.inv.index(self.boots)
                            self.inv[pos].amount+=1
                        else:
                            self.boots.amount=1
                            self.inv.append(self.boots)
                        i.amount=0
                        self.boots=i
                    elif i.typeofitem=="weapon":
                        if self.weapon in self.inv:
                            pos=self.inv.index(self.weapon)
                            self.inv[pos].amount+=1
                        else:
                            self.weapon.amount=1
                            self.inv.append(self.weapon)
                        i.amount=0
                        self.weapon=i
                    else:
                        print("Item cannot be equipped")

                

    def buy(self, buyitem):
      buyitem.lower()
      try:
        buyitem=itemDict[buyitem]
        if buyitem.cost>self.coins:
          print("You don't have enough coins to buy this item")
        else:
          if buyitem in self.inv:
            pos=self.inv.index(buyitem)
            self.inv[pos].amount+=1
            self.coins-=buyitem.cost
          else: 
            self.coins-=buyitem.cost
            buyitem.amount=1
            self.inv.append(buyitem)
      except KeyError:
        print("Did you misspell? because this item doesn't exist")


player=characters.testSetup("name")

player.showInv()
player.equip("starter chestplate")
player.showInv()
