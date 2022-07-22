import random
import numpy
import pandas as pd
import colorama
from colorama import init
from areas import area, areaDict
init(autoreset=True)
from colorama import Fore, Back, Style
from item import items,itemDict
from attack import attacks,attackDict
monlist=[]

def inputcheck(message:str):
    while True:
        try:
            message=int(input(message))
            break
        except ValueError:
            print("Try again with a num")
    return message

def monsterSelection(player):
    return player.area.monsters[random.randint(0,(len(player.area.monsters)-1))]



class characters: #class is used to make an object
    def __init__(self, rpgclass:str, name:str, health:int, currenthp:int, extrahp:int, mana:int, currentmp:int,extramana:int, defense:int,extradefense:int, intelligence:int,extraintelligence:int, strength:int,extrastrength:int, speed:int,extraspeed:int, xp:int, xpcontainer:int, level:int, coins:int, area:area, weapon:items, helmet:items, chestplate:items, leggings:items, boots:items, inv:list, attackmoves:list):
        self.rpgclass = rpgclass
        self.name = name
        self.health = health #self refers to the object
        self.currenthp =  currenthp
        self.extrahp=extrahp
        self.mana = mana
        self.currentmp = currentmp
        self.extramana=extramana
        self.defense = defense
        self.extradefense=extradefense
        self.intelligence = intelligence
        self.extraintelligence=extraintelligence
        self.strength = strength
        self.extrastrength=extrastrength
        self.speed = speed
        self.extraspeed=extraspeed
        self.xp = xp
        self.xpcontainer = xpcontainer
        self.level = level
        self.coins = coins
        self.area= area
        self.area.init(monlist,itemDict)
        self.weapon= weapon
        self.helmet=helmet
        self.chestplate=chestplate
        self.leggings=leggings
        self.boots=boots
        self.inv=inv
        self.attackmoves=attackmoves
        if self.rpgclass=="Monster":
            monlist.append(self)

    # Merges items together if they are the same type( so it takes less space in inv menu)
    def mergeItems(self):
        for item in self.inv:
            if item.amount<=0:
                self.inv.remove(item)
            for i in self.inv:
                if i.name==item.name:
                    if not self.inv.index(i) ==self.inv.index(item):
                        self.inv.remove(item)
                        itempos=self.inv.index(i)
                        self.inv[itempos].amount+=item.amount
    
    # Restores health and mana
    def restore(self):
        self.currentmp=self.mana
        self.currenthp=self.health

    #Makes sure that hp isn't over maxhp
    def check(self):
        if self.currenthp>self.health:
            self.currenthp=self.health
        if self.currentmp>self.mana:
            self.currentmp=self.mana

    # Adds the stats from equipped items 
    def applystats(self):
        # Resets base level stats
        self.health-=self.extrahp
        self.mana-=self.extramana
        self.defense-=self.extradefense
        self.intelligence-=self.extraintelligence
        self.strength-=self.extrastrength
        self.speed-=self.extraspeed
        # Resets external buffs
        self.extrahp=0
        self.extramana=0
        self.extradefense=0
        self.extraintelligence=0
        self.extrastrength=0
        self.extraspeed=0
        # Makes the weapon the character is holding a dictionary
        stats=vars(self.weapon)
        # Adds the buffs from that weapon
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the helmet the character is wearing a dictionary
        stats=vars(self.helmet)
        # Adds the buffs from that helmet
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the chestplate the character is wearing a dictionary
        stats=vars(self.chestplate)
        # Adds the buffs from that chestplate
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the leggings the character is wearing a dictionary
        stats=vars(self.leggings)
        # Adds the buffs from that legging
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Makes the boots the character is wearing a dictionary
        stats=vars(self.boots)
        # Adds the buffs from that boots
        self.extrahp+=stats["hp"]
        self.extramana+=stats["mana"]
        self.extradefense+=stats["defense"]
        self.extraintelligence+=stats["intelligence"]
        self.extrastrength+=stats["strength"]
        self.extraspeed+=stats["speed"]
        # Adds stored buffs to actual stats
        self.health+=self.extrahp
        self.mana+=self.extramana
        self.defense+=self.extradefense
        self.intelligence+=self.extraintelligence
        self.strength+=self.extrastrength
        self.speed+=self.extraspeed    

    # Mage charcter
    def mageSetup(name):
        # Just returns a character object
        return characters("Mage", name, 85, 85,0, 125, 125,0, 15,0, 25,0, 10,0, 20,0, 0, 25, 0, 25, areaDict[1], itemDict["wizard'sstaff"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], [], [attackDict["bonk"],attackDict["embers"], attackDict[""],attackDict[""]])

    # Rogue character
    def rogueSetup(name):
        # Just returns a character object
        return characters("Rogue", name, 100, 100, 0, 70, 70,0, 18,0, 20,0, 20,0, 25,0, 0, 25, 0, 25,areaDict[1], itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], [], [attackDict["cut"],attackDict[""],attackDict[""],attackDict[""]])
    
    # Warrior character
    def warriorSetup(name):
        # Just returns a character object
        return characters("Warrior", name, 110, 110,0, 50, 50,0, 22,0, 10,0, 280,0, 14,0, 0, 25, 0, 25, areaDict[1], itemDict["warrior'ssword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[], [attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
        
    # Testing character
    def testSetup(name):
        inv=[]
        testattacks=[]
        # Giving test character all items
        for key, value in itemDict.items():
            temp = value
            inv.append(temp)
            inv.append(temp)
        # Giving test character all attacks
        for key, value in attackDict.items():
            temp=value
            testattacks.append(temp)
        return characters("Human", name, 100, 100,0, 100, 100,0, 100,0, 100,0, 100,0, 100,0, 100, 100, 100, 100,areaDict[3], itemDict["null"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"], inv, testattacks)

    # Goes through character creation
    def createCharacter():
        # Gets name
        name = input("What is your name? ")
        # Continuously repeats if they don't type in a correct class
        while True:
            print("What class would you like to be? ")
            print("You can be a Mage, Rogue, or a Warrior")
            rpgclass=input("")
            rpgclass=rpgclass.replace(" ","").lower()
            # Determines what class they chose
            if rpgclass=="mage":
                return characters.mageSetup(name)
            elif rpgclass=="rogue":
                return characters.rogueSetup(name)
            elif rpgclass=="warrior":
                return characters.warriorSetup(name)
            else:
                print("That isn't a valid choice")
                print()
    
    # Shows the stats of the character
    def stats(self):
        print()
        print("----------------"+self.name+"'s Stats----------------")
        print("Class: "+self.rpgclass)
        print("Level "+str(self.level)+" <-> "+str(self.xp)+"/"+str(self.xpcontainer)+" XP until next level")
        print(Fore.LIGHTYELLOW_EX+"Coins: "+str(self.coins))
        print(Fore.LIGHTRED_EX+"❤  Health: "+str(self.currenthp)+"/"+str(self.health)+Style.RESET_ALL+"     Helmet: "+self.helmet.color+str(self.helmet.name))
        print(Fore.BLUE+"🕮  Mana: "+str(self.currentmp)+"/"+str(self.mana)+Style.RESET_ALL+"       Chestplate: "+self.chestplate.color+str(self.chestplate.name))
        print(Fore.LIGHTGREEN_EX+"❈ Defense: "+str(self.defense)+Style.RESET_ALL+"           Leggings: "+self.leggings.color+str(self.leggings.name))
        print(Fore.LIGHTBLUE_EX+"✎ Intelligence: "+str(self.intelligence)+Style.RESET_ALL+"        Boots: "+self.boots.color+str(self.boots.name))
        print(Fore.RED+"❁ Strength: "+str(self.strength)+Style.RESET_ALL+"         Weapon: "+self.weapon.color+str(self.weapon.name))
        print("✦ Speed: "+str(self.speed))
        print()
    
    # Shows the inventory of that character
    def showInv(self):
        # Declaring separate lists to organize into sections
        weaponslist=[]
        armorlist=[]
        otherslist=[]
        # Goes through every item in inventory
        for item in self.inv:
            item:items
            # Determines what type of item it is
            if item.typeofitem=="boots" or item.typeofitem=="leggings" or item.typeofitem=="helmet" or item.typeofitem=="chestplate":
                armorlist.append(item)
            elif item.typeofitem=="weapon":
                weaponslist.append(item)
            if item.typeofitem=="usable":
                otherslist.append(item)
        # Finds out which of the lists which have the most
        categories=[weaponslist, armorlist, otherslist]
        most= categories[numpy.argmax([len(l) for l in categories])]
        # Uses this information of longest list to add in a empty temp item, so it won't fall into an IndexError
        while len(armorlist)<len(most):
            armorlist.append(itemDict[""])
        while len(weaponslist)<len(most):
            weaponslist.append(itemDict[""])
        while len(otherslist)<len(most):
            otherslist.append(itemDict[""])

        print("Armor:                                 Weapons:                                 Others:")
        # Prints the amount of times the largest list has to cover all items.
        for item in range(len(most)):
            print("     "+armorlist[item].color+armorlist[item].name+Style.RESET_ALL+" "+str(armorlist[item].amount)+"x              "+weaponslist[item].color+weaponslist[item].name+Style.RESET_ALL+" "+str(weaponslist[item].amount)+"x              "+otherslist[item].color+otherslist[item].name+Style.RESET_ALL+" "+str(otherslist[item].amount)+"x")
        print("\n")
    
    # Equips items  
    def equip(self, itemname:str):
        # Looks through entire inventory
        for item in self.inv:
            item:items
            # if the names match then do below
            if item.name.lower().__contains__(itemname.replace(" ","").lower()):
                # Gets pos of the item and then alter the amount of that item in the inv
                pos=self.inv.index(item)
                self.inv[pos].amount-=1
                # Checks if it's a helmet
                if item.typeofitem=="helmet":
                    # Exchanges armor pieces
                    self.inv.append(self.helmet)
                    self.helmet=item
                # Checks if it's a chestplate
                elif item.typeofitem=="chestplate":
                    # Exchanges armor pieces
                    self.inv.append(self.chestplate)       
                    self.chestplate=item
                # Checks if it's leggings
                elif item.typeofitem=="leggings":
                    # Exchanges armor pieces
                    self.inv.append(self.leggings)
                    self.leggings=item
                # Checks if it's boots
                elif item.typeofitem=="boots":
                    # Exchanges armor pieces
                    self.inv.append(self.boots)        
                    self.boots=item
                # Checks if it's a weapon
                elif item.typeofitem=="weapon":
                    # Exchanges Weapons
                    self.inv.append(self.weapon)
                    self.weapon=item
                # If it can't be equipped it tells the player and then gives back the item tooken away at the start
                else:
                    print("Item cannot be equipped")
                    pos=self.inv.index(item)
                    self.inv[pos].amount+=1
        self.mergeItems()
        self.applystats()
                
    # Player buys item from shop
    def buy(self, buyitem:str):
        # Syntax because that is what the key for the data in dict is like
        buyitem=buyitem.replace(" ", "").lower()
        # if they type leave then nothing will happen
        if not buyitem[:1]=="l":
            try:
                buyitem:items=itemDict[buyitem]
                # checks if they have enought coins
                if buyitem.cost>self.coins:
                    print("You don't have enough coins to buy this item")
                elif not buyitem in self.area.items:
                    print("Not in this area")
                else:
                    self.coins-=buyitem.cost
                    self.inv.append(buyitem)
                    self.mergeItems()
            # If encounters KeyError then the player must of mispelled
            except KeyError:
                print("Did you misspell? because this item doesn't exist")
        elif buyitem[:4]=="info":
            items.itemInfo(buyitem.replace(" ","").lower()[4:])
            input()

    # Assigns a move to character and allows them to choose which slot to put it in
    def addMoves(self, move:attacks):
        # Made so I can type less code
        print("Congragulations!")
        print(Fore.LIGHTYELLOW_EX+"You have obtained the attack: "+move.color+move.name)
        input("Next ")
        print("\n"*100)
        self.attackMenu()
        while True:
            slot=inputcheck("Which slot would you like to put the move "+move.color+move.name.replace(" ", "")+Style.RESET_ALL+"? ")
            # Makes sure in valid slot
            if slot<=4 and slot>=1:
                break
            else:
                print("Put it in a valid move slot")
        self.attackmoves[int(slot-1)]=move

    # Checks the level of players if they are a certain level then it gives them new attacks
    def checkLevel(self):
        if self.level==8:
            # New attacks for mage
            if self.rpgclass.lower()=="mage":
                self.addMoves(attackDict["fireball"])
            # New attacks for warrior
            elif self.rpgclass.lower()=="warrior":
                self.addMoves(attackDict["shieldbash"])
            # new attacks for rogue
            elif self.rpgclass.lower()=="rogue":
                self.addMoves(attackDict["daggerthrow"])
    
    # Levels up character
    def levelup(self):
        # continuosly levels up until xp isn't over the cap
        while self.xp>=self.xpcontainer:
            self.xp=int(self.xp-self.xpcontainer)
            self.level+=1
            self.xpcontainer=int(self.xpcontainer*1.5)
            print(Fore.YELLOW+"You Leveled Up!"+Style.RESET_ALL+"      You are now level: "+Fore.YELLOW+str(self.level))
            # Random distribution of stats increases
            statsincrease=[]
            for i in range(6):
                statsincrease.append(random.randint(3,6))
            print(Fore.LIGHTRED_EX+"❤  Health: "+str(self.health)+" +"+str(statsincrease[0]))
            print(Fore.BLUE+"🕮  Mana: "+str(self.mana)+" +"+str(statsincrease[1]))
            print(Fore.LIGHTGREEN_EX+"❈ Defense: "+str(self.defense)+" +"+str(statsincrease[2]))
            print(Fore.LIGHTBLUE_EX+"✎ Intelligence: "+str(self.intelligence)+" +"+str(statsincrease[3]))
            print(Fore.RED+"❁ Strength: "+str(self.strength)+" +"+str(statsincrease[4]))
            print("✦ Speed: "+str(self.speed)+" +"+str(statsincrease[5]))
            self.health+=statsincrease[0]
            self.mana+=statsincrease[1]
            self.defense+=statsincrease[2]
            self.intelligence+=statsincrease[3]
            self.strength+=statsincrease[4]
            self.speed+=statsincrease[5]
            input()
            # Allows player to pick where to spend points
            points=10
            while points>0:
                self.restore()
                print("You have "+Style.BRIGHT+str(points)+Style.RESET_ALL+" extra points to spend")
                self.stats()
                stat=input("What stat do you want to add points to? ").replace(" ","").lower()
                pointspent=inputcheck("How much points do you want to spend? ")
                if pointspent>points:
                    print("I SAID you have "+Style.BRIGHT+str(points)+Style.RESET_ALL+" extra points to spend")
                    pointspent=0
                elif stat=="health":
                    self.health+=pointspent
                elif stat=="mana":
                    self.mana+=pointspent
                elif stat=="defense":
                    self.defense+=pointspent
                elif stat=="intelligence":
                    self.intelligence+=pointspent
                elif stat=="strength":
                    self.strength+=pointspent
                elif stat=="speed":
                    self.speed+=pointspent
                else:
                    print("That's not a valid stat")
                    pointspent=0
                points-=pointspent
            self.checkLevel()
            self.restore
            print("\n"*150)
            print("This is what you look like now")
            self.stats

    # Displays and attack menu
    def attackMenu(self):
        moves=[]
        for i in self.attackmoves:
            moves.append(i)
        print("Move 1: "+moves[0].color+moves[0].name+Style.RESET_ALL+"Move 3: "+moves[2].color+moves[2].name)
        print("Move 2: "+moves[1].color+moves[1].name+Style.RESET_ALL+"Move 4: "+moves[3].color+moves[3].name)

    # Returns true if health<=0
    def isDead(self):
        if self.currenthp<1:
            return True
        else:
            return False
    
    # allows user to regen mana and health by drinking potions
    def use(self, reqeditem:str):
        for item in self.inv:
            item:items
            if reqeditem.replace(" ","").lower()==item.name.replace(" ","").lower():
                if item.typeofitem=="usable":
                    pos=self.inv.index(item)
                    self.inv[pos].amount-=1
                    item=vars(item)
                    self.currenthp+=item["hp"]
                    self.currentmp+=item["mana"]
                    self.defense+=item["defense"]
                    self.strength+=item["strength"]
                    self.intelligence+=item["intelligence"]
                    self.speed+=item["speed"]
                    usestr="You gained "
                    if item["hp"]>0:
                        usestr+=Fore.RED+str(item["hp"])+" health"+Style.RESET_ALL+" and "
                    if item["mana"]>0:
                        usestr+=Fore.BLUE+str(item["mana"])+" mana"+Style.RESET_ALL+" and "
                    if item["defense"]>0:
                        usestr+=Fore.LIGHTGREEN_EX+str(item["defense"])+" permanent defense"+Style.RESET_ALL+" and "
                    if item["intelligence"]>0:
                        usestr+=Fore.LIGHTBLUE_EX+str(item["intelligence"])+" permanent intelligence"+Style.RESET_ALL+" and "
                    if item["strength"]>0:
                        usestr+=Fore.RED+str(item["strength"])+" permanent strength"+Style.RESET_ALL+" and "
                    if item["speed"]>0:
                        usestr+=str(item["speed"])+" permanent speed"+Style.RESET_ALL+" and "
                    print(usestr.rstrip("and "))
                    self.mergeItems()
                    self.check()
                    return True
                else:
                    print("Cannot use this item")
                    break
        return False

    # How the monster selects a move
    def monMoveSelect(self):
        while True:
            monmove=random.randint(0,3)
            if not self.attackmoves[monmove].type=="nonexistent":
                monmove:attacks=self.attackmoves[monmove]
                if not monmove.manacost>self.currentmp:
                    return monmove
                else:
                    while True:
                        item=random.randint(0,len(self.inv)-1)
                        item:items=self.inv[item]
                        if item.typeofitem=="usable":
                            itemstats=vars(item)
                            self.currenthp+=itemstats["hp"]
                            self.currentmp+=itemstats["mana"]
                            self.defense+=itemstats["defense"]
                            self.strength+=itemstats["strength"]
                            self.intelligence+=itemstats["intelligence"]
                            self.speed+=itemstats["speed"]
                            self.check()
                            return item

    # calculates the damage of an attack
    def attackCalc(self, move:attacks, receiver):
        # when monmoveSelect() does its thing it may return a items object instead of attacks
        if type(move) == attacks:
            mondescrip=0
            # This is to separate the player and monster description of attacks
            if self.rpgclass=="Monster":
                mondescrip=3
            # Determines if there is a crit
            crit=random.randint(1,1000)
            crit=crit<self.speed*8
            # Determines if there is a miss
            miss=random.randint(1,1000)
            miss=miss<receiver.speed*2
            # Description of attack
            attackmessage=move.descrip[0+mondescrip]
            # Calculates damage
            if move.type=="Physical":
                buff=int(self.strength/2.25)
                damage=int((1-(receiver.defense/(receiver.defense+180)))*int(move.damage+buff))
            elif move.type=="Magic":
                buff=(self.intelligence/5)/100
                damage=int((1-(receiver.defense/(receiver.defense+180)))*int(move.damage*(buff+1)))
                self.currentmp-=move.manacost
            else:
                print("ERROR")
            if crit:
                attackmessage=move.descrip[1+mondescrip]
                damage=int(damage*1.6)
            if miss:
                # 2 is the index of player miss description
                # for monster the index is 5, so if you add 3 then it gets the monster descriptioon
                return [0,move.descrip[2+mondescrip]]
            else:
                return [damage,attackmessage+str(damage)+" damage"]
        else:
            return [0, " used a "+move.color+move.name] 

    # Checks if anyone has died yet
    def battleCheck(self,m):
        if m.isDead() and self.isDead():
            print("You both are close to dying")
            print("You are forced to run away")
            return True
        elif m.isDead():
            print("The "+m.name+" is dead!")
            reward=random.randint(5,20)
            loot=random.randint(1,100)
            print("You Won! You found "+Fore.YELLOW+str(reward)+" coins")
            self.coins+=reward
            if loot<=100:
                loot=random.choice(["weapon","helmet","chestplate","leggings", "boots","inv"])
                loot=m.__dict__[loot]
                if isinstance(loot, list):
                    loot=random.randint(0,len(loot))
                    inv=m.__dict__["inv"]
                    loot=inv[loot]
                    self.inv.append(loot)
                    print("You also obtained: "+loot.color+loot.name)
                else:
                    self.inv.append(loot)
                    print("You also obtained: "+loot.color+loot.name)
            self.mergeItems()
            return True
        elif self.isDead():
            print("You almost died...")
            print("You were still able to escape")
            return True
        return False
    
    def battle(self):
        m:characters=monsterSelection(self)
        m.restore()
        monmove=m.monMoveSelect()
        print(Fore.LIGHTBLUE_EX+self.name+Style.RESET_ALL+" encounters a "+Fore.YELLOW+m.name)
        while self.currenthp>0 and m.currenthp>0:
            # Player selection of moves
            print()
            print("1: Attack                "+Fore.RED+"❤  "+str(m.currenthp)+"/"+str(m.health)+Style.RESET_ALL+" The "+m.name)
            print("2: Use an item")
            print("3: Status                "+Fore.RED+"❤  "+str(self.currenthp)+"/"+str(self.health)+Style.RESET_ALL+" "+self.name)
            print("4: Run")
            battleinput=inputcheck("What would you like to do? ")
            # Attack
            if battleinput==1:
                self.attackMenu()
                while True:
                    move=inputcheck("Which move would you like to use? ")
                    try:
                        move:attacks=self.attackmoves[move-1]
                        if not move.type=="nonexistent":
                            break
                        elif move.manacost>self.currentmp:
                            print("You don't have enough mana for this move")
                        else:
                            print("Try again with a valid move")
                    except IndexError:
                        print("Try again with a valid move")
                # Monster selecion of moves
                monmove=m.monMoveSelect()
                # Calculates damage for both sides
                monmove=m.attackCalc(monmove, self)
                move=self.attackCalc(move, m)
                print()
                # If player speed> monster speed: player attacks first
                if self.speed>m.speed:
                    m.currenthp-=move[0]
                    # Printing the attack move and then checking for death
                    print(move[1])
                    if self.battleCheck(m):
                        break
                    self.currenthp-=monmove[0]
                    # Printing the attack move and then checking for death
                    print("The "+m.name+monmove[1])
                    if self.battleCheck(m):
                        break
                    print()
                # If monster speed > player speed: monster attacks first
                elif m.speed>self.speed:
                    self.currenthp-=monmove[0]
                    print("The "+m.name+monmove[1])               
                    if self.battleCheck(m):
                        break
                    m.currenthp-=move[0]
                    print(move[1])
                    if self.battleCheck(m):
                        break
                # If monster speed==player speed(process of elimination): attack at the same time
                else:
                    self.currenthp-=monmove[0]
                    m.currenthp-=move[0]
                    print(move[1])
                    print("The "+m.name+monmove[1])
                    if self.battleCheck(m):
                        break
            # Use item
            elif battleinput==2:
                while True:
                    self.showInv()
                    reqeditem=input("What item do you want to use?(l to leave) ")
                    if reqeditem.replace(" ","").lower()[:2]=="le":
                        break
                    elif reqeditem[:4]=="info":
                        items.itemInfo(reqeditem.replace(" ","").replace("info", '').lower())
                        input()
                    elif self.use(reqeditem):
                        monmove=m.monMoveSelect()
                        monmove=m.attackCalc(monmove, self)
                        self.currenthp-=monmove[0]
                        print("The "+m.name+monmove[1])
                        break
                    else:
                        print("weird")
            # Show stats
            elif battleinput==3:
                self.stats()
            # Run away
            elif battleinput==4:
                escapechance=random.randint(1,1000)
                if self.speed*25<escapechance:
                    print("You sucessfully escaped")
                    print("\n"*150)
                    break
                else:
                    print("You weren't able to escape")
                    monmove=m.monMoveSelect()
                    monmove=m.attackCalc(monmove, self)
                    self.currenthp-=monmove[0]
                    print("The "+m.name+monmove[1])
                    self.battleCheck(m)
            else:
                print("Select a valid choice")

    def moveArea(self, areas):
        try:
            self.area=areaDict[areas].init(monlist,itemDict)
        except KeyError:
            print("That area doesn't exist")


# Monsters
characters("Monster", "Slime", 75, 75, 0, 50, 50,0, 20,0, 5,0, 12,0,18,0, 0,0,3,15,areaDict[1],itemDict["skeletonsword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[itemDict["smallhealthpotion"]],[attackDict["pounce"],attackDict[""],attackDict[""],attackDict[""]])
characters("Monster", "Goblin", 80, 80,0, 40, 40,0, 15, 0,5,0, 20,0,25,0, 0,0,3,20,areaDict[1],itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[itemDict["smallhealthpotion"]],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])
characters("Monster", "Orc", 120, 120,0, 30, 30,0, 25,0, 5,0, 38,0, 15,0, 0,0,3,20,areaDict[1],itemDict["rogue'sdagger"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[itemDict["smallhealthpotion"]],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])

characters("Monster", "Skeleton", 120, 120,0, 20, 20,0,25,0, 0,0, 20,0,25,0, 0,0,3,15,areaDict[2],itemDict["skeletonsword"], itemDict["starterhelmet"], itemDict["starterchestplate"], itemDict["starterleggings"], itemDict["starterboots"],[itemDict["calciumdrink"]],[attackDict["slash"],attackDict[""],attackDict[""],attackDict[""]])

characters("Monster", "Necromancer", 150, 150,0,100, 0, 0, 18, 0, 28, 0, 18, 0, 20, 0, 0,0,8, 10, areaDict[3], itemDict["necromancerwand"], itemDict["necromancerhood"], itemDict["necromancerrobe"],itemDict["necromancertrousers"],itemDict["necromancerboots"],[itemDict["smallhealthpotion"],itemDict["smallmanapotion"],itemDict["largerestorationpotion"]],[attackDict["fireball"],attackDict[""],attackDict[""],attackDict[""]] )


player=characters.testSetup("")
player.battle()

