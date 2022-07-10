import colorama
from colorama import Fore, Back, Style
from areas import area, areaDict

itemDict={}

class items:
    def __init__(self,name:str, buyable:bool,  typeofitem:str, hp:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, cost:int, amount:int,area:area,  color):
        self.typeofitem=typeofitem
        self.name=name
        self.hp=hp
        self.mana=mana
        self.defense=defense
        self.intelligence=intelligence
        self.strength=strength
        self.speed=speed
        self.cost=cost
        self.buyable=buyable
        self.amount=amount
        self.area=area
        self.color= color
        itemDict[self.name.replace(" ","").replace("\x1b[7;35;40m", "").replace("\x1b[0m", "").lower()]= self
    # Displays info of item
    def info(self):
        print(self.name+"stats")
        print(Fore.LIGHTRED_EX+"❤ HP bonus: "+str(self.hp)+Fore.LIGHTYELLOW_EX+"            Cost: "+str(self.cost))
        print(Fore.LIGHTGREEN_EX+"❈ Defense bonus: "+str(self.defense))
        print(Fore.LIGHTBLUE_EX+"🕮  Mana bonus: "+str(self.mana))
        print(Fore.BLUE+"✎ Intelligence bonus: "+str(self.intelligence))
        print(Fore.RED+"❁ Strength bonus: "+str(self.strength))
        print("✦ Speed bonus: "+str(self.speed))


    # Finds the info of an item 
    def itemInfo(itemname:str):
        # Declares a variable used to determine if item was found
        found=False
        # Looks through the entire dictionary to find if any item names match
        for key,value in itemDict.items():
            if itemname.replace(" ","").lower()==key:
                value.info()
                found=True
        # If the item wasn't found then it prints that the item doesn't exist
        if not found==True:
            print("This item doesn't exist")


items("                         ",False,"null", 0, 0, 0, 0, 0, 0, 0, 0,[0], Fore.WHITE)

items("Starter Helmet           ",True,"helmet", 5 , 0, 5, 0, -1, -1, 10, 1,[1],Fore.WHITE)
items("Starter Chestplate       ",True,"chestplate", 5 , 0, 5, 0, -1, -1, 10, 1,[1],Fore.WHITE)
items("Starter Leggings         ",True,"leggings", 5 , 0, 5, 0, -1, -1, 10, 1,[1],Fore.WHITE)
items("Starter Boots            ",True,"boots", 5 , 0, 5, 0, -1, -1, 10, 1,[1],Fore.WHITE)

items("Skeleton Sword           ",False,"weapon", 0, 15, 0, 0, 8, -4, 5, 1,[2],Fore.WHITE)

items("Wizard's Staff           ",True,"weapon", 0, 10, 0, 10, 2, 2, 12, 1,[1],Fore.CYAN)
items("Wizard Hat               ",True,"helmet", 5, 20, -5, 5, -5, 4, 20, 1,[2],Fore.LIGHTCYAN_EX)
items("Wizard Robe              ",True,"chestplate", 5, 20, -5, 5, -5, 4, 20, 1,[2],Fore.LIGHTCYAN_EX)
items("Wizard Pants             ",True,"leggings", 5, 20, -5, 5, -5, 4, 20, 1,[2],Fore.LIGHTCYAN_EX)
items("Wizard Boots             ",True,"boots", 5, 20, -5, 5, -5, 4, 20, 1,[2],Fore.LIGHTCYAN_EX)

items("Necromancer Wand         ",False,"weapon", 0, 20, 0, 20, 0, 5, 25, 1,[1],Fore.MAGENTA)
items("Necromancer Hood         ",False,"helmet", 10, 20, 2, 10, 0, -2, 25, 1,[3],Fore.MAGENTA)
items("Necromancer Robe         ",False,"chestplate", 15, 30, 12, 15, -5, -4, 30, 1,[3],Fore.MAGENTA)
items("Necromancer Trousers     ",False,"leggings", 12, 25, 8, 10, 0, 8, 30, 1,[3],Fore.MAGENTA)
items("Necromancer Boots        ",False,"boots", 5, 15, 2, 5, 0, 10, 20, 1,[3], Fore.MAGENTA)


items("Warrior's Sword          ", True,"weapon", 0, -5, 0, 0, 8, -4, 5, 1,[1],Fore.WHITE)
items("Rogue's Dagger           ", True,"weapon", 0, -2, 0, -2, 6, 6, 5, 1,[1],Fore.WHITE)

items("Small Health Potion      ", True, "usable", 35,0,0,0,0,0,10, 1,[1,2,3],Fore.LIGHTRED_EX)
items("Large Health Potion      ", True, "usable", 75,0,0,0,0,0,20, 1,[1,2,3],Fore.LIGHTRED_EX)
items("Small Mana Potion        ", True, "usable", 0,35,0,0,0,0,10, 1,[1,2,3],Fore.LIGHTBLUE_EX)
items("Large Mana Potion        ", True, "usable", 0,75,0,0,0,0,20, 1,[1,2,3],Fore.LIGHTBLUE_EX)
items("Small Restoration Potion ", True, "usable", 35, 50, 0, 0, 0, 0, 40, 1, [2,3], Fore.LIGHTMAGENTA_EX)
items("Calcium Drink            ", False, "usable", 0, 0, 4, 0, 0, 0, 0, 1, [2], Fore.WHITE)

items("ALL POTION               ",False, "usable", 100, 100, 100, 100, 100, 100, 100000, 1,[0],Fore.LIGHTYELLOW_EX)
items("null                     ",False, "weapon", 0, 0, 0, 0, 0, 0, 0, 0,[0],Fore.WHITE)
items("null potion              ",False, "usable", 0, 0, 0, 0, 0, 0, 0, 0,[0],Fore.WHITE)
items("null boots               ", False,"boots", 0, 0, 0, 0, 0, 0, 0, 0,[0],Fore.WHITE)
