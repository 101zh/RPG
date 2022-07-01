from character import characters
from character import inputcheck
import item
from item import itemDict

# Shop func
def shop(player):
    shoplist=[]
    templist=[]
    uihelp=0
    # Getting all the buyable items for the shop
    for key, value in itemDict.items():
        if value.buyable==True:
            shoplist.append(value)
    
    print("Welcome to the shop!")
    while True:
        print("\nArmor\nWeapons\nOther Items\nLeave")
        shopinput = input("What would you like to buy? ").lower()
        # Armor
        if shopinput[:1]=="a":
            print("\nArmor:")
            # Getting all armor into a list
            for item in shoplist:
                if item.typeofitem=="helmet" or item.typeofitem=="chestplate" or item.typeofitem=="boots" or item.typeofitem=="leggings":
                    templist.append(item)
                    tempamount=range(len(templist))
            
            try:
                # Prints out all armor  
                for item in tempamount:
                    item+=uihelp
                    print(str(templist[item].cost)+"$    "+str(templist[item].name)+"     |   "+str(templist[item+1].cost)+"$    "+str(templist[item+1].name))
                    uihelp+=1
            # When it prints out all armor it will ask what to buy
            except IndexError:
                shopinput=input("\nWhat do you want to buy?(type leave to not buy) ")
                templist=[]
                player.buy(shopinput)
                uihelp=0
        # Weapons
        elif shopinput[:1]=="w":
            print("\nWeapons:")
            # Getting all weapons into a list
            for item in shoplist:
                if item.typeofitem=="weapon":
                    templist.append(item)
                    tempamount=range(len(templist))        
            try:
                # Prints out all weapons  
                for item in tempamount:
                    item+=uihelp
                    print(str(templist[item].cost)+"$    "+str(templist[item].name)+"     |   "+str(templist[item+1].cost)+"$    "+str(templist[item+1].name))
                    uihelp+=1
            # When it prints out all weapons it will ask what to buy
            except IndexError:
                shopinput=input("\nWhat do you want to buy?(type info (itemname) to get info of that item ) ")
                templist=[]
                player.buy(shopinput)
                uihelp=0
        # Other items(Potions)
        elif shopinput[:1]=="o":
            print("\nOther Items:")
            # Getting all other items into a list
            for i in shoplist:
                if i.typeofitem=="usable" and i.buyable==True:
                    templist.append(i)
                    tempamount=range(len(templist))        
            try:  
                # Prints out all other items 
                for item in tempamount:
                    item+=uihelp
                    print(str(templist[item].cost)+"$    "+str(templist[item].name)+"     |   "+str(templist[item+1].cost)+"$    "+str(templist[item+1].name))
                    uihelp+=1
            # When it prints out all other items it will ask what to buy
            except IndexError:
                shopinput=input("\nWhat do you want to buy?(type leave to not buy) ")
                templist=[]
                player.buy(shopinput)
                uihelp=0
        # Leave the shop
        elif shopinput[:1]=="l":
          print("Bye! Come back again!\n")
          break

