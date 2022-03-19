def shop(player):
    print("Welcome to the shop!")
    while True:
        shopinput = input("\n\nWeapons\nHeal\nleave\n\n")
        shopinput= shopinput.lower()
        # weapons shop
        while True:
            if shopinput=="weapons":
                print("You have "+player.coins+" coins")
                print("\n\n                Woodsword                Stonesword                  IronSword                   Diamondsword")
                print("Attack:         +10                          +20                         +40                         +50")
                print("Cost:           -5                           -10                         -30                         -40\n\n")
                iteminput = input("What weapons do you want?")
                if iteminput=="woodsword" and player.coins>=5:
                    print("purchased sucessfully +10 damage\n\n")
                    userattack+=10
                    player.coins-=5
                    break
                elif iteminput=="stonesword" and player.coins>=10:
                    print("purchased sucessfully +20 damage\n\n")
                    userattack+=20
                    player.coins-=10
                    break
                elif iteminput=="ironsword" and player.coins>=30:
                    print("purchased sucessfully +40 damage\n\n")
                    userattack+=40
                    player.coins-=30
                    break
                elif iteminput=="diamondsword" and player.coins>=40:
                    print("purchased sucessfully +50 damage\n\n")
                    userattack+=50
                    player.coins-=40
                    break
                else:
                    print("That's not a weapon")
                    print("Or you don't have enough coins")
        while True:
            if shopinput=="heal":
                userinput=input("are you sure you want to heal? it costs 10 coins")
                userinput=userinput.lower()
                if userinput=="no":
                    print("see you later!\n\n")
                elif userinput=="yes" and player.coins>=10:
                    player.hp=player.maxhp
                    print("you have been fully healed\n\n")
                    break
            else:
                print("that's not a choice")
                print("Or you don't have enough coins")
        if shopinput=="leave":
            break