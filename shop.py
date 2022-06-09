from re import A, T
from numpy import True_, place
from character import characters
import item
from item import itemDict
player=characters.testSetup("jafidjsif")
player.coins+=2000

def inputcheck(message:str):
    while True:
        try:
            message=int(input(message))
            break
        except ValueError:
            print("Try again with a num")
    return message

def shop(player):
    shoplist=[]
    templist=[]
    for key, value in itemDict.items():
        temp=value
        shoplist.append(temp)
    print("Welcome to the shop!")
    while True:
        print("\nArmor\nWeapons\nOther Items\nLeave")
        shopinput = input("What would you like to buy? ").lower()
        if shopinput[:1]=="a":
            pages=inputcheck("Which page do you want to go to? (1-2 pages) ")
            print("\nArmor:")
            pages*=4
            for i in shoplist:
                if i.buyable==True and (i.typeofitem=="helmet" or i.typeofitem=="chestplate" or i.typeofitem=="boots" or i.typeofitem=="leggings"):
                    templist.append(i)
                    tempamount=range(len(templist))        
            for armor in tempamount:
                if armor<pages and armor>pages-5:
                    print(str(templist[armor].cost)+"$    "+str(templist[armor].name))
            shopinput=input("\nWhat do you want to buy?(type leave to not buy) ")
            player.buy(shopinput)
        elif shopinput[:1]=="w":
            print("\nWeapons:")
            for i in shoplist:
                if i.typeofitem=="weapon" and i.buyable==True:
                    print(str(i.cost)+"$    "+str(i.name))
            shopinput=input("\nWhat do you want to buy? (type leave not buy) ")
            player.buy(shopinput)
        elif shopinput[:1]=="o":
            print("\nOther Items:")
            for i in shoplist:
                if i.typeofitem=="usable" and i.buyable==True:
                    print(str(i.cost)+"$    "+str(i.name))
            shopinput=input("\nWhat do you want to buy? (type leave not buy) ")
            player.buy(shopinput)
        elif shopinput[:1]=="l":
          print("Bye! Come back again!\n")
          break

# player.stats()
# player.showInv()
shop(player)
# player.stats()
# player.showInv()
