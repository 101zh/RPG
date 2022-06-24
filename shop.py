from character import characters
from character import inputcheck
import item
from item import itemDict
player=characters.testSetup("jafidjsif")
player.coins+=2000


def shop(player):
    shoplist=[]
    templist=[]
    guihelp=0
    for key, value in itemDict.items():
        temp=value
        shoplist.append(temp)
    print("Welcome to the shop!")
    while True:
        print("\nArmor\nWeapons\nOther Items\nLeave")
        shopinput = input("What would you like to buy? ").lower()
        if shopinput[:1]=="a":
            print("\nArmor:")
            for i in shoplist:
                if i.buyable==True and (i.typeofitem=="helmet" or i.typeofitem=="chestplate" or i.typeofitem=="boots" or i.typeofitem=="leggings"):
                    templist.append(i)
                    tempamount=range(len(templist))
            try:  
                for item in tempamount:
                    item+=guihelp
                    print(str(templist[item].cost)+"$    "+str(templist[item].name)+"     |   "+str(templist[item+1].cost)+"$    "+str(templist[item+1].name))
                    guihelp+=1
            except IndexError:
                shopinput=input("\nWhat do you want to buy?(type leave to not buy) ")
                templist=[]
                player.buy(shopinput)
                guihelp=0
        elif shopinput[:1]=="w":
            print("\nWeapons:")
            for i in shoplist:
                if i.typeofitem=="weapon" and i.buyable==True:
                    templist.append(i)
                    tempamount=range(len(templist))        
            try:  
                for item in tempamount:
                    item+=guihelp
                    print(str(templist[item].cost)+"$    "+str(templist[item].name)+"     |   "+str(templist[item+1].cost)+"$    "+str(templist[item+1].name))
                    guihelp+=1
            except IndexError:
                shopinput=input("\nWhat do you want to buy?(type leave to not buy) ")
                templist=[]
                player.buy(shopinput)
                guihelp=0
        elif shopinput[:1]=="o":
            print("\nOther Items:")
            for i in shoplist:
                if i.typeofitem=="usable" and i.buyable==True:
                    templist.append(i)
                    tempamount=range(len(templist))        
            try:  
                for item in tempamount:
                    item+=guihelp
                    print(str(templist[item].cost)+"$    "+str(templist[item].name)+"     |   "+str(templist[item+1].cost)+"$    "+str(templist[item+1].name))
                    guihelp+=1
            except IndexError:
                shopinput=input("\nWhat do you want to buy?(type leave to not buy) ")
                templist=[]
                player.buy(shopinput)
                guihelp=0
        elif shopinput[:1]=="l":
          print("Bye! Come back again!\n")
          break


# shop(player)

