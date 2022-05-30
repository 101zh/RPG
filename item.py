import colorama
from colorama import Fore, Back, Style
itemDict={}

class items:
    def __init__(self, typeofitem:str, name:str, hp:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, cost:float):
        self.typeofitem=typeofitem
        self.name=name
        self.hp=hp
        self.mana=mana
        self.defense=defense
        self.intelligence=intelligence
        self.strength=strength
        self.speed=speed
        self.cost=cost
        itemDict[self.name.lower()]= self

    def info(self):
        print(self.name+"'s stats")
        print(Fore.LIGHTRED_EX+"❤ HP bonus: "+str(self.hp)+Fore.LIGHTYELLOW_EX+"            Cost: "+str(self.cost))
        print(Fore.LIGHTGREEN_EX+"❈ Defense bonus: "+str(self.defense))
        print(Fore.LIGHTBLUE_EX+"🕮  Mana bonus: "+str(self.mana))
        print(Fore.BLUE+"✎ Intelligence bonus: "+str(self.intelligence))
        print(Fore.RED+"❁ Strength bonus: "+str(self.strength))
        print("✦ Speed bonus: "+str(self.speed))

startHelmet=items("helmet","Starter Helmet", 5, 0, 5, 0, -5, -5, 5)
startChestplate=items("chestplate","Starter Chestplate", 5, 0, 5, 0, -5, -5, 5)
startLeggings=items("leggings","Starter Leggings", 5, 0, 5, 0, -5, -5, 5)
startBoots=items("boots","Starter Boots", 5, 0, 5, 0, -5, -5, 5)

startStaff=items("weapon", "Wizard's Staff", 0, 10, 0, 10, -2, 2, 5)
startSword=items("weapon", "Warrior's Sword", 0, -5, 0, 0, 8, -4, 5)
startDagger=items("weapon", "Rogue's Dagger", 0, -2, 0, -2, 6, 6, 5)

null=items("weapon", "null", 0, 0, 0, 0, 0, 0, 0)
nullBoots=items("boots", "null boots", 0, 0, 0, 0, 0, 0, 0)