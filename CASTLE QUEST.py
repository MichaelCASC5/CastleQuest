#C A S T L E  T E X T  A D V E N T U R E
# *
#   * F R O M :
#   * VERTEX OF HUNTER
#   *
# *

import random
import math

def intros():
    rand = random.randrange(0,10)
    str = ""
    
    if(rand < 1):
        str = "You walk into"
    elif(rand < 2):
        str = "You find yourself in"
    elif(rand < 3):
        str = "This new place is"
    elif(rand < 4):
        str = "You are now in"
    elif(rand < 5):
        str = "Your eyes pace around, you are in"
    elif(rand < 6):
        str = "As you scan your surroundings, you notice that you are within"
    else:
        str = "You are in"
    
    return str

def adjectives():
    rand = random.randrange(0,40)
    str = ""
    
    if(rand < 1):
        str = "a wide"
    elif(rand < 2):
        str = "a small"
    elif(rand < 3):
        str = "a cold"
    elif(rand < 4):
        str = "a stinky"
    elif(rand < 5):
        str = "a strangely hot, and steamy"
    elif(rand < 6):
        str = "a torch-lit"
    elif(rand < 7):
        str = "a frigidly cold"
    elif(rand < 8):
        str = "a dirt covered"
    elif(rand < 9):
        str = "a dirty"
    elif(rand < 10):
        str = "a stone"
    elif(rand < 11):
        str = "a giant"
    elif(rand < 12):
        str = "a dusty"
    elif(rand < 13):
        str = "a dust"
    elif(rand < 14):
        str = "a metal"
    elif(rand < 15):
        str = "a dark"
    elif(rand < 16):
        str = "a very dark"
    elif(rand < 17):
        str = "a nightmarishly dark"
    elif(rand < 18):
        str = "a brightly lit"
    elif(rand < 19):
        str = "an eerie"
    elif(rand < 20):
        str = "a flooded"
    elif(rand < 21):
        str = "a creepy"
    elif(rand < 22):
        str = "a worn"
    elif(rand < 23):
        str = "a rugged"
    else:
        str = "a"
    
    return str

def loc():
    rand = random.randrange(0,20)
    str = ""
    
    if(rand < 1):
        str = "chamber"
    elif(rand < 2):
        str = "cellar"
    elif(rand < 3):
        str = "sewer"
    elif(rand < 4):
        str = "cave"
    elif(rand < 5):
        str = "chamber, where the walls ascend many feet high, and are topped by a grand dome"
    elif(rand < 6):
        str = "rope bridge, it dangles haphazardly over a deep ravine"
    elif(rand < 7):
        str = "cage"
    elif(rand < 8):
        str = "dungeon"
    elif(rand < 9):
        str = "dungeon, it is overgrown with vines"
    elif(rand < 10):
        str = "library"
    elif(rand < 11):
        str = "cellar, the walls leak"
    elif(rand < 12):
        str = "sewer, the water flows gently"
    elif(rand < 13):
        str = "cave, your footsteps echo through the walls"
    elif(rand < 14):
        str = "library, the books litter the floor"
    else:
        str = "room"

    str = str + "."
    return str

def directions(score, inventory, health,name):
    rand = random.randrange(1,4)
    mons = random.randrange(1,4)
    work = random.randrange(1,4)

    while(work == mons):
        work = random.randrange(1,4)
    
    if(rand < 2):
        print("There is an exit ahead.", end=" ")
    else:
        print("There are", rand, "exits.", end=" ")
    
    if(work <= rand):
        print("You can see a workbench beyond exit " + str(work) + ".", end=" ")
    
    if(mons <= rand):
        print("You can hear a monster within exit " + str(mons) + ".", end=" ")

    space(2)
    
    str1 = input("Which direction would you like to go in? [1-3]")
    ans = 0
    if(str1 == ""):
        ans = 1
    else:
        if(str1 != "1" and str1 != "2" and str1 != "3"):
            str1 = "1"
        ans = int(str1)
    
    if(ans > rand):
        ans = rand
    elif(ans < 1):
        ans = 1
    
    print("You continue into exit " + str(ans) + "...")
    
    
    if(ans == mons):
        monster(score, inventory, health,name)
    elif(ans == work):
        inte = random.randrange(4)
        if(inte == 0):
            print("A monster blocks your path!\n")
            monster(score, inventory, health,name)
            if(health[0] > 0):
                workbench(score,inventory,health,name)
        else:
            workbench(score,inventory,health,name)

def remove(inventory, ans):
    for i in range(len(inventory)):
        o = "" + str(inventory[i])
        
        if(o.find(',') > 0 and o[0:o.find(',')] == ans) or (o.find(';') > 0 and o[0:o.find(';')] == ans):
            del inventory[i]
            break;

        if(o == ans):
            del inventory[i]
            break;
    
def workbench(score,inventory, health, name):
    ent()
    space(30)
    print("SCORE:",score,"\t\t\tHEALTH:",health,"\n")
    inv(inventory)
    print("Welcome to the workbench, " + str(name[0]) + "! Craft whatever you'd like, or eat.")
    print("Remember that cool downs must be at [0] to use that item!\n")
    print("Ex: 2 dagger\tor\t1 iron ingot 3 gunpowder\n")
    print("You can also name the food item you wish to eat.")

    ehealth = [0]
    
    ans = input()
    ans = ans.replace(" ", "")
    ans = ans.lower()

    #SWORDS
    if(ans == "1ironingot>1stick" and count(inventory,'iron ingot') >= 1 and count(inventory,'stick') >= 1):
        remove(inventory,'iron ingot')
        remove(inventory,'stick')
        inventory += ['dagger,0']

        print("You crafted a dagger!")
    elif(ans == "2dagger" and count(inventory,'dagger') >= 2):
        for i in range(2):
            remove(inventory,'dagger')
        inventory += ['short sword,0']
        
        print("You crafted a short sword!")
    elif(ans == "2shortsword" and count(inventory,'short sword') >= 2):
        for i in range(2):
            remove(inventory,'short sword')
        inventory += ['sword,0']
        
        print("You crafted a sword!")
    elif(ans == "2sword" and count(inventory,'sword') >= 2):
        for i in range(2):
            remove(inventory,'sword')
        inventory += ['long sword,0']
        
        print("You crafted a long sword!")
    elif(ans == "1longsword>1sword" and count(inventory,'long sword') >= 1 and count(inventory,'sword') >= 1):
        remove(inventory,'long sword')
        remove(inventory,'sword')
        inventory += ['excalibur,0']
        
        print("You crafted excalibur! The ground trembles as you wield the mightly blade!")

    #SHIELDS
        
    elif(ans == "7stick" and count(inventory,'stick') >= 7):
        for i in range(7):
            remove(inventory,'stick')
        inventory += ['wooden shield;50']
        
        print("You crafted a wooden shield!")
    elif(ans == "4ironingot>4stick" and count(inventory,'iron ingot') >= 4 and count(inventory,'stick') >= 4):
        for i in range(4):
            remove(inventory,'iron ingot')
        for i in range(4):
            remove(inventory,'stick')
        inventory += ['iron shield;150']
        
        print("You crafted an iron shield!")
    elif(ans == "2ironshield>10stick" and count(inventory,'iron shield') >= 2 and count(inventory,'stick') >= 10):
        for i in range(2):
            remove(inventory,'iron shield')
        for i in range(10):
            remove(inventory,'stick')
        inventory += ['metal hoplon;300']
        
        print("You crafted a metal hoplon! The shield shimmers in the dim light, and you can hear the monsters tremble...")

    #ARMOR
        
    elif(ans == "15stick" and count(inventory,'stick') >= 15):
        for i in range(15):
            remove(inventory,'stick')
        inventory += ['wooden armor;125']
        
        print("You crafted wooden armor!")
    elif(ans == "15ironingot" and count(inventory,'iron ingot') >= 15):
        for i in range(15):
            remove(inventory,'iron ingot')
        inventory += ['iron armor;300']
        
        print("You crafted iron armor!")

    #GUNS
    elif(ans == "1ironingot>3gunpowder" and count(inventory,'iron ingot') >= 1 and count(inventory,'gunpowder') >= 3):
        remove(inventory,'iron ingot')
        for i in range(3):
            remove(inventory,'gunpowder')
        inventory += ['bullet']
        
        print("You crafted a bullet!")
    elif(ans == "1ironingot>2stick" and count(inventory,'iron ingot') >= 1 and count(inventory,'stick') >= 2):
        for i in range(1):
            remove(inventory,'iron ingot')
        for i in range(2):
            remove(inventory,'stick')
        inventory += ['flint lock,0']
        
        print("You crafted a flint lock pistol!")
    elif(ans == "2flintlock" and count(inventory,'flint lock') >= 2):
        for i in range(2):
            remove(inventory,'flint lock')
        inventory += ['revolver,0']
        
        print("You crafted a revolver!")
    elif(ans == "2revolver" and count(inventory,'revolver') >= 2):
        for i in range(2):
            remove(inventory,'revolver')
        inventory += ['musket,0']
        
        print("You crafted a musket!")
        
    #FOOD
    
    elif(ans == "apple" and count(inventory,'apple') >= 1):
        num = input("How many apples do you want to eat?")
        if(num.isnumeric() == False):
            num = 0
        else:
            num = int(num)

        if(num > count(inventory,'apple')):
            num = count(inventory,'apple')
        
        for i in range(num):
            usage(inventory,score,ehealth,ans,health)
            
        print("You ate", num, "apples!")
    elif(ans == "bread" and count(inventory,'bread') >= 1):
        num = input("How much bread do you want to eat?")
        if(num.isnumeric() == False):
            num = 0
        else:
            num = int(num)

        if(num > count(inventory,'bread')):
            num = count(inventory,'bread')
        
        for i in range(num):
            usage(inventory,score,ehealth,ans,health)
            
        print("You ate", num, "bread!")
    elif(ans == "potato" and count(inventory,'potato') >= 1):
        num = input("How many potatos do you want to eat?")
        if(num.isnumeric() == False):
            num = 0
        else:
            num = int(num)

        if(num > count(inventory,'potato')):
            num = count(inventory,'potato')
        
        for i in range(num):
            usage(inventory,score,ehealth,ans,health)
            
        print("You ate", num, "potatos!")
    elif(ans == "steak" and count(inventory,'steak') >= 1):
        num = input("How much steak do you want to eat?")
        if(num.isnumeric() == False):
            num = 0
        else:
            num = int(num)

        if(num > count(inventory,'steak')):
            num = count(inventory,'steak')
        
        for i in range(num):
            usage(inventory,score,ehealth,ans,health)
            
        print("You ate", num, "steak!")
    elif(ans == "potionoflife" and count(inventory,'potion of life') >= 1):
        num = input("How many potions of life do you want to drink?")
        if(num.isnumeric() == False):
            num = 0
        else:
            num = int(num)

        if(num > count(inventory,'potion of life')):
            num = count(inventory,'potion of life')
        
        for i in range(num):
            usage(inventory,score,ehealth,ans,health)
            
        print("You drank", num, "potions of life!")
    else:
        print("You crafted nothing.")

def count(inventory, ans):
    output = 0
    
    for i in range(len(inventory)):
        o = "" + str(inventory[i])
        
        if(o.find(',') > 0 and o[0:o.find(',')] == ans and int(o[o.find(',')+1:]) == 0):
            output+=1
        if(o.find(',') > 0 and int(o[o.find(',')+1:]) > 0):
            num = int(o[o.find(',')+1:])
            num-=1
            inventory[i] = "" + str(o[0:o.find(',')]) + str(",") + str(num)

        if(o == ans):
            output+=1
        
    return output

def sub(inventory,ans,sub):
    done = 0
    for i in range(len(inventory)):
        for j in range(1000):
            if done == 0:
                if inventory[i] == str(ans) + ";" + str(j):
                    done = 1
                    num = (j - sub)
                    if num > 0:
                        inventory[i] = str(ans) + ";" + str(num)
                    else:
                        remove(inventory, ans)

def arm(inventory, ans):
    output = 0
    for i in range(len(inventory)):
        for j in range(1000):
            if inventory[i] == str(ans) + ";" + str(j):
                output += 1
    return output

def armor(inventory, health, num):
    if(arm(inventory, 'buckler') > 0):
        sub(inventory,'buckler',num)
    elif(arm(inventory, 'wooden shield') > 0):
        sub(inventory,'wooden shield',num)
    elif(arm(inventory, 'wooden armor') > 0):
        sub(inventory,'wooden armor',num)
    elif(arm(inventory, 'iron shield') > 0):
        sub(inventory,'iron shield',num)
    elif(arm(inventory, 'iron armor') > 0):
        sub(inventory,'iron armor',num)
    elif(arm(inventory, 'metal hoplon') > 0):
        sub(inventory,'metal hoplon',num)
    else:
        health[0]-=num
        
    
def rodent(score, inventory, health):
    ehealth = [int(score[0]/500) + 1]
    print("A vicious rodent appears! It jumps at your face.\n")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Rodent Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,3)
        if(att == 0):
            print("The rodent claws into your skin. -",int((score[0]/1000)*2 + 1),"HP")
            armor(inventory,health,int((score[0]/1000)*2 + 1))
        elif(att == 1):
            print("The rodent bites into your skull. -",int((score[0]/1000)*3 + 1),"HP")
            armor(inventory,health,int((score[0]/1000)*3 + 1))
        else:
            print("The rodent's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()
        
        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("The rodent has been defeated! It thuds to the floor.")
        score[0]+=50
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("You succumb to the ferocious rat.")

def zombie(score, inventory, health,name):
    ehealth = [int(score[0]/100) + 1]
    print("A zombie appears! \"" + str(name[0]) + "...\" it groans.\n")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Zombie Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The zombie slashes you with sharp claws. -",int((score[0]/1000)*2 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*2 + 2))
        elif(att == 1):
            print("The zombie bites into your arm. -",int((score[0]/1000)*3 + 4),"HP")
            armor(inventory,health,int((score[0]/1000)*3 + 4))
        elif(att == 2):
            print("The zombie strangles you. -",int((score[0]/1000)*4 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*4 + 6))
        else:
            print("The zombies's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("The zombie has been defeated! It collapses and fall apart.")
        score[0]+=75
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("The zombie eats your brains.")

def skeleton(score, inventory, health):
    ehealth = [int(score[0]/100) + 1]
    print("A skeleton appears! Its bones rattle as it draws nearer.\n")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Skeleton Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The skeleton shoves you to the floor. -",int((score[0]/1000)*2 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*2 + 2))
        elif(att == 1):
            print("The skeleton delivers a hard punch to your face. -",int((score[0]/1000)*4 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*4 + 6))
        elif(att == 2):
            print("The skeleton bites down on your shoulder. -",int((score[0]/1000)*6 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*6 + 8))
        else:
            print("The skeleton's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("The skeleton has been defeated! Its bones rattle across the floor as they roll away.")
        score[0]+=100
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("It rips you apart.")

def mummy(score, inventory, health):
    ehealth = [int(score[0]/90) + 1]
    print("A mummy appears! The evil glow of its undead eyes illuminates your surroundings.\n")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Mummy Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The mummy slams your head into the wall. -",int((score[0]/1000) + 2),"HP")
            armor(inventory,health,int((score[0]/1000) + 2))
        elif(att == 1):
            print("The mummy attempts to rip your arm off. -",int((score[0]/1000)*2.5 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*2.5 + 6))
        elif(att == 2):
            print("The mummy drives its sharp claws into your skin. -",int((score[0]/1000)*3.5 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*3.5 + 8))
        else:
            print("The mummy's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("The mummy has been defeated! It hits the floor, and the glow of its eyes dims away...")
        score[0]+=125
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("It shoves you into a coffin.")

def vampire(score, inventory, health,name):
    ehealth = [int(score[0]/85) + 1]
    print("A vampire appears! \"" + str(name[0]) + "!\" It shouts. \"I have been awaiting you...\"\n")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Vampire Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The vampire claws you. -",int((score[0]/1000)*1.5 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*1.5 + 2))
        elif(att == 1):
            print("The vampire bites into your neck. -",int((score[0]/1000)*2.75 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*2.75 + 6))
        elif(att == 2):
            print("The vampire summons a swarm of bats. They all claw you as they pass. -",int((score[0]/1000)*3.75 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*3.75 + 8))
        else:
            print("The vampire's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("\"Noooo!\" It screams in agonizing pain, and turns to dust...")
        score[0]+=150
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("It sucks all your blood away.")

def witch(score, inventory, health,name):
    ehealth = [int(score[0]/80) + 1]
    print("A witch appears! Its cackles echo throughout the castle.\n")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Witch Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The witch stabs a voodoo doll. -",int((score[0]/1000)*1.5 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*1.5 + 2))
        elif(att == 1):
            print("\"Ohh " + str(name[0]) +  "... I can't wait to oven you!\" A poisonous gas fills the room. -",int((score[0]/1000)*3 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*3 + 6))
        elif(att == 2):
            print("The witch heals herself. +",int(score[0]/300),"EHP")
            ehealth[0]+=int(score[0]/300)
        else:
            print("The witch's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("The witch has been defeated! She bursts into a brilliant flame.")
        score[0]+=175
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("She cackles at your death.")

def werewolf(score, inventory, health):
    ehealth = [int(score[0]/75) + 1]
    print("A werewolf appears! It drools saliva as it snarls.")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Werewolf Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The werewolf claws you. -",int((score[0]/1000)*1.75 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*1.75 + 2))
        elif(att == 1):
            print("The werewolf kicks you with its powerful hind legs. -",int((score[0]/1000)*3.5 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*3.5 + 6))
        elif(att == 2):
            print("The werewolf bites into your leg. -",int((score[0]/1000)*3.75 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*3.75 + 8))
        else:
            print("The werewolf's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("It howls and the walls tremble. It collapses.")
        score[0]+=200
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("It consumes you.")

def phantom(score, inventory, health, name):
    ehealth = [int(score[0]/75) + 1]
    print("You hear a terrifying shriek. \"" + str(name[0]) + ", I have come for you!\"")
    print("A phantom appeared!")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Phantom Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The phantom caves in the walls. -",int((score[0]/1000)*1.75 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*1.75 + 2))
        elif(att == 1):
            print("The phantom posseses your left arm, and you stab yourself. -",int((score[0]/1000)*3.5 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*3.5 + 6))
        elif(att == 2):
            print("The phantom lets out an ear-piercing shriek, you collapse. -",int((score[0]/1000)*4 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*4 + 8))
        else:
            print("The phantom retreats momentarily.")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("It turns into ectoplasm. The goo sticks to your boots.")
        score[0]+=225
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("It posseses you completely.")

def knight(score, inventory, health):
    ehealth = [int(score[0]/25) + 1]
    print("What seems like a knight approaches you... he has already succumbed to the castle...")
    print("A Zombie Knight appeared!")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Zombie Knight Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The zombie knight slashes you with a sword. -",2,"HP")
            armor(inventory,health,2)
        elif(att == 1):
            print("The zombie knight bashes you with its shield. -",4,"HP")
            armor(inventory,health,4)
        elif(att == 2):
            print("The zombie knight strangles you with a rope. -",6,"HP")
            armor(inventory,health,6)
        else:
            print("The zombie knight's attack missed!")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("The zombie knight has been defeated! Its armor hits the ground with a sharp sound.")
        score[0]+=250
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("The zombie knight eats your brains.")

def troll(score, inventory, health, name):
    ehealth = [int(score[0]/65) + 1]
    print("You hear the thuds of giant steps. \"Fee fi fo fum, I smell the blood of " + str(name[0]) + ".\"")
    print("A Giant Troll appeared!")
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Giant Troll Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The giant troll swings a massive fist into the wall. Almost everything collapses -",int((score[0]/1000)*2 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*2 + 2))
        elif(att == 1):
            print("The giant troll attempts to stomp you into the ground. -",int((score[0]/1000)*4 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*4 + 6))
        elif(att == 2):
            print("The giant troll picks you up and begins to crush you in its mouth. -",int((score[0]/1000)*4.5 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*4.5 + 8))
        else:
            print("The giant troll loses its balance for a moment.")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("It slowly tips over and crashes to the floor. The entire castle nearly comes down.")
        score[0]+=275
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("It turns your bones to bread.")

def dragon(score, inventory, health, name):
    ehealth = [int(score[0]/50) + 1]
    print("The flapping of giant wings can be heard. There is a horrible roar.")
    print("The dragon stares you down, and smoking flames leave its nostrils.\n")
    
    print("\"Foolish " + str(name[0]) + ", I have slaughtered many like you.\"\n")
    
    input("Press enter to begin battle:")
    print()

    while(ehealth[0] > 0 and health[0] > 0):
        space(30)
        print("SCORE:",score,"\t\t\tHEALTH:",health)
        print("Dragon Health:",ehealth,"\n\n\n")
        
        inv(inventory)
        
        att = random.randrange(0,4)
        if(att == 0):
            print("The dragon screeches and crushes you beneath its massive claws -",int((score[0]/1000)*3 + 2),"HP")
            armor(inventory,health,int((score[0]/1000)*3 + 2))
        elif(att == 1):
            print("The dragon crushes you in its mouth. -",int((score[0]/1000)*4.5 + 6),"HP")
            armor(inventory,health,int((score[0]/1000)*4.5 + 6))
        elif(att == 2):
            print("The dragon opens its jaws and incinerates you with flames. -",int((score[0]/1000)*5 + 8),"HP")
            armor(inventory,health,int((score[0]/1000)*5 + 8))
        else:
            print("You fool the dragon, it is confused for a moment.")
        
        space(1)
        
        print("Use an item!")
        ans = input()
        ans.replace(" ", "")
        ans = ans.lower()

        if(count(inventory,ans) > 0):
            usage(inventory,score,ehealth,ans,health)
        else:
            print("You don't have that!")
            ent()

    if(health[0] > 0):
        print("A horrible screech is let out. You can hear distant walls of the castle collapse.")
        print("\"" + str(name[0]) + "! Heed my words... I shall return...\"")
        score[0]+=300
        keyLoot(inventory)
        loot(score,inventory)
    else:
        print("\"A pathetic display, " + str(name[0]) + ".\" The dragon returns to the depths of the castle.")

def assign(ans, num):
    done = False
    
    for i in range(len(inventory)):
        o = "" + str(inventory[i])
        
        if(o.find(',') > 0 and o[0:o.find(',')] == ans and int(o[o.find(',')+1:]) == 0 and done == False):
            inventory[i] = "" + str(o[0:o.find(',')]) + str(",") + str(num)
            done = True
    
def usage(inventory,score,ehealth,ans,health):
    if(ans == "dagger"):
        ehealth[0]-=1
        score[0]+=10
        assign(ans,0)
    elif(ans == "short sword"):
        ehealth[0]-=4
        score[0]+=20
        assign(ans,2)
    elif(ans == "sword"):
        ehealth[0]-=12
        score[0]+=40
        assign(ans,5)
    elif(ans == "long sword"):
        ehealth[0]-=48
        score[0]+=70
        assign(ans,7)
    elif(ans == "excalibur"):
        ehealth[0]-=200
        score[0]+=250
        assign(ans,6)
    elif(ans == "flint lock"):
        if(count(inventory,'bullet') > 0):
            remove(inventory,'bullet')
            ehealth[0]-=30
            score[0]+=100
            assign(ans,3)
        else:
            print("You don't have any ammo!")
            ent()
    elif(ans == "revolver"):
        if(count(inventory,'bullet') > 0):
            remove(inventory,'bullet')
            ehealth[0]-=90
            score[0]+=120
            assign(ans,5)
        else:
            print("You don't have any ammo!")
    elif(ans == "musket"):
        if(count(inventory,'bullet') > 0):
            remove(inventory,'bullet')
            ehealth[0]-=180
            score[0]+=140
            assign(ans,3)
        else:
            print("You don't have any ammo!")
    elif(ans == "apple"):
        inventory.remove('apple')
        health[0]+=5
        score[0]+=5
        healthcap(health)
    elif(ans == "bread"):
        inventory.remove('bread')
        health[0]+=15
        score[0]+=15
        healthcap(health)
    elif(ans == "potato"):
        inventory.remove('potato')
        health[0]+=25
        score[0]+=25
        healthcap(health)
    elif(ans == "steak"):
        inventory.remove('steak')
        health[0]+=45
        score[0]+=45
        healthcap(health)
    elif(ans == "potion of life" or ans == "potionoflife"):
        inventory.remove('potion of life')
        health[0]+=100
        score[0]+=120
        healthcap(health)
    else:
        print("You can't use that!")
        ent()

def healthcap(health):
    if(health[0] > 100):
        health[0] = 100
    
def monster(score, inventory, health, name):
    ent()
    space(30)
    
    rand = random.randrange(round(score[0]/250,0)+1)
    
    if(rand < 1):
        rodent(score, inventory, health)
    elif(rand < 2):
        zombie(score, inventory, health,name)
    elif(rand < 3):
        skeleton(score, inventory, health)
    elif(rand < 4):
        mummy(score, inventory, health)
    elif(rand < 5):
        vampire(score, inventory, health,name)
    elif(rand < 6):
        witch(score, inventory, health,name)
    elif(rand < 7):
        werewolf(score,inventory,health)
    elif(rand < 8):
        phantom(score,inventory,health,name)
    elif(rand < 9):
        knight(score,inventory,health)
    elif(rand < 10):
        troll(score,inventory,health,name)
    else:
        dragon(score,inventory,health,name)

def foodLoot(score, inventory):
    balance = balance = random.randrange(round(score[0]/500,0)+1)

    if(balance < 1):
        inventory += ['apple']
        print("an apple!")
    elif(balance < 2):
        inventory += ['bread']
        print("bread!")
    elif(balance < 3):
        inventory += ['potato']
        print("a potato!")
    elif(balance < 4):
        inventory += ['steak']
        print("steak!")
    else:
        inventory += ['potion of life']
        print("a potion of life!")

def keyLoot(inventory):                         #keys
        amnt = random.randrange(3)
        if(amnt > 0):
            print("You found ", end="")
        
        for i in range(amnt):
            inventory += ['key']
        if(amnt == 1):
            print("a key!")
        elif(amnt > 1):
            print(amnt, "keys!")

def loot(score,inventory):
    if(random.randrange(100) < 40):
        print("You found ", end="")
        foodLoot(score, inventory)

    
    for i in range(int(score[0]/2000)+1):
        rand = random.randrange(0,100)
        
        print("You found ", end="")
        if(rand < 25):                            #swords
            inventory += ['dagger,0']
            print("a dagger!")
        elif(rand < 65):                            #food
            print("nothing.")
        elif(rand < 75):                            #iron
            for i in range(int(score[0]/2000) + 2):
                inventory += ['iron ingot']
            print(int(score[0]/2000) + 2, "iron ingots!")
        elif(rand < 85):
            for i in range(int(score[0]/1000) + 2):
                inventory += ['stick']
            print(int(score[0]/1000) + 2, "sticks!")
        elif(rand < 95):
            for i in range(int(score[0]/2000) + 2):
                inventory += ['gunpowder']
            print(int(score[0]/2000) + 2, "gunpowder!")
        else:
            inventory += ['buckler;5']
            print("a buckler!")
    

def chest(score,inventory):
    num = random.randrange(4)
    if(num == 0):
        print("There are no chests here.")
    elif(num == 1):
        print("There is 1 chest here", end="")
        if(inventory.count('key') > 0):
            print(".")
        else:
            print(", but you don't have any keys left!")
    else:
        print("There are",num,"chests here", end="")
        if(inventory.count('key') > 0):
            print(".")
        else:
            print(", but you don't have any keys left!")

    if(num > 0 and inventory.count('key') > 0):
        str1 = input("How many chests do you want to open?")
        ans = 0
        if(str1.isnumeric() == False):
            ans = 0
        else:
            ans = int(str1)
        
        print()
        if(ans > num):
            ans = num
        
        while(ans > 0 and inventory.count('key') > 0):
            
            loot(score,inventory)
            score[0]+=20
            
            ans-=1
            inventory.remove('key')

    print()
    return ""

def inv(inventory):
    items = []
    armor = []
    weapons = []

    for i in inventory:
        if(i.find(',') > 0):
            num = 0
            end = ""
            if(int(i[i.find(',')+1:]) == 0):
                end = " READY"
                
            weapons+=[i.replace(',',' [') + str(']') + end]
        elif(i.find(';') > 0):
            armor+=[i.replace(';',' [') + str(']')]
        else:
            items+=[i]

    warn = ""
    if(len(items)>30):
        del items[30:]
        warn = "\t\tYour inventory has 30 items!\nClear up space so that you can continue to get loot."
    
    long = len(items)
    if len(armor) > len(items):
        long = len(armor)
    if len(weapons) > long:
        long = len(weapons)
    while len(items) < long:
        items += [" "]
    while len(armor) < long:
        armor += [" "]
    while len(weapons) < long:
        weapons += [" "]
    
    long1 = 0
    for i in range(len(items)):
        if len(items[i]) > long1:
            long1 = len(items[i])
    if long1 < 6:
        long1 = 6
    long2 = 0
    for i in range(len(armor)):
        if len(armor[i]) > long2:
            long2 = len(armor[i])
    if long2 < 7:
        long2 = 7
    long3 = 0
    for i in range(len(weapons)):
        if len(weapons[i]) > long3:
            long3 = len(weapons[i])
    
    print("INVENTORY:",warn,"\n")
    print("Items:" + " " * (long1 - 1) + "Shield:" + " " * (long2 - 2) + "Weapons: ")
    for i in range(long):
        print(items[i],end=" " * (long1 - len(items[i]) + 5))
        print(armor[i],end=" " * (long2 - len(armor[i]) + 5))
        print(weapons[i])
    print()
    
def ent():
    input("Press enter to continue:")
    print()

def space(n):
    for i in range(n):
        print()

#*****=====*****
#vars
score = [100]
health = [100]
name = [""]
inventory = ['key','key','dagger,0','buckler;5']

space(30)
print("Welcome to CASTLE QUEST!\n\n\n")
print("What is your name, hero?")
name[0] = input("NAME: ")
print("\n\n\nWelcome, " + str(name[0]) + "! I wish you best of luck, but I don't think you'll survive very long...")
ent()
space(30)

#The beginning
print("You are at the entrance of a grand castle. The sun is setting. Firmly, you step forward. Good luck.")
space(5)
inv(inventory)
chest(score,inventory)
print()
print("You advance forward... into the unknown...")
ent()
space(30)

while(health[0] > 0):
    print("SCORE:",score,"\t\t\tHEALTH:",health,"\n")

    #room
    print(intros(), adjectives(), loc(), end=" ")
    space(2)
    inv(inventory)
    print(chest(score, inventory))

    #direction
    directions(score, inventory, health,name)
    
    ent()
    space(30)

print("G A M E  O V E R")
print("Here are your final stats:")
ent()
space(8)
print("SCORE:",score)
space(1)
inv(inventory)
space(3)
print("The castle defeats you for now, but the monsters within tremble when they hear... \"" + str(name[0]) + "...\"")
input("Press enter to leave.")
