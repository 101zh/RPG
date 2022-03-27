from character import characters
import random
import pygame
pygame.init()

# started at 7:49 6/17 8:20
player=characters.createCharacter()

userattack=25
userxp=0
money=15
iteminput="empty"
monsterhealth=100
monstermaxhealth=100
monsterattack=15
print("\nDon't use caps when typing")
print('\n\ntype attack to attack            type shop to Shop           type help for help      type stats to check your stats\n\n')


while True:
    userinput = input("What do you want to do?\n")
    if userinput=="attack":
        print("\n\n"+player.name+" has encountered a goblin with health")
        while True:
            if player.hp<=0:
                a=1
                b=10
                loss=random.randrange(a, b+1)
                loss=str(loss)
                print("you have died you lost "+loss+" coins\n\n")
                loss=int(loss)
                money-=loss
                player.hp=player.maxhp
                monsterhealth=monstermaxhealth
                break
            elif monsterhealth<=0:
                a=9
                b=20
                reward=random.randrange(a, b+1)
                reward=str(reward)
                print("you have defeated the monster and you recieved "+reward+" coins\n\n")
                reward=int(reward)
                money+=reward
                monstermaxhealth+=10
                monsterhealth=monstermaxhealth
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
                player.hp-=monsterattack
            elif attackinput=="run":
                print("coward! you ran away from the fight loosing 1 coin")
                money-=1
                break
    # shop
    elif userinput=="shop":
        print("developing")
    # this is Help
    elif userinput=="help":
        print('\n\ntype attack to attack       type shop to Shop       type help for help       type stats to check your stats\n\n')
        print("\nDon't use caps when typing")
    # shows the stats of a player
    elif userinput=="stats":
        player.hp=str(player.hp)
        player.maxhp=str(player.maxhp)
        userattack=str(userattack)
        money=str(money)
        print(player.name+"'s stats")
        print("\n\n"+player.hp+"/"+player.maxhp+" Health")
        print(userattack+" Attack")
        print(money+ " Money\n\n")
        player.hp=int(player.hp)
        player.maxhp=int(player.maxhp)
        userattack=int(userattack)
        money=int(money)
    else:
        print("\n\nThat is not a Valid command type help if you need help\n\n")
