from numpy import True_, place
from character import characters
import item
from item import itemDict
player=characters.testSetup("jafidjsif")
player.coins+=2000


def shop():
    shoplist=[]
    for key, value in itemDict.items():
        temp=value
        shoplist.append(temp)
    print("Welcome to the shop!")
    while True:
        print("\nArmor\nWeapons\nOther Items\nLeave")
        shopinput = input("What would you like to buy? ").lower()
        if shopinput[:2]=="a":
            print("\nArmor:")
            for i in shoplist:
                if i.buyable==True and (i.typeofitem=="helmet" or i.typeofitem=="chestplate" or i.typeofitem=="boots" or i.typeofitem=="leggings"):
                    print(str(i.name))
        elif shopinput[:1]=="w":
            print("\nWeapons:")
            for i in shoplist:
                if i.typeofitem=="weapon" and i.buyable==True:
                    print(str(i.name))
        elif shopinput[:1]=="o":
            print("\nOther Items:")
            for i in shoplist:
                if i.typeofitem=="usable" and i.buyable==True:
                    print(str(i.name))
        elif shopinput[:1]=="l":
          print("Bye! Come back again!\n")
          break

        
        
shop()