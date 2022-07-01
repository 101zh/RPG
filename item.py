import colorama
from colorama import Fore, Back, Style
itemDict={}

class items:
    def __init__(self,name:str, buyable:bool,  typeofitem:str, hp:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, cost:float, amount:int, color):
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
        self.color= color
        itemDict[self.name.replace(" ","").lower()]= self
    # Displays info of item
    def info(self):
        print(self.name+"'s stats")
        print(Fore.LIGHTRED_EX+"❤ HP bonus: "+str(self.hp)+Fore.LIGHTYELLOW_EX+"            Cost: "+str(self.cost))
        print(Fore.LIGHTGREEN_EX+"❈ Defense bonus: "+str(self.defense))
        print(Fore.LIGHTBLUE_EX+"🕮  Mana bonus: "+str(self.mana))
        print(Fore.BLUE+"✎ Intelligence bonus: "+str(self.intelligence))
        print(Fore.RED+"❁ Strength bonus: "+str(self.strength))
        print("✦ Speed bonus: "+str(self.speed))

    # Finds the info of an item 
    def itemInfo(itemname):
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

none=items("                       ", False,"null", 0, 0, 0, 0, 0, 0, 0, 0, Fore.WHITE)

startHelmet=items("Starter Helmet         ",True,"helmet", 5 , 0, 5, 0, -1, -1, 10, 1,Fore.WHITE)
startChestplate=items("Starter Chestplate     ",True,"chestplate", 5 , 0, 5, 0, -1, -1, 10, 1,Fore.WHITE)
startLeggings=items("Starter Leggings       ",True,"leggings", 5 , 0, 5, 0, -1, -1, 10, 1,Fore.WHITE)
startBoots=items("Starter Boots          ",True,"boots", 5 , 0, 5, 0, -1, -1, 10, 1,Fore.WHITE)

skelsword=items("Skeleton Sword         ", True,"weapon", 0, 15, 0, 0, 8, -4, 5, 1,Fore.WHITE)

wizardHat=items("Wizard Hat             ",True,"helmet", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)
wizardRobe=items("Wizard Robe            ",True,"chestplate", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)
wizardPants=items("Wizard Pants           ",True,"leggings", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)
wizardBoots=items("Wizard Boots           ",True,"boots", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)

startStaff=items("Wizard's Staff         ", True,"weapon", 0, 10, 0, 10, -2, 2, 5, 1,Fore.WHITE)
startSword=items("Warrior's Sword        ", True,"weapon", 0, -5, 0, 0, 8, -4, 5, 1,Fore.WHITE)
startDagger=items("Rogue's Dagger         ", True,"weapon", 0, -2, 0, -2, 6, 6, 5, 1,Fore.WHITE)

shppot=items("Small Health Potion    ", True, "usable", 35,0,0,0,0,0,10, 1,Fore.LIGHTRED_EX)
lhppot=items("Large Health Potion    ", True, "usable", 75,0,0,0,0,0,20, 1,Fore.LIGHTRED_EX)
smppot=items("Small Mana Potion      ", True, "usable", 0,35,0,0,0,0,10, 1,Fore.LIGHTBLUE_EX)
lmppot=items("Large Mana Potion      ", True, "usable", 0,75,0,0,0,0,20, 1,Fore.LIGHTBLUE_EX)

null=items("null                   ",False, "weapon", 0, 0, 0, 0, 0, 0, 0, 1,Fore.WHITE)
nullpotion=items("null potion            ",False, "usable", 0, 0, 0, 0, 0, 0, 0, 1,Fore.WHITE)
nullBoots=items("null boots             ", False,"boots", 0, 0, 0, 0, 0, 0, 0, 1,Fore.WHITE)


# Used to make sure all strings have the same amount of spaces
# items("                       ", False,"null", 0, 0, 0, 0, 0, 0, 0, 0)

# items("Starter Helmet         ",True,"helmet", 5 , 0, 5, 0, -2, -2, 10, 1,Fore.WHITE)
# items("Starter Chestplate     ",True,"chestplate", 5 , 0, 5, 0, -2, -2, 10, 1,Fore.WHITE)
# items("Starter Leggings       ",True,"leggings", 5 , 0, 5, 0, -2, -2, 10, 1,Fore.WHITE)
# items("Starter Boots          ",True,"boots", 5 , 0, 5, 0, -2, -2, 10, 1,Fore.WHITE)

# items("Skeleton Sword         ", True,"weapon", 0, 15, 0, 0, 8, -4, 5, 1,Fore.WHITE)

# items("Wizard Hat             ",True,"helmet", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)
# items("Wizard Robe            ",True,"chestplate", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)
# items("Wizard Pants           ",True,"leggings", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)
# items("Wizard Boots           ",True,"boots", 5, 20, -5, 5, -5, 4, 20, 1,Fore.WHITE)

# items("Wizard's Staff         ", True,"weapon", 0, 10, 0, 10, -2, 2, 5, 1,Fore.WHITE)
# items("Warrior's Sword        ", True,"weapon", 0, -5, 0, 0, 8, -4, 5, 1,Fore.WHITE)
# items("Rogue's Dagger         ", True,"weapon", 0, -2, 0, -2, 6, 6, 5, 1,Fore.WHITE)

# items("Small Health Potion    ", True, "usable", 25,0,0,0,0,0,10, 1,Fore.WHITE)
# items("Large Health Potion    ", True, "usable", 50,0,0,0,0,0,20, 1,Fore.WHITE)
# items("Small Mana Potion      ", True, "usable", 0,25,0,0,0,0,10, 1,Fore.WHITE)
# items("Large Mana Potion      ", True, "usable", 0,50,0,0,0,0,20, 1,Fore.WHITE)

# items("null                   ",False, "weapon", 0, 0, 0, 0, 0, 0, 0, 1,Fore.WHITE)
# items("null potion            ",False, "usable", 0, 0, 0, 0, 0, 0, 0, 1,Fore.WHITE)
# items("null boots             ", False,"boots", 0, 0, 0, 0, 0, 0, 0, 1,Fore.WHITE)
