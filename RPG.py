from attack import attacks
from character import characters,monlist, inputcheck
from item import items, itemDict
from shop import shop
import colorama
from colorama import Fore,Back,Style, init
import random
import time
init(autoreset=True)


# Finds the info of an item 
def itemInfo(itemname:str):
    # Declares a variable used to determine if item was found
    found=False
    # Looks through the entire dictionary to find if any item names match
    for key,value in itemDict.items():
        if itemname.replace(" ","").lower()==key:
            value.info()
            found=True
    # If the item wasn't found then it prints that the item doesn't exist
    if not found==True:
        print("This item doesn't exist")

def helpmenu():
    typehelp=input("What do you want help with?(shop, player, items, hunting) ").lower()
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
    elif typehelp[:1]=="b":
        print("     Nothing for now")

def basicHelp():
    print("     Here is a basic guide to this game")
    print("     Type: help - for more commands")
    print("     Type: equip (itemname) - to equip items")
    print("     Type: stats - to show stats")
    print("     Type: inventory - to show inventory")
    print("     Type: shop - to go to shop")
    print("     Type: hunt - to hunt monsters")
    print("     Type: info (itemname) - to show info of that item")
    input("OK? ")

def start():
    # print("\n"*100)
    # print("Initializing...")
    # time.sleep(2)
    # print("\n"*100)
    # print("Loading......")
    # time.sleep(1)
    # print("\n"*100)
    # print(Fore.LIGHTYELLOW_EX+"WELCOME TO A GENERIC RPG")
    # basicHelp()
    # print("\n"*100)
    # player=characters.createCharacter()
    player=characters.mageSetup("aaaaaaa")
    print("\nThis is what you look like:")
    player.applystats()
    player.restore()
    player.stats()
    input()
    while True:
        print()
        print("Shop")
        print("Hunt")
        print("Inventory")
        print("Exit")
        pinput=input("What would you like to do? ").lower()
        print()
        if pinput[:1]=="s":
            shop(player)
        elif pinput[:1]=="hu":
            player.battle()
        elif pinput[:1]=="inv":
            player.showInv()
        elif pinput[:2]=="ex":
            break
        elif pinput[:4]=="info":
            itemInfo(pinput.replace(" ","").lower()[4:])
            input()
        else:
            print("That isn't a command")
            basicHelp()

start()
