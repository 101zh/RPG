from attack import attacks
from character import characters,monlist, inputcheck
from item import items, itemDict
from shop import shop
import colorama
from colorama import Fore,Back,Style, init
import random
import time
init(autoreset=True)

def damageCalc(p:characters,attack:attacks, m:characters):
    if p.rpgclass=="Monster":
        mondescrip=3
    crit=random.randint(1,1000)
    crit=crit<p.speed*15
    miss=random.randint(1,1000)
    miss=miss<m.speed*66
    attackmessage=attack.descrip[0+mondescrip]
    if attack.type=="Physical":
        buff=int(p.strength/2.25)
        damage=int(attack.damage+buff)
    elif attack.type=="Magic":
        buff=(p.intelligence/5)/100
        damage=int(attack.damage*(buff+1))
    else:
        print("ERROR")
    if crit:
        attackmessage=attack.descrip[1+mondescrip]
        damage=int(damage*1.6)
    if miss:
        return [0,attack.descrip[2+mondescrip]]
    else:
        return [damage,attackmessage]

def monsterSelection():
    m=random.randint(0,2)
    m=monlist[m]
    return m

def battleCheck(p:characters,m:characters):
    if m.isDead() and p.isDead():
        print("You both are close to dying")
        print("You are forced to run away")
        return True
    elif m.isDead():
        print("You died...")
        print("You were still able to escape")
        return True
    elif p.isDead():
        print("The "+m.name+" is dead!")
        reward=random.randint(5,20)
        print("You Won! You found "+Fore.YELLOW+str(reward)+" coins")
        return True
    return False

def battle(p:characters):
    m:characters=monsterSelection()
    m.applystats()
    m.restore()
    print(Fore.LIGHTBLUE_EX+p.name+Style.RESET_ALL+" encounters a "+Fore.YELLOW+m.name)
    while p.hp>0 and m.hp>0:
        # Player selection of moves
        print("1: Attack\n2: Use an item\n3: Run")
        battleinput=inputcheck("What would you like to do? ")
        if battleinput==1:
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
            # Calculates damage for both sides
            monmove=damageCalc(m,monmove, p)
            move=damageCalc(p,move, m)
            # If player speed> monster speed: player attacks first
            if p.speed>m.speed:
                m.hp-=move[0]
                # Printing the attack move and then checking for death
                print(move[1])
                if battleCheck(p,m):
                    break
                p.hp-=monmove[0]
                # Printing the attack move and then checking for death
                print(monmove[1])
                if battleCheck(p,m):
                    break
                print()
            # If monster speed > player speed: monster attacks first
            elif m.speed>p.speed:
                p.hp-=monmove[0]
                print(monmove[1])                
                if battleCheck(p,m):
                    break
                m.hp-=move[0]
                print(move[1])
                if battleCheck(p,m):
                    break
            # If monster speed==player speed(process of elimination): attack at the same time
            else:
                p.hp-=monmove[0]
                m.hp-=move[0]
                print(move[1])
                print(monmove[1])
                if battleCheck(p,m):
                    break
        elif battleinput==2:
            p.showInv()



        

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