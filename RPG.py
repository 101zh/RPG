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
    print("Here is a basic guide to this game")
    print()

while True:
    print("Initializing...")
    time.sleep(2)
    print("\n"*20)
    print("Loading......")
    time.sleep(1)
    print("\n"*20)
    print(Fore.LIGHTYELLOW_EX+"WELCOME TO A GENERIC RPG")
    print("     Here is a basic guide to this game")
    print("     Type: help - for this menu")
    print("     Type: equip (num) - to equip items")
    print("     Type: stats - to show stats")
    print("     Type: showinv - to show inventory")
    print("     Type: info (itemname) - to show info of that item")
    input("OK? ")
    print("\n"*20)
    player=characters.createCharacter()
    break