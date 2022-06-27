from attack import attacks
from character import characters
from character import monlist
from character import inputcheck
from item import items
from item import itemDict
from shop import shop
import colorama
from colorama import Fore,Back,Style
import random
import time


def damageCalc(p:characters,attack:attacks):
    if attack.type=="Physical":
        buff=int(p.strength/2.25)
        damage=attack.damage+buff
        return damage
    elif attack.type=="Magic":
        buff=(p.intelligence/5)/100
        damage=attack.damage*(buff+1)
        return damage
    else:
        print("ERROR")

def monsterSelection():
    m=random.randint(0,2)
    m=monlist[m]
    return m

def battle(p:characters):
    m:characters=monsterSelection()
    m.applystats()
    m.restore()
    print(Fore.LIGHTBLUE_EX+p.name+Style.RESET_ALL+" encounters a "+Fore.YELLOW+m.name)
    while p.hp>0 and m.hp>0:
        # Player selection of moves
        p.attackMenu()
        while True:
            move=inputcheck("Which move would you like to use? ")
            try:
                move:attacks=p.attackmoves[move-1]
                if not move.type=="nonexistent":
                    break
                else:
                    print("Try again with a valid move")
            except IndexError:
                print("Try again with a valid move")
        # Monster selecion of moves
        while True:
            monmove:attacks=random.randint(0,3)
            if not m.attackmoves[monmove].type=="nonexistent":
                monmove=m.attackmoves[monmove]
                break
        damageCalc(m,monmove)
        damageCalc(p,move)
        

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

# start()
player=characters.mageSetup("aaaaaaaaaaa")
player.applystats()
player.restore()
battle(player)