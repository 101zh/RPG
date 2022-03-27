from numpy import place
from character import characters
import pygame
pygame.init()
player=characters.mageSetup("jafidjsif")
player.coins+=2000

def shop(user):
    print("Welcome to the shop!")
    while True:
        shopinput = input("\nWeapons\nHeal\nleave\n")
        shopinput= shopinput.lower()
        # weapons shop
        if shopinput=="weapons":
            while True:
                shopinput=""
                print("You have "+str(user.coins)+" coins")
                print("\n\n                Woodsword                Stonesword                  IronSword                   Diamondsword")
                print("Attack:         +10                          +20                         +40                         +50")
                print("Cost:           -5                           -10                         -30                         -40\n\n")
                iteminput = input("What weapons do you want? ")
                if iteminput=="woodsword" and user.coins>=5:
                    print("purchased sucessfully +10 damage\n\n")
                    user.strength+=10
                    user.coins-=5
                    break
                elif iteminput=="stonesword" and user.coins>=10:
                    print("purchased sucessfully +20 damage\n\n")
                    user.strength+=20
                    user.coins-=10
                    break
                elif iteminput=="ironsword" and user.coins>=30:
                    print("purchased sucessfully +40 damage\n\n")
                    user.strength+=40
                    user.coins-=30
                    break
                elif iteminput=="diamondsword" and user.coins>=40:
                    print("purchased sucessfully +50 damage\n\n")
                    user.strength+=50
                    user.coins-=40
                    break
                else:
                    print("\nThat's not a weapon")
                    print("Or you don't have enough coins\n")
                    pygame.time.wait(1000)
        elif shopinput=="heal":
            while True:
                shopinput=""
                print("You have "+str(user.coins)+" coins")
                userinput=input("are you sure you want to heal? it costs 10 coins ")
                userinput=userinput.lower()
                if userinput=="no" or "n":
                    print("Oh ok\n\n")
                    break
                elif userinput=="yes" and user.coins>=10:
                    user.hp=user.maxhp
                    print("You have been fully healed\n\n")
                    break
                else:
                    print("\nThat's not a choice")
                    print("Or you don't have enough coins\n")
                    pygame.time.wait(1000)
        elif shopinput=="leave":
            print("See you later!\n\n")
            break
        else:
            print("That's not a choice")
            pygame.time.wait(1000)

shop(player)