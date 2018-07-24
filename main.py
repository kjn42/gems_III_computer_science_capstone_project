import time
import random
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

#based on the book The Most Dangerous Game
print (" You wake up on an island full of trees, your mind is in a daze.")
print (" You try to remember your own name... ")
name = input("What was it again? ") 
print (" Now I remember, it was" , name, ".")
time.sleep(1.5)
print (" You walk around the island and find a man with a rugged face and a few scars on his face.")
time.sleep(3)
print (" He introduces himself as General Health and he explains that he is the owner of this island.")
time.sleep(3)
print (' You ask him what he means when he says that "he owns this island."')
time.sleep(2.5)
print (" General Health starts to explain his back story...")
time.sleep(2)

print (' "You see I am an experienced hunter, as are you , and quite frankly I have started to find hunting boring." ')
time.sleep(4.5)
print (' "I have hunted around the world, large rhinos? No problem. Siberian Tigers? Easy. Animals, as you see only have their instinct and strength to win a fight, they do not have the wit to fight against man."')
time.sleep(6)
print (' "This is when I decided to find a new animal, one that is cunning, smart, strong, then it hit me as the perfect animal to hunt." ')
time.sleep(5.5)

print (' You have an idea of what he is going to say but you ask anyways, "What do you mean the perfect animal?" ')
time.sleep(4)
print (' "Well my dear', name , ', I am obviously talking about hunting humans." ' )
time.sleep(2.5)
print (' "You see I have done my research on you. You are a very skilled hunter and that is why I brought you to this island. We will both hunt each other!" ' )
time.sleep(5)
print (' The moment you hear this your eyes widen and you immedietly exclaim "You must be out of your mind to be doing this! Are you not afraid of death?! " ')
time.sleep(4)
print (' General Health laughs in your face "Well thats the thrill of the hunt my friend!" ')
time.sleep(3)
print (' You try to leave but the general says to your back "If you win you can keep this island or go home." Seeing no way else to leave the island except killing the general you have to accept his challenge. ')
time.sleep(6)
print (' You tell him that you accept his challenge.')
time.sleep(3)
print (' The general shows a wide smile "Great! Now let me explain the rules."')
time.sleep(3)
print (' "I will supply you with a knife, hunting clothes, and a small amount of food."')
time.sleep(4)
print (' "However, I myself have a Colt Python gun and two hunting dogs by my side. I will alot you a couple of hours as a headstart. Remeber you goal is to kill me." ')
time.sleep(5)
print (' The general throws the supplies at your feet, which includes a few knives, and you start picking them up.')
time.sleep(4.5)
print (' " and ......"')
time.sleep(1.3)
print (' "START! " ')
#Not mentioned to player but it takes 3 hits to kill general 

time.sleep(.5)
print(" You start running East.")
time.sleep(5)
print(" You stop to catch your breath. You can continue to run East, or go back West.")
player_choice = input("")
while player_choice != "East" and player_choice != "West":
    print(' Choose either "East" or "West", please.')
    print(" You can continue to run East, or go back West.")
    player_choice = input("")
if player_choice == "East":
    print(" You continue running East.")
    time.sleep(2)
    print(" You decide to look backwards, and off in the distance you see...")
    time.sleep(1)
    print(' "The general' + "'s gaining on me!" + '"')
    time.sleep(1)
    print(" You spot a large tree ahead of you. You can stay and fight the general, or hide in the tree.")
    player_choice = input("")
    while player_choice != "Fight" and player_choice != "Hide":
        print(' Choose either "Fight" or "Hide", please.')
        print(" You can stay and fight the general, or hide in the tree.")
        player_choice = input("")
    if player_choice == "Hide":
        print(" You quickly climb the tree to hide from the general.")
        time.sleep(2)
        print(" The general arrives at the tree and stands under it.")
        time.sleep(1)
        print(" He doesn't seem to notice you. You probably could jump him, or you could stay in hiding.")
        player_choice = input("")
        while player_choice != "Jump him" and player_choice != "Stay":
            print(' Choose either "Jump him" or "Stay", please.')
            print(" You probably could jump him, or you could stay in hiding.")
            player_choice = input("")
        if player_choice == "Stay":
            print(" The general moves away. You spend the night in the tree.")
            time.sleep(5)
            print(" The next day, the general is nowhere to be seen. You climb down the tree.")
            time.sleep(2)
            print(" You can either lay a trap for the general, or start running.")
            player_choice = input("")
            while player_choice != "Lay a trap" and player_choice != "Run":
                print(' Choose either "Lay a trap" or "Run", please.')
                print(" You can either lay a trap for the general or start running.")
            if player_choice == "Lay a trap":
                print(" You tie a knife to a sapling, pull it back, and tie the twig down.")
            print(" You start running North.")
            time.sleep(5)
            if player_choice == "Lay a trap":
                print(' You hear the trap spring.')
                print(' The general yells in pain, and then mutters, "You' + "'" + 're a crafty one, I' + "'" + 'give you that."')
                general_health -= 1
                time.sleep(2)
            print(" You arrive at a swamp. The area is muddy and has many broken tree branches scattered around.")
            time.sleep(1)
            print(" You can turn back and fight the general, or set another trap in the swamp.")
            player_choice = input("")
            while player_choice != "Fight" and player_choice != "Set a trap":
                print(' Choose either "Fight" or "Set a trap", please.')
                print(" You can turn back and fight the general, or set another trap in the swamp.")
                player_choice = input("")
            if player_choice == "Set a trap":
                print (' You look behind you and see that the general is not near.')
                time.sleep(2)
                print (' You start setting up your second trap by sharpening the thick branches with your knife and hide them in the mud.')
                time.sleep(3)
                print (' Once you finish you start to leave the area to set more traps.')
                time.sleep(2)
                print (' While walking you hear the howl of a dog, so you look back panicked but see none.')
                time.sleep(3)
                print (' You realize your trap worked.')
                time.sleep(2)
                print (" The injured dog's paw is cut from the traps and he can not pursue you anymore.")
                time.sleep(3)
                print (' Now there is only one hunting dog to worry about.')
                time.sleep(2)
                print(" You can either start running West, or stay and fight the general.")
                player_choice = input("")
                while player_choice != "Run West" and player_choice != "Fight":
                    print(' Chooes either "Run West" or "Fight", please.')
                    print(" You can either start running West, or stay and fight the general.")
                    player_choice = input("")
                if player_choice == "Run West":
                    print (' You return into the forest area.')
                    time.sleep(1.5)
                    print (' While considering your options, you notice that the forest has many vines.')
                    time.sleep(3)
                    print(" You can either choose to fight the general or set yet another trap.")
                    player_choice = input("")
                    while player_choice != "Fight" and player_choice != "Set a trap":
                        print(' Choose either "Fight" or "Set a trap", please.')
                        print(" You can either choose to fight the general or set yet another trap.")
                        player_choice = input("")
                    if player_choice == "Set a trap":
                        print (' An idea comes to your mind. You start getting the vines and start making a net.')
                        time.sleep(3)
                        print (' You cover the finished net in a bunch of leaves and branches, and hang the net high in a tree.')
                        time.sleep(3)
                        print (' You start leaving the area toward a cliff.')
                        time.sleep(2)
                        print (' While you are leaving you hear another howl of a dog, this time you do not look behind you, since you know your trap worked.')
                        time.sleep(4)
                        print(" You arrive at a cliff. The general hot on your heels. You can either jump off or fight the general.")
                        player_choice = input("")
                        while player_choice != "Jump" and player_choice != "Fight":
                            print(' Choose either "Jump" or "Fight", please.')
                            print(" You can either jump off the cliff or fight the general.")
                            player_choice = input("")
                        if player_choice == "Jump":
                            print (" You jump off the cliff and land in the water below.")
                            time.sleep(2)
                            print(" You start to swim toward the general's house.")
                            time.sleep(2)
                            print (' The general scoffs and says "I wanted to land the killing blow, too bad he jumped." ')
                            time.sleep(3)
                            print (' "At least I won the hunt."')
                            time.sleep(2)
                            print (' The general walks back home and puts his gun on his drawer. He then lays on his bed after the hunt to sleep.')
                            time.sleep(4)
                            print (' You finally made it to the back of the generals house. You climb up his house toward his window.')
                            time.sleep(3)
                            print (' You wait outside the generals window and decide you could use some rest.')
                            time.sleep(3)
                            print (' You rest on the large window ledge and wait until morning.')
                            time.sleep(5)
                            print (' It is morning and the general wakes up and goes toward the window to open the curtains.')
                            time.sleep(3)
                            print (' You hear the general moving around in his room you quickly hang off the window ledge. The general does not notice your fingers.')
                            time.sleep(4)
                            print (' The general leaves and goes downstairs to eat breakfast.')
                            time.sleep(2)
                            print (' You quickly break the window and grab his gun heading downstairs. The general looks up surprised that you are still alive.')
                            time.sleep(3)
                            print (' his eyes dart to the gun in your hand.')
                            time.sleep(1.5)
                            print (' "Well"')
                            time.sleep(1)
                            print ('.')
                            time.sleep(1)
                            print ('.')
                            time.sleep(1)
                            print ('.')
                            time.sleep(1)
                            print (' "Looks like that was my last hunt." General Health gives a wry smile "At least you gave me the thrill I was seeking".')
                            time.sleep(3)
                            print (' You load the gun and point it at him.')
                            time.sleep(1.5)
                            print (' "I guess we both win then."') 
                            time.sleep(1)
                            print (' You shoot the general in the head.')
                            time.sleep(2)
                            print (" You win.")
                    else:
                        print(" The general catches up to you.")
                        fight_general_with_1_dog(general_health)
                else:
                    print(" The general soon rushes to where you are, furious with the loss.")
                    fight_general_with_1_dog(general_health)
            else:
                print(" The general catches up to you, fuming with anger.")
                fight_general_with_2_dogs(general_health)
        else:
            print(" You drop from the tree, slashing the general on the way down.")
            general_health -= 1
            time.sleep(1)
            fight_general_with_2_dogs(general_health)
    else:
        print(" The general catches up to you.")
        time.sleep(1)
        print(' He says, "You shouldn' + "'" + 't have let me catch up to you.')
        fight_general_with_2_dogs(general_health)
else:
    print(" You run back towards where you started.")
    time.sleep(3)
    print(" You bump into the general.")
    time.sleep(.5)
    print(' He says, "It was foolish of you to run towards me."')
    fight_general_with_2_dogs(general_health)