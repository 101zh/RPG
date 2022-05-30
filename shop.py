from numpy import place
from character import characters
import pygame
import item
from item import itemList
pygame.init()
player=characters.testSetup("jafidjsif")
player.coins+=2000

def shop(user):
    print("Welcome to the shop!")
    while True:
        print("\nArmor\nWeapons\nOther Items\n\Leave")
        shopinput = input("What would you like to buy?").lower()
        if shopinput[:2]=="ar":
            print()

        
shop(player)