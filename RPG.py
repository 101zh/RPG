from character import characters
from item import items
from item import itemDict
from shop import shop
import colorama
from colorama import Fore,Back,Style
import random
import time

def damage(p,m,typeattack):
  print("Not ready")

def battle(p):
    print("not ready yet...")

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


def start():
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
    print("     Type: inventory - to show inventory")
    print("     Type: shop - to go to shop")
    print("     Type: hunt - to hunt monsters")
    print("     Type: info (itemname) - to show info of that item")
    input("OK? ")
    print("\n"*100)
    player=characters.createCharacter()
    print("\nThis is what you look like:")
    player.applystats()
    player.restore()
    player.stats()
    while True:
        player.applystats()
        player.restore()
        print("Shop")
        print("Hunt")
        print("Inventory")
        print("Exit")
        pinput=input("What would you like to do? ").lower()
        if pinput[:1]=="s":
            shop(player)
        elif pinput[:1]=="h":
            battle(player)
        elif pinput[:1]=="inv":
            player.showInv()
        elif pinput[:1]=="ex":
            break

start()