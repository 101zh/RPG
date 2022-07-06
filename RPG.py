import numpy
from attack import attacks, attackDict
from character import characters,monlist, inputcheck
from item import items, itemDict
from shop import shop
import colorama
import pandas as pd
from areas import area, areaDict
from colorama import Fore,Back,Style, init
import random
import time
init(autoreset=True)


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
        print("     Type: equip (itemname) - to equip items")
        print("     Type: use (itemname) - to use that item")
    elif typehelp[:1]=="b":
        print("1: Attack")
        print("2: Use an item")
        print("3: Status")
        print("4: Run")

def saveExit(p:characters):
    save= pd.read_csv("RPG\savefile.csv", index_col="col0")
    loops=1
    p=p.__dict__
    for key,data in p.items():
        if loops<=20:
            save.iloc[0, loops-1] = data
            loops+=1
    invstr=""
    attackstr=""
    for i in p["inv"]:
        invstr+=i.name.replace(" ","").lower()+" "
    for i in p["attackmoves"]:
        attackstr+=i.name.replace(" ","").lower()+" "
    save.loc['player', 'area']=p['area'].areanum
    save.loc['player', 'weapon']=p["weapon"].name.replace(" ","").lower()
    save.loc['player', 'helmet']=p["helmet"].name.replace(" ","").lower()
    save.loc['player', 'chestplate']=p["chestplate"].name.replace(" ","").lower()
    save.loc['player', 'boots']=p["boots"].name.replace(" ","").lower()
    save.loc['player', 'leggings']=p["leggings"].name.replace(" ","").lower()
    save.loc['player', 'inv']=invstr
    save.loc['player', 'attackmoves']=attackstr
    save.to_csv('RPG\savefile.csv')

def load():
    save=pd.read_csv("RPG\savefile.csv", index_col="col0")
    print(save.iloc[0,0])
    if not save.loc["player","rpgclass"]=="new":
        statslist=[]
        for i in range(26):
            statslist.append(save.iloc[0,i])
            print(statslist)
        inv=save.loc["player","inv"].rstrip()
        inventory=inv.split(" ")
        for i in inventory:
            inventory[inventory.index(i)]=itemDict[i]
        moves=save.loc["player", "attackmoves"].rstrip()
        moves=moves.split(" ")
        for i in moves:
            moves[moves.index(i)]=attackDict[i]
        while len(moves)<4:
            moves.append(itemDict[""])
        return characters(statslist[0],statslist[1],statslist[2],statslist[3],statslist[4],statslist[5],statslist[6],statslist[7],statslist[8],statslist[9],statslist[10],statslist[11],statslist[12],statslist[13],statslist[14],statslist[15],statslist[16],statslist[17],statslist[18],statslist[19],areaDict[statslist[20]],itemDict[statslist[21]],itemDict[statslist[22]],itemDict[statslist[23]],itemDict[statslist[24]],itemDict[statslist[25]], inventory, moves)
    return False

def basicHelp():
    print("     Here is a basic guide to this game")
    print("     Type: help - for more commands")
    print("     Type: equip (itemname) - to equip items")
    print("     Type: stats - to show stats")
    print("     Type: inventory - to show inventory")
    print("     Type: shop - to go to shop")
    print("     Type: hunt - to hunt monsters")
    print("     Type: info (itemname) - to show info of that item")
    print("     Type: movearea (areanum) - to move to that area")
    input("OK? ")

def start():
    print("\n"*100)
    print("Initializing...")
    for key, data in areaDict:
        data.init(monlist, itemDict)
    time.sleep(2)
    print("\n"*100)
    print("Loading......")
    time.sleep(1)
    print("\n"*100)
    print(Fore.LIGHTYELLOW_EX+"WELCOME TO A GENERIC RPG")
    basicHelp()
    print("\n"*100)
    if load():
        player=characters.createCharacter()
        player.area=areaDict[1]
        print("\nThis is what you look like:")
        player.applystats()
        player.restore()
        player.stats()
        input()
    else:
        player=load()
    while True:
        print()
        print("Shop")
        print("Hunt")
        print("Inventory")
        print("Exit")
        pinput=input("What would you like to do? ").replace(" ","").lower()
        print()
        if pinput[:1]=="s":
            shop(player)
        elif pinput[:1]=="hu":
            player.battle()
        elif pinput[:1]=="inv":
            player.showInv()
            pinput=input("What item do you want to use? ").replace(" ","").lower()
            if not pinput=="":
                player.use(pinput)
        elif pinput[:2]=="ex":
            saveExit(player)
            break
        elif pinput[:4]=="info":
            items.itemInfo(pinput[4:])
            input()
        elif pinput[:3]=="use":
            player.use(pinput[3:])
        elif pinput[:5]=="equip":
            player.equip(pinput[5:])
        elif pinput[:8]=="movearea":
            try:
                player.moveArea(int(pinput[8:]))
            except ValueError:
                print("Type in a number")
        elif pinput[:2]=="he":
            help()
        else:
            print("That isn't a command")
            basicHelp()

start()

