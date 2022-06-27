import random
import pandas as pd
import colorama
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
import item
from item import items
from item import itemDict
import attack
from attack import attacks
from attack import attackDict
monlist=[]

def inputcheck(message:str):
    while True:
        try:
            message=int(input(message))
            break
        except ValueError:
            print("Try again with a num")
    return message

class characters: #class is used to make an object
    def __init__(self, rpgclass:str, name:str, maxhp:int, hp:int, maxmana:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, xp:int, xpcontainer:int, level:int, coins:int, weapon, helmet, chestplate, leggings, boots, inv:list, attackmoves:list):
        self.rpgclass = rpgclass
        self.name = name
        self.maxhp = maxhp #self refers to the object
        self.extrahp = 0
        self.hp = hp
        self.maxmana = maxmana
        self.extramana = 0
        self.mana = mana
        self.defense = defense
        self.extradefense = 0
        self.intelligence = intelligence
        self.extraintelligence = 0
        self.strength = strength
        self.extrastrength = 0
        self.speed = speed
        self.extraspeed = 0
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
        self.attackmoves=attackmoves
        if self.rpgclass=="Monster":
            monlist.append(self)

    def restore(self):
        self.mana=self.maxmana
        self.hp=self.maxhp
      
    def applystats(self):
        self.maxhp-=self.extrahp
        self.maxmana-=self.extramana
        self.defense-=self.extradefense
        self.intelligence-=self.extraintelligence
        self.strength-=self.extrastrength
        self.speed-=self.extraspeed

        self.extrahp=0
        self.extramana=0
        self.extradefense=0
        self.extraintelligence=0
        self.extrastrength=0
        self.extraspeed=0
        
        stats=vars(self.weapon)
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        stats=vars(self.helmet)
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        stats=vars(self.chestplate)
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        stats=vars(self.leggings)
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        stats=vars(self.boots)
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
          
        self.maxhp+=self.extrahp
        self.maxmana+=self.extramana
        self.defense+=self.extradefense
        self.intelligence+=self.extraintelligence
        self.strength+=self.extrastrength
        self.speed+=self.extraspeed    

    def mageSetup(name):
        return characters("Mage", name, 85, 85, 125, 125, 15, 30, 10, 20, 0, 25, 0, 25, itemDict["wizard'sstaff"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], [], [attackDict["bonk"],attackDict["embers"], attackDict[""],attackDict[""]])

    def rogueSetup(name):
        return characters("Rogue", name, 100, 100, 70, 70, 18, 20, 20, 25, 0, 25, 0, 25, itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], [], [attackDict["cut"],attackDict[""],attackDict[""],attackDict[""]])

    def warriorSetup(name):
        return characters("Warrior", name, 110, 110, 50, 50, 22, 10, 30, 14, 0, 25, 0, 25, itemDict["warrior'ssword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[], [attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
        
    def testSetup(name):
        inv=[]
        testattacks=[]
        for key, value in itemDict.items():
            temp = value
            inv.append(temp)
        for key, value in attackDict.items():
            temp=value
            testattacks.append(temp)
        return characters("Human", name, 100, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, itemDict["null"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], inv, testattacks)

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
        for key,data in itemDict:
            if itemname.lower()==data.name.lower():
                data.info()
                found=True
            
        if not found==True:
            print("This item doesn't exist")

    def equip(self, itemname):
        for i in self.inv:
            if itemname.lower()==i.name.lower():
                if i.amount>1:
                    pos=self.inv.index(i)
                    self.inv[pos].amount-=1
                    if i.typeofitem=="helmet":
                        if self.helmet in self.inv:
                            pos=self.inv.index(self.helmet)
                            self.inv[pos].amount+=1
                        else:
                            self.helmet.amount=1
                            self.inv.append(self.helmet)
          
                        self.helmet=i
                    elif i.typeofitem=="chestplate":
                        if self.chestplate in self.inv:
                            pos=self.inv.index(self.chestplate)
                            self.inv[pos].amount+=1
                        else:
                            self.chestplate.amount=1
                            self.inv.append(self.chestplate)
          
                        self.chestplate=i
                    elif i.typeofitem=="leggings":
                        if self.leggings in self.inv:
                            pos=self.inv.index(self.leggings)
                            self.inv[pos].amount+=1
                        else:
                            self.leggings.amount=1
                            self.inv.append(self.leggings)
          
                        self.leggings=i
                    elif i.typeofitem=="boots":
                        if self.boots in self.inv:
                            pos=self.inv.index(self.boots)
                            self.inv[pos].amount+=1
                        else:
                            self.boots.amount=1
                            self.inv.append(self.boots)
          
                        self.boots=i
                    elif i.typeofitem=="weapon":
                        if self.weapon in self.inv:
                            pos=self.inv.index(self.weapon)
                            self.inv[pos].amount+=1
                        else:
                            self.weapon.amount=1
                            self.inv.append(self.weapon)
          
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
                        self.helmet=i
                    elif i.typeofitem=="chestplate":
                        if self.chestplate in self.inv:
                            pos=self.inv.index(self.chestplate)
                            self.inv[pos].amount+=1
                        else:
                            self.chestplate.amount=1
                            self.inv.append(self.chestplate)
          
                        self.chestplate=i
                    elif i.typeofitem=="leggings":
                        if self.leggings in self.inv:
                            pos=self.inv.index(self.leggings)
                            self.inv[pos].amount+=1
                        else:
                            self.leggings.amount=1
                            self.inv.append(self.leggings)
          
                        self.leggings=i
                    elif i.typeofitem=="boots":
                        if self.boots in self.inv:
                            pos=self.inv.index(self.boots)
                            self.inv[pos].amount+=1
                        else:
                            self.boots.amount=1
                            self.inv.append(self.boots)
          
                        self.boots=i
                    elif i.typeofitem=="weapon":
                        if self.weapon in self.inv:
                            pos=self.inv.index(self.weapon)
                            self.inv[pos].amount+=1
                        else:
                            self.weapon.amount=1
                            self.inv.append(self.weapon)
          
                        self.weapon=i
                    else:
                        print("Item cannot be equipped")
        self.applystats()
                
    def buy(self, buyitem:items):
      buyitem=buyitem.replace(" ", "").lower()
      if not buyitem[:1]=="l":
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

    def checkLevel(self):
        if self.level==8:
            if self.rpgclass.lower()=="mage":
                print("Congragulations!")
                print(Fore.LIGHTYELLOW_EX+"You have obtained the attack: "+attackDict["fireball"].color+" Fireball")
                input("Next ")
                print("\n"*100)
                self.attackMenu()
                slot=inputcheck("Which slot would you like to put the move "+attackDict["fireball"].color+"Fireball? ")
                self.attackmoves[int(slot-1)]=attackDict["fireball"]
            elif self.rpgclass.lower()=="warrior":
                print("Congragulations!")
                print(Fore.LIGHTYELLOW_EX+"You have obtained the attack: "+attackDict["shieldbash"].color+" Shield Bash")
                input("Next ")
                print("\n"*100)
                self.attackMenu()
                slot=inputcheck("Which slot would you like to put the move "+attackDict["shieldbash"].color+"Shield Bash? ")
                self.attackmoves[int(slot-1)]=attackDict["shieldbash"]
            elif self.rpgclass.lower()=="rogue":
                print("Congragulations!")
                print(Fore.LIGHTYELLOW_EX+"You have obtained the attack: "+attackDict["daggerthrow"].color+" Dagger Throw")
                input("Next ")
                print("\n"*100)
                self.attackMenu()
                slot=inputcheck("Which slot would you like to put the move "+attackDict["daggerthrow"].color+"Shield Bash? ")
                self.attackmoves[int(slot-1)]=attackDict["daggerthrow"]

    def levelup(self):
        while self.xp>=self.xpcontainer:
            self.xp=int(self.xp-self.xpcontainer)
            self.level+=1
            self.xpcontainer=int(self.xpcontainer*1.2)
            print(Fore.YELLOW+"You Leveled Up!"+Style.RESET_ALL+"      You are now level: "+Fore.YELLOW+str(self.level))
            self.checkLevel()

    def attackMenu(self):
        moves=[]
        for i in self.attackmoves:
            moves.append(i)
        print("Move 1: "+moves[0].color+moves[0].name+Style.RESET_ALL+"Move 3: "+moves[2].color+moves[2].name)
        print("Move 2: "+moves[1].color+moves[1].name+Style.RESET_ALL+"Move 4: "+moves[3].color+moves[3].name)

          


# player=characters.mageSetup("name")
# player.xp+=100000000
# player.levelup()

area1skel=characters("Monster", "Skeleton", 100, 100, 20, 20,25, 0, 20,25, 0,0,3,15,itemDict["skeletonsword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
area1gob=characters("Monster", "Goblin", 80, 80, 40, 40, 15, 5, 20,25, 0,0,3,20,itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
area1orc=characters("Monster", "Orc", 120, 120, 30, 30, 25, 5, 38, 15, 0,0,3,20,itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
