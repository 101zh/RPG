userhealth=100
userbackuphealth=100
userattack=25
userxp=0
money=15
iteminput="empty"
monsterhealth=100
mosnterbackuphealth=100
monsterattack=15
import random

# started at 7:49 6/17 8:20
user = input("What is your name?")
print("\nDon't use caps when typing")
print('\n\ntype attack to attack            type shop to Shop           type help for help      type stats to check your stats\n\n')

while True:
    userinput = input("What do you want to do?\n")
    if userinput=="attack":
        print("\n\n"+user+" has encountered a goblin with health")
        while True:
            if userhealth==0:
                a=1
                b=10
                loss=random.randrange(a, b+1)
                loss=str(loss)
                print("you have died you lost "+loss+" coins\n\n")
                loss=int(loss)
                money-=loss
                userhealth=userbackuphealth
                monsterhealth=mosnterbackuphealth
                break
            elif monsterhealth==0:
                a=9
                b=20
                reward=random.randrange(a, b+1)
                reward=str(reward)
                print("you have defeated the monster and you recieved "+reward+" coins\n\n")
                reward=int(reward)
                money+=reward
                mosnterbackuphealth+=10
                monsterhealth=mosnterbackuphealth
                monsterattack+=5
                break
            attackinput=input("You can Run or attack what do you want to do?\n\n")
            if attackinput=="attack":
                userattack=str(userattack)
                print("you swung your sword and dealed "+userattack+" damage\n\n")
                userattack=int(userattack)
                monsterhealth-=userattack
                monsterattack=str(monsterattack)
                print("The monster hits back and deals "+monsterattack+" damaged\n\n")
                monsterattack=int(monsterattack)
                userhealth-=monsterattack
            elif attackinput=="run":
                print("coward! you ran away from the fight loosing 1 coin")
                money-=1
                break
    # shop
    elif userinput=="shop":
        while True:
            shopinput = input("\n\nWeapons\nHealth\nHeal\nleave\n\n")
            # weapons shop
            if shopinput=="weapons":
                print("\n\n                Woodsword                Stonesword                  IronSword                   Diamondsword")
                print("Attack:         +10                          +20                         +40                         +50")
                print("Cost:           -5                           -10                         -30                         -40\n\n")
                iteminput = input("What weapons do you want?")
                if money < 5:
                    print("You don't have enought money Bro")
                elif iteminput=="woodsword":
                    print("purchased sucessfully +10 damage\n\n")
                    userattack+=10
                    money-=5
                    break
                elif money < 10:
                    print("You don't have enought money Bro")
                elif iteminput=="stonesword":
                    print("purchased sucessfully +20 damage\n\n")
                    userattack+=20
                    money-=10
                    break
                elif money < 30:
                    print("You don't have enought money Bro")
                elif iteminput=="ironsword":
                    print("purchased sucessfully +40 damage\n\n")
                    userattack+=40
                    money-=30
                    break
                elif money < 40:
                    print("You don't have enought money Bro")
                elif iteminput=="diamondsword":
                    print("purchased sucessfully +50 damage\n\n")
                    userattack+=50
                    money-=40
                    break
                else:
                    print("Bro that's not a weapon")
                # Health shop
            elif shopinput=="health":
                print("\n\n             +10 Health              +25 Health              +50 Health              +100 Health")
                print("Cost:            -20                     -50                     -100                     -200\n\n")
                iteminput = input("How much health do you want? Type out the the number of health you want(do not type the + or health)")
                if money < 20:
                    print("You don't have enought money Bro")
                elif iteminput=="10":
                    print("purchased sucessfully +10 Health\n\n")
                    userhealth+=10
                    userbackuphealth+=10
                    money-=20
                    break
                elif money < 50:
                    print("You don't have enought money Bro")
                elif iteminput=="25":
                    print("purchased sucessfully +25 Health\n\n")
                    userhealth+=25
                    userbackuphealth+=25
                    money-=50
                    break
                elif money < 100:
                    print("You don't have enought money Bro")
                elif iteminput=="50":
                    print("purchased sucessfully +50 Health\n\n")
                    userhealth+=50
                    userbackuphealth+=50
                    money-=100
                    break
                elif money < 200:
                    print("You don't have enought money Bro")
                elif iteminput=="100":
                    print("purchased sucessfully +100 Health\n\n")
                    userhealth+=100
                    userbackuphealth+=100
                    money-=200
                    break
                else:
                    print("Bro that's not a valid number")
            elif shopinput=="leave":
                print("you left the shop\n\n")
                break
            elif shopinput=="heal":
                userinput=input("are you sure you want to heal? it costs 10 coins")
                if userinput=="no":
                    print("see you later!\n\n")
                    break
                elif money<10:
                    print("you don't have enough money\n\n")
                    break
                elif userinput=="yes":
                    userhealth=userbackuphealth
                    print("you have been fully healed\n\n")
                    break

            else:
                print("that's not a choice")
    # this is Help
    elif userinput=="help":
        print('\n\ntype attack to attack       type shop to Shop       type help for help       type stats to check your stats\n\n')
        print("\nDon't use caps when typing")
    # shows the stats of a player
    elif userinput=="stats":
        userhealth=str(userhealth)
        userbackuphealth=str(userbackuphealth)
        userattack=str(userattack)
        money=str(money)
        print(user+"'s stats")
        print("\n\n"+userhealth+"/"+userbackuphealth+" Health")
        print(userattack+" Attack")
        print(money+ " Money\n\n")
        userhealth=int(userhealth)
        userbackuphealth=int(userbackuphealth)
        userattack=int(userattack)
        money=int(money)
    else:
        print("\n\nThat is not a Valid command type help if you need help\n\n")
