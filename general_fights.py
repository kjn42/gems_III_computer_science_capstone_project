import random
import time
general_health = 3
def fight_only_general(general_health):
    while general_health != 0:
        if general_health == 3:
            print(" The general is in perfect condition.")
        elif general_health == 2:
            print(" The general a bit scratched up.")
        elif general_health == 1:
            print(" The general is in poor condition.")
        else:
            print("something's wrong")
        player_choice = input("Attack or try to dodge? ")
        while player_choice != "Attack" and player_choice != "Dodge":
            print(" Choose one of the listed options, please.")
            player_choice = input("Attack or try to dodge?")
        if player_choice == "Attack":
            if general_health == 1:
                print(" You lunge at the general one last time, stabbing him.\n You can feel that you hit a vital point.")
                print(' The general, shocked, falls to his knees. "How could I have missed my shots..."')
                time.sleep(2)
                print(" The general collapses.")
                print(" You win.")
                break
            else:
                print(" You lunge at the general and stab him right in the guts.")
            general_health -= 1
        else:
            print(" You drop your stance and prepare for the worst.")
        time.sleep(1)
        print(" The general raises his revolver, takes aim, and fires.")
        time.sleep(1)
        x = random.randint(1,8)
        if x == 1:
            print(" His shot misses.")
        else:
            print(" The well-aimed bullet hits one of your vital points, and pain shoots through your body.")
            print(' The general sighs and says "You know, I kind of hoped you would put up \n more of a fight." Your vision fades to black.\n Game over. You died')
            break

def fight_general_with_1_dog(general_health):
    if general_health == 3:
            print(" The general is in perfect condition.")
    elif general_health == 2:
        print(" The general a bit scratched up.")
    elif general_health == 1:
        print(" The general is in poor condition.")
    else:
        print("something's wrong")
    while general_health != 0:
        player_choice = input("Attack or try to dodge? ")
        while player_choice != "Attack" and player_choice != "Dodge":
            print(" Choose one of the listed options, please.")
            player_choice = input("Attack or try to dodge?")
        if player_choice == "Attack":
            print(" You lunge at the general and stab him right in the guts.")
            general_health -= 1
        else:
            print(" You drop your stance and prepare for the worst.")
        print(" One of the dogs leaps at you, knocking you over.")
        time.sleep(3)
        x = random.randint(1,4)
        print("")
        if x == 1:
            print(" The dog goes for your neck, killing you instantly.")
            print(" Game over. You died.")
            break
        else:
            print(" You wrestle with the dog and manage to throw it off of you.")
            print(" Taking the opening, you jump on the dog and kill it before it gets back up.")
            print(' All that remains is the general. He says, "As expected of a true hunter.')
            print(" I'd like to play with you more, but it seems your time is up." + '"\n He fires his gun.')
            time.sleep(5)
            x = random.randint(1,8)
            if x == 1:
                print(" His shot misses.")
                fight_only_general(general_health)
                break
            else:
                print(" The well-aimed bullet hits one of your vital points, and pain shoots through your body.")
                print(' The general sighs and says "You know, I kind of hoped you would put up \n more of a fight." Your vision fades to black.\n Game over. You died')
                break
        
def fight_general_with_2_dogs(general_health):
    if general_health == 3:
            print(" The general is in perfect condition.")
    elif general_health == 2:
        print(" The general a bit scratched up.")
    elif general_health == 1:
        print(" The general is in poor condition.")
    else:
        print("something's wrong")
    while general_health != 0:
        player_choice = input("Attack or try to dodge? ")
        while player_choice != "Attack" and player_choice != "Dodge":
            print(" Choose one of the listed options, please.")
            player_choice = input("Attack or try to dodge?")
        if player_choice == "Attack":
            print(" You lunge at the general and stab him right in the guts.")
            general_health -= 1
        else:
            print(" You drop your stance and prepare for the worst.")
        print(" One of the dogs leaps at you, knocking you over.")
        time.sleep(3)
        x = random.randint(1,4)
        print("")
        if x == 1:
            print(" The dog goes for your neck, killing you instantly.")
            print(" Game over. You died.")
            break
        else:
            print(" You wrestle with the dog and manage to throw it off of you.")
            print(" Taking the opening, you jump on the dog and kill it before it gets back up.")
            print(" The other dog rushes at you, full of rage.")
            time.sleep(5)
            x = random.randint(1,4)
            print("")
            if x == 1:
                print(" It jumps at you and starts tearing you apart.")
                print(" Game over. You died.")
                break
            else:
                print(" This time, you're ready for it, and quickly grab and dispatch it before it can attack you.")
                time.sleep(2)
                print(' All that remains is the general. He says, "As expected of a true hunter.')
                print(" I'd like to play with you more, but it seems your time is up." + '"\n He fires his gun.')
                time.sleep(5)
                x = random.randint(1,8)
                if x == 1:
                    print(" His shot misses.")
                    fight_only_general(general_health)
                    break
                else:
                    print(" The well-aimed bullet hits one of your vital points, and pain shoots through your body.")
                    print(' The general sighs and says "You know, I kind of hoped you would put up \n more of a fight." Your vision fades to black.\n Game over. You died')
                    break