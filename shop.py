from numpy import place
from character import characters
import pygame
pygame.init()
player=characters.mageSetup("jafidjsif")
player.coins+=2000

def shop():
    print("Welcome to the shop!")
    while True:
        shopinput = input("\nArmor\nWeapons\nOther Items")
        shopinput= shopinput.lower()
        
shop(player)