from numpy import place
from character import characters
import pygame
import item
from item import itemDict
pygame.init()
player=characters.testSetup("jafidjsif")
player.coins+=2000
print(itemDict)

def shop(user):
    shoplist=[]
    for key, value in itemDict.items():
        temp=value
        shoplist.append(value)
    print("Welcome to the shop!")
    while True:
        print("\nArmor\nWeapons\nOther Items\nLeave")
        shopinput = input("What would you like to buy? ").lower()
        if shopinput[:2]=="ar":
            for i in shoplist:
                print(str(i.name))

        
        
shop(player)