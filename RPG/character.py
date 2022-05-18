import random
from urllib.parse import parse_qs
import pandas as pd
from item import items

startHelmet=items("helmet","Starter Helmet", 5, 0, 5, 0, -5, -5, True)
startChestplate=items("chestplate","Starter Chestplate", 5, 0, 5, 0, -5, -5, True)
startLeggings=items("leggings","Starter Leggings", 5, 0, 5, 0, -5, -5, True)
startBoots=items("boots","Starter Boots", 5, 0, 5, 0, -5, -5, True)

startStaff=items("weapon", "Wizard Staff", 0, 10, 0, 10, -2, 2, True)
startSword=items("weapon", "Warrior Sword", 0, -5, 0, 0, 8, -4, True)
startDagger=items("weapon", "Rogue's Dagger", 0, -2, 0, -2, 6, 6, True)

null=items("usable", "null", 0, 0, 0, 0, 0, 0, False)

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
        return characters("Mage", name, 85, 85, 125, 125, 15, 25, 15, 20, 0, 20, 0, 25, startStaff, startHelmet, startChestplate, startLeggings, startBoots, [startStaff, startHelmet, startChestplate, startLeggings, startBoots, null])

    def rogueSetup(name):
        return characters("Rogue", name, 100, 100, 70, 70, 18, 15, 18, 25, 0, 20, 0, 25, startDagger, startHelmet, startChestplate, startLeggings, startBoots, [])

    def warriorSetup(name):
        return characters("Warrior", name, 110, 110, 50, 50, 22, 12, 22, 14, 0, 20, 0, 25, startSword, startHelmet, startChestplate, startLeggings, startBoots, [])

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
        print("Coins: "+str(self.coins))
        print("Health: "+str(self.hp)+"/"+str(self.maxhp))
        print("Mana: "+str(self.mana)+"/"+str(self.maxmana))
        print("Speed: "+str(self.speed))
        print("Defense: "+str(self.defense))
        print("Intelligence: "+str(self.intelligence))
        print("Strength: "+str(self.strength))
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
                print(i.name+':')
                print("    HP bonus: "+str(i.hp))
                print("    Mana bonus: "+str(i.mana))
                print("    Defense bonus: "+str(i.defense))
                print("    Intelligence bonus: "+str(i.intelligence))
                print("    Strength bonus: "+str(i.strength))
                print("    Speed bonus: "+str(i.speed))


    # def equip(self, itemname):
    #     for i in self.inv:
    #         if itemname.lower()==i.name.lower():
    #             self.inv.remove(i)
    #             return self.inv
    #unfinished


player=characters.mageSetup("name")

print(player.inv)
player.inv=player.equip("starter boots")
print(player.inv)
