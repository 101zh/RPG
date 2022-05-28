import colorama
from colorama import Fore, Back, Style


class items:
    def __init__(self, typeofitem:str, name:str, hp:int, mana:int, defense:int, intelligence:int, strength:int, speed:int):
        self.typeofitem=typeofitem
        self.name=name
        self.hp=hp
        self.mana=mana
        self.defense=defense
        self.intelligence=intelligence
        self.strength=strength
        self.speed=speed

    def info(self):
        print(self.name+"'s stats")
        print(Fore.LIGHTRED_EX+"❤ HP bonus: "+str(self.hp))
        print(Fore.LIGHTGREEN_EX+"❈ Defense bonus: "+str(self.defense))
        print(Fore.LIGHTBLUE_EX+"🕮  Mana bonus: "+str(self.mana))
        print(Fore.BLUE+"✎ Intelligence bonus: "+str(self.intelligence))
        print(Fore.RED+"❁ Strength bonus: "+str(self.strength))
        print("✦ Speed bonus: "+str(self.speed))