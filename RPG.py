from character import characters
from item import items
from item import itemDict
from shop import shop
import colorama
from colorama import Fore,Back,Style
import random
import time

def battle(p):
    print("not ready yet...")

def helpmenu():
    typehelp=input("What do you want help with?(shop, player, items) ").lower()
    if typehelp[:1]=="s":
        print("     Type: buy (item) - to buy an item")
        print("     Type: shop - to visit the shop")
        print("     Type: info (itemname) - to show info of that item")
    elif typehelp[:1]=="i":
        print("     Type: info (itemname) - to show info of that item")
        print("     Type: equip (itemname) - to equip items")
        print("     Type: use (itemname) - to use that item")
    elif typehelp[:1]=="p":
        print("     Type: stats - to show stats")
        print("     Type: showinv - to show inventory")


while True:
    print("\n"*100)
    print("Initializing...")
    time.sleep(2)
    print("\n"*100)
    print("Loading......")
    time.sleep(1)
    print("\n"*100)
    print(Fore.LIGHTYELLOW_EX+"WELCOME TO A GENERIC RPG")
    print("     Here is a basic guide to this game")
    print("     Type: help - for more commands")
    print("     Type: equip (itemname) - to equip items")
    print("     Type: stats - to show stats")
    print("     Type: showinv - to show inventory")
    print("     Type: info (itemname) - to show info of that item")
    input("OK? ")
    print("\n"*100)
    player=characters.createCharacter()
    print("\nThis is what you look like:")
    player.stats()

    break