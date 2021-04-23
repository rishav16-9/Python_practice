from classes.game import bcolors, Person
from classes.magic import spell
from classes.inventory import Item
#Black magic

fire = spell("fire", 10, 100, "black")
Thunder = spell("Thunder", 10, 100, "black")
Rage = spell("Rage", 10, 100, "black")
Quake = spell("Quake", 10, 100, "black")
Blizzard = spell("Blizzard", 10, 100, "black")

#White Magic

cure = spell ("cure", 12, 120, "white")
cura = spell ("cura", 15, 200, "white")

# create some item

potion = Item("Potion", "potion", "Heals 50 hp", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 hp", 100)
superpotion = Item("Super-potion", "potion", "Heals 500 hp", 500)
elixer = Item("Elixer", "Elixer", "Fully restores HP/MP of the party member", 9999)
hielixier = Item("MegaElixier", "Elixer", "Fully restore partys hp/mp", 9999)

grenade = Item("grenade", "attacls", "Deals 500 Damage", 500)

#Instantiate People

player_spell = [fire, Thunder, Rage, Quake, Blizzard, cure, cura]
player_item = [potion, hipotion, superpotion, elixer, hielixier, grenade]
player = Person (1000, 65, 60, 34, player_spell, player_item) 
enemy = Person (1200, 65, 60, 34, [], [])

runnning = True
i = 0

# print('''bcolors.FAIL +''' bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while runnning:
    print ("====================")
    player.choose_action()
    choice = input("Choose Action")
    index = int(choice) - 1
    
    # print("Your choose", choice)
    # print("Your choose", index)
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked enemy for", dmg, "points of damage")
    
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1
        
        if magic_choice == -1:
            continue
          
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
           
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n Not enough mp\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(spell.cost)

        if spell.property == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.Name + "heal for", str(magic_dmg), "HP," + bcolors.ENDC) 
        elif spell.property == "black":
            player.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.Name + "deal for", str(magic_dmg),"points of damage," + bcolors.ENDC)
    
        # player.reduce_mp(spell.cost)
        # enemy.take_damage(magic_dmg)
        # print(bcolors.OKBLUE + "\n" +spell.Name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
    
    elif index == 2:
        player.choose_item()
        item_choice = int(input("choose item: ")) - 1
        
        if item_choice == -1:
            continue
            
        if item_choice == potion:
            player.heal(item.prop)
            
    enemy_choice = 1    
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks you for", enemy_dmg)
    
    print("=======================")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
         
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN+"You won, Enemy died" + bcolors.ENDC)
        runnning = False 
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lost, Enemy Won, Better Luck Next Time!!!!" + bcolors.ENDC)
        runnning = False
    
