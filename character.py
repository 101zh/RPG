import random
import numpy
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

    # Restores health and mana
    def restore(self):
        self.mana=self.maxmana
        self.hp=self.maxhp

    # Adds the stats from equipped items 
    def applystats(self):
        # Resets base level stats
        self.maxhp-=self.extrahp
        self.maxmana-=self.extramana
        self.defense-=self.extradefense
        self.intelligence-=self.extraintelligence
        self.strength-=self.extrastrength
        self.speed-=self.extraspeed
        # Resets external buffs
        self.extrahp=0
        self.extramana=0
        self.extradefense=0
        self.extraintelligence=0
        self.extrastrength=0
        self.extraspeed=0
        # Makes the weapon the character is holding a dictionary
        stats=vars(self.weapon)
        # Adds the buffs from that weapon
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the helmet the character is wearing a dictionary
        stats=vars(self.helmet)
        # Adds the buffs from that helmet
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the chestplate the character is wearing a dictionary
        stats=vars(self.chestplate)
        # Adds the buffs from that chestplate
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the leggings the character is wearing a dictionary
        stats=vars(self.leggings)
        # Adds the buffs from that legging
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the boots the character is wearing a dictionary
        stats=vars(self.boots)
        # Adds the buffs from that boots
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Adds stored buffs to actual stats
        self.maxhp+=self.extrahp
        self.maxmana+=self.extramana
        self.defense+=self.extradefense
        self.intelligence+=self.extraintelligence
        self.strength+=self.extrastrength
        self.speed+=self.extraspeed    

    def mageSetup(name):
        # Just returns a character object
        return characters("Mage", name, 85, 85, 125, 125, 15, 30, 10, 20, 0, 25, 0, 25, itemDict["wizard'sstaff"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], [], [attackDict["bonk"],attackDict["embers"], attackDict[""],attackDict[""]])

    def rogueSetup(name):
        # Just returns a character object
        return characters("Rogue", name, 100, 100, 70, 70, 18, 20, 20, 25, 0, 25, 0, 25, itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], [], [attackDict["cut"],attackDict[""],attackDict[""],attackDict[""]])

    def warriorSetup(name):
        # Just returns a character object
        return characters("Warrior", name, 110, 110, 50, 50, 22, 10, 30, 14, 0, 25, 0, 25, itemDict["warrior'ssword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[], [attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
        
    def testSetup(name):
        inv=[]
        testattacks=[]
        # Giving test character all items
        for key, value in itemDict.items():
            temp = value
            inv.append(temp)
        # Giving test character all attacks
        for key, value in attackDict.items():
            temp=value
            testattacks.append(temp)
        return characters("Human", name, 100, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, itemDict["null"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], inv, testattacks)

    def createCharacter():
        # Gets name
        name = input("What is your name? ")
        # Continuously repeats if they don't type in a correct class
        while True:
            print("What class would you like to be? ")
            print("You can be a Mage, Rogue, or a Warrior")
            rpgclass=input("")
            rpgclass=rpgclass.lower()
            # Determines what class they chose
            if rpgclass=="mage":
                return characters.mageSetup(name)
            elif rpgclass=="rogue":
                return characters.rogueSetup(name)
            elif rpgclass=="warrior":
                return characters.warriorSetup(name)
            else:
                print("That isn't a valid choice")
                print()
    
    # Shows the stats of the character
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

    # Shows the inventory of that character
    def showInv(self):
        # Declaring separate lists to organize into sections
        weaponslist=[]
        armorlist=[]
        otherslist=[]
        # Goes through every item in inventory
        for item in self.inv:
            item:items
            # Determines what type of item it is
            if item.typeofitem=="boots" or item.typeofitem=="leggings" or item.typeofitem=="helmet" or item.typeofitem=="chestplate":
                armorlist.append(item)
            elif item.typeofitem=="weapon":
                weaponslist.append(item)
            if item.typeofitem=="usable":
                otherslist.append(item)
        # Finds out which of the lists which have the most
        categories=[weaponslist, armorlist, otherslist]
        most= categories[numpy.argmax([len(l) for l in categories])]
        # Uses this information of longest list to add in a empty temp item, so it won't fall into an IndexError
        while len(armorlist)<len(most):
            armorlist.append(itemDict[""])
        while len(weaponslist)<len(most):
            weaponslist.append(itemDict[""])
        while len(otherslist)<len(most):
            otherslist.append(itemDict[""])

        print("Armor:                                 Weapons:                                 Others:")
        # Prints the amount of times the largest list has to cover all items.
        for item in range(len(most)):
            print("     "+armorlist[item].name+" "+str(armorlist[item].amount)+"x              "+weaponslist[item].name+" "+str(weaponslist[item].amount)+"x              "+otherslist[item].name+" "+str(otherslist[item].amount)+"x")
        print("\n")

    def itemInfo(self, itemname):
        # Declares a variable used to determine if item was found
        found=False
        # Looks through the entire dictionary to find if any item names match
        for key,value in itemDict:
            if itemname.lower()==value.name.lower():
                value.info()
                found=True
        # If the item wasn't found then it prints that the item doesn't exist
        if not found==True:
            print("This item doesn't exist")

    def equip(self, itemname):
        # Looks through entire inventory
        for item in self.inv:
            # if the names match then do below
            if itemname.lower()==item.name.lower():
                # If the amount of that item is 1 do what is indented
                if item.amount>1:
                    # Finds the item position to subtract 1 from it because it is no longer in inv
                    pos=self.inv.index(item)
                    self.inv[pos].amount-=1
                    # Checks if it's a helmet
                    if item.typeofitem=="helmet":
                        # If what the player is currently wearing is in the inventory increase the amount of it in inventory
                        # (So items can be stackable)
                        if self.helmet in self.inv:
                            pos=self.inv.index(self.helmet)
                            self.inv[pos].amount+=1
                        # If not in the inventory set the amount to 1 and add the new item to inventory
                        else:
                            self.helmet.amount=1
                            self.inv.append(self.helmet)
          
                        self.helmet=item
                        # Checks if it's a chestplate
                    elif item.typeofitem=="chestplate":
                        # If what the player is currently wearing is in the inventory increase the amount of it in inventory
                        # (So items can be stackable)
                        if self.chestplate in self.inv:
                            pos=self.inv.index(self.chestplate)
                            self.inv[pos].amount+=1
                        # If not in the inventory set the amount to 1 and add the new item to inventory
                        else:
                            self.chestplate.amount=1
                            self.inv.append(self.chestplate)
          
                        self.chestplate=item
                        # Checks if it's leggings
                    elif item.typeofitem=="leggings":
                        # If what the player is currently wearing is in the inventory increase the amount of it in inventory
                        # (So items can be stackable)
                        if self.leggings in self.inv:
                            pos=self.inv.index(self.leggings)
                            self.inv[pos].amount+=1
                        # If not in the inventory set the amount to 1 and add the new item to inventory
                        else:
                            self.leggings.amount=1
                            self.inv.append(self.leggings)
          
                        self.leggings=item
                        # Checks if it's boots
                    elif item.typeofitem=="boots":
                        # If what the player is currently wearing is in the inventory increase the amount of it in inventory
                        # (So items can be stackable)
                        if self.boots in self.inv:
                            pos=self.inv.index(self.boots)
                            self.inv[pos].amount+=1
                        # If not in the inventory set the amount to 1 and add the new item to inventory
                        else:
                            self.boots.amount=1
                            self.inv.append(self.boots)
          
                        self.boots=item
                        # Checks if it's a weapon
                    elif item.typeofitem=="weapon":
                        # If what the player is currently wearing is in the inventory increase the amount of it in inventory
                        # (So items can be stackable)
                        if self.weapon in self.inv:
                            pos=self.inv.index(self.weapon)
                            self.inv[pos].amount+=1
                        # If not in the inventory set the amount to 1 and add the new item to inventory
                        else:
                            self.weapon.amount=1
                            self.inv.append(self.weapon)
          
                        self.weapon=item
                    else:
                        # If it can't be equipped it tells the player and then gives back the item tooken away at the start
                        print("Item cannot be equipped")
                        self.inv[pos].amount+=1
                else:
                    self.inv.remove(item)
                    if item.typeofitem=="helmet":
                        if self.helmet in self.inv:
                            pos=self.inv.index(self.helmet)
                            self.inv[pos].amount+=1
                        else:
                          self.helmet.amount=1
                          self.inv.append(self.helmet)
                        self.helmet=item
                    elif item.typeofitem=="chestplate":
                        if self.chestplate in self.inv:
                            pos=self.inv.index(self.chestplate)
                            self.inv[pos].amount+=1
                        else:
                            self.chestplate.amount=1
                            self.inv.append(self.chestplate)
          
                        self.chestplate=item
                    elif item.typeofitem=="leggings":
                        if self.leggings in self.inv:
                            pos=self.inv.index(self.leggings)
                            self.inv[pos].amount+=1
                        else:
                            self.leggings.amount=1
                            self.inv.append(self.leggings)
          
                        self.leggings=item
                    elif item.typeofitem=="boots":
                        if self.boots in self.inv:
                            pos=self.inv.index(self.boots)
                            self.inv[pos].amount+=1
                        else:
                            self.boots.amount=1
                            self.inv.append(self.boots)
          
                        self.boots=item
                    elif item.typeofitem=="weapon":
                        if self.weapon in self.inv:
                            pos=self.inv.index(self.weapon)
                            self.inv[pos].amount+=1
                        else:
                            self.weapon.amount=1
                            self.inv.append(self.weapon)
          
                        self.weapon=item
                    else:
                        print("Item cannot be equipped")
                        self.inv.append(item)
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

          


player:characters=characters.testSetup('AAAA')
player.showInv()

area1skel=characters("Monster", "Skeleton", 100, 100, 20, 20,25, 0, 20,25, 0,0,3,15,itemDict["skeletonsword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
area1gob=characters("Monster", "Goblin", 80, 80, 40, 40, 15, 5, 20,25, 0,0,3,20,itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
area1orc=characters("Monster", "Orc", 120, 120, 30, 30, 25, 5, 38, 15, 0,0,3,20,itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
