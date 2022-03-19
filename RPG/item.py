class items:
    def __init__(self, typeofitem:str, name:str, hp:int, mana:int, defense:int, intelligence:int, strength:int, speed:int, equip:bool):
        self.typeofitem=typeofitem
        self.name=name
        self.hp=hp
        self.mana=mana
        self.defense=defense
        self.intelligence=intelligence
        self.strength=strength
        self.speed=speed
        self.equip=equip
        

    def info(self, character):
        print(self.name+"'s stats")
        print("HP bonus: "+str(self.hp))
        print("Defense bonus: "+str(self.defense))
        print("Mana bonus: "+str(self.mana))
        print("Intelligence bonus: "+str(self.intelligence))
        print("Strength bonus: "+str(self.strength))
        print("Speed bonus: "+str(self.speed))
        print("Equipped: "+str(self.equip))