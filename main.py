import time
import random
from colorama import Fore
general_health = 3

def fight_only_general(general_health):
    while general_health != 0:
        if general_health == 3:
            print(Fore.BLACK+" The general is in perfect condition.")
        elif general_health == 2:
            print(Fore.BLACK+" The general a bit scratched up.")
        elif general_health == 1:
            print(Fore.BLACK+" The general is in poor condition.")
        else:
            print(Fore.BLACK+"something's wrong")
        print(Fore.MAGENTA+"Attack",Fore.BLACK+"or try to",Fore.MAGENTA+"dodge?")
        player_choice = input('')
        while player_choice != "Attack" and player_choice != "Dodge":
            print(Fore.BLACK+" Choose one of the listed options, please.")
            print(Fore.MAGENTA+"Attack",Fore.BLACK+"or try to",Fore.MAGENTA+"dodge?")
            player_choice = input('')
        if player_choice == "Attack":
            if general_health == 1:
                print(Fore.BLACK+" You lunge at the general one last time, stabbing him.\n You can feel that you hit a vital point.")
                print(Fore.BLACK+' The general, shocked, falls to his knees. "How could I have missed my shots..."')
                time.sleep(2)
                print(Fore.BLACK+" The general collapses.")
                print(Fore.BLACK+ " You win.")
                break
            else:
                print(Fore.BLACK+" You lunge at the general and stab him right in the guts.")
            general_health -= 1
        else:
            print(Fore.BLACK+" You drop your stance and prepare for the worst.")
        time.sleep(1)
        print(Fore.BLACK+" The general raises his revolver, takes aim, and fires.")
        time.sleep(1)
        x = random.randint(1,8)
        if x == 1:
            print(Fore.BLACK+" His shot misses.")
        else:
            print(Fore.BLACK+" The well-aimed bullet hits one of your vital points, and pain shoots through your body.")
            print(Fore.BLACK+' The general sighs and says ',Fore.RED+'"You know, I kind of hoped you would put up \n more of a fight."',Fore.BLACK+' Your vision fades to black.\n Game over. You died')
            break

def fight_general_with_1_dog(general_health):
    if general_health == 3:
            print(Fore.BLACK+" The general is in perfect condition.")
    elif general_health == 2:
        print(Fore.BLACK+" The general a bit scratched up.")
    elif general_health == 1:
        print(Fore.BLACK+" The general is in poor condition.")
    else:
        print(Fore.BLACK+"something's wrong")
    while general_health != 0:
        print(Fore.MAGENTA+"Attack",Fore.BLACK+"or try to",Fore.MAGENTA+"dodge?")
        player_choice = input('')
        while player_choice != "Attack" and player_choice != "Dodge":
            print(Fore.BLACK+" Choose one of the listed options, please.")
            print(Fore.MAGENTA+"Attack",Fore.BLACK+"or try to",Fore.MAGENTA+"dodge?")
            player_choice = input('')
        if player_choice == "Attack":
            print(Fore.BLACK+" You lunge at the general and stab him right in the guts.")
            general_health -= 1
        else:
            print(Fore.BLACK+" You drop your stance and prepare for the worst.")
        print(Fore.BLACK+" One of the dogs leaps at you, knocking you over.")
        time.sleep(3)
        x = random.randint(1,4)
        print("")
        if x == 1:
            print(Fore.BLACK+" The dog goes for your neck, killing you instantly.")
            print(Fore.BLACK+" Game over. You died.")
            break
        else:
            print(Fore.BLACK+" You wrestle with the dog and manage to throw it off of you.")
            print(Fore.BLACK+" Taking the opening, you jump on the dog and kill it before it gets back up.")
            print(Fore.BLACK+' All that remains is the general. He says, "As expected of a true hunter.')
            print(Fore.BLACK+" I'd like to play with you more, but it seems your time is up." + '"\n He fires his gun.')
            time.sleep(5)
            x = random.randint(1,8)
            if x == 1:
                print(Fore.BLACK+" His shot misses.")
                fight_only_general(general_health)
                break
            else:
                print(Fore.BLACK+" The well-aimed bullet hits one of your vital points, and pain shoots through your body.")
                print(Fore.BLACK+' The general sighs and says "You know, I kind of hoped you would put up \n more of a fight." Your vision fades to black.\n Game over. You died')
                break
        
def fight_general_with_2_dogs(general_health):
    if general_health == 3:
            print(Fore.BLACK+" The general is in perfect condition.")
    elif general_health == 2:
        print(Fore.BLACK+" The general a bit scratched up.")
    elif general_health == 1:
        print(Fore.BLACK+" The general is in poor condition.")
    else:
        print(Fore.BLACK+"something's wrong")
    while general_health != 0:
        print(Fore.MAGENTA+"Attack",Fore.BLACK+"or try to",Fore.MAGENTA+"dodge?",Fore.MAGENTA)
        player_choice = input("")
        while player_choice != "Attack" and player_choice != "Dodge":
            print(Fore.BLACK+" Choose one of the listed options, please.")
            print(Fore.MAGENTA+"Attack",Fore.BLACK+"or try to",Fore.MAGENTA+"dodge? ")
            player_choice = input('')
        if player_choice == "Attack":
            print(Fore.BLACK+" You lunge at the general and stab him right in the guts.")
            general_health -= 1
        else:
            print(Fore.BLACK+" You drop your stance and prepare for the worst.")
        print(Fore.BLACK+" One of the dogs leaps at you, knocking you over.")
        time.sleep(3)
        x = random.randint(1,4)
        print("")
        if x == 1:
            print(Fore.BLACK+" The dog goes for your neck, killing you instantly.")
            print(Fore.BLACK+" Game over. You died.")
            break
        else:
            print(Fore.BLACK+" You wrestle with the dog and manage to throw it off of you.")
            print(Fore.BLACK+" Taking the opening, you jump on the dog and kill it before it gets back up.")
            print(Fore.BLACK+" The other dog rushes at you, full of rage.")
            time.sleep(5)
            x = random.randint(1,4)
            print("")
            if x == 1:
                print(Fore.BLACK+" It jumps at you and starts tearing you apart.")
                print(Fore.BLACK+" Game over. You died.")
                break
            else:
                print(Fore.BLACK+" This time, you're ready for it, and quickly grab and dispatch it before it can attack you.")
                time.sleep(2)
                print(Fore.BLACK+' All that remains is the general. He says, "As expected of a true hunter.')
                print(Fore.BLACK+" I'd like to play with you more, but it seems your time is up." + '"\n He fires his gun.')
                time.sleep(5)
                x = random.randint(1,8)
                if x == 1:
                    print(Fore.BLACK+" His shot misses.")
                    fight_only_general(general_health)
                    break
                else:
                    print(Fore.BLACK+" The well-aimed bullet hits one of your vital points, and pain shoots through your body.")
                    print(Fore.BLACK+' The general sighs and says "You know, I kind of hoped you would put up \n more of a fight." Your vision fades to black.\n Game over. You died')
                    break

###based on the book The Most Dangerous Game
#print (" You wake up on an island full of trees, your mind is in a daze.")
#print (" You try to remember your own name... ")
#name = input("What was it again? ") 
#print (" Now I remember, it was" , name, ".")
#time.sleep(1.5)
#print (" You walk around the island to try to map out the place.")
#time.sleep(3)
#print ("You keep walking and on the other side of the island you find a massive building. Out of curiousity you walk towards it.")
#time.sleep(4)
#print ("While walking towards the building a man with a rugged face and a few scars on his face taps on your shoulder.")
#time.sleep(3.5)
#print ("Instinctively you jump back away from the man.")
#time.sleep(3)
#print (" He flashes a kind smile showing how he doesn't plan to attack. He introduces himself as General Health and he explains that he is the owner of this island.")
#time.sleep(5)
#print (' You ask him what he means when he says that "he owns this island."')
#time.sleep(2.5)
#print (" General Health starts to explain his back story...")
#time.sleep(2)
#
#print (Fore.RED + '"You see I am an experienced hunter, as are you, and quite frankly I have started to find hunting boring." ')
#time.sleep(4.5)
#print (Fore.RED +' "I have hunted around the world, large rhinos? No problem. Siberian Tigers? Easy. Animals, as you see only have their instinct and strength to win a fight, they do not have the wit to fight against man."')
#time.sleep(6)
#print (Fore.RED+'"I was horrified. Think of how I felt! Hunting, my biggest passion started to bore me!"')
#time.sleep(4)
#print (Fore.RED + ' "This is when I decided to find a new animal, one that is cunning, smart, strong, and then it hit me as the perfect animal to hunt." ')
#time.sleep(5.5)
#print (Fore.BLACK + ' You have an idea of what he is going to say but you ask anyways,' ,Fore.GREEN + ' "What do you mean the perfect animal?" ')
#time.sleep(4)
#print (Fore.RED +' "Well my dear', name , Fore.RED + ', I am obviously talking about hunting humans." ' )
#time.sleep(2.5)
#print (Fore.RED + ' "You see, I have done my research on you. You are a very skilled hunter and that is why I brought you to this island that I bought. We will both hunt each other!" ' )
#time.sleep(5)
#print (Fore.BLACK + ' The moment you hear this, your eyes widen and you immediately exclaim' , Fore.GREEN + ' "You must be out of your mind to be doing this! Hunting humans!? That is basically murder!" ')
#time.sleep(4)
#print (Fore.BLACK + ' General Health laughs in your face.' , Fore.RED + ' "Well it is more enjoyable than hunting other animals. Do you want me to be bored?" ')
#time.sleep(4)
#print (Fore.GREEN+'"Are you insane? Are you not afraid of death!?"')
#time.sleep(3)
#print (Fore.BLACK + ' General Health laughs in your face again.' , Fore.RED + ' "Well that is the thrill of the hunt, my friend!" ')
#time.sleep(4)
#print (Fore.BLACK + ' You try to leave, but the general says to your back,' , Fore.RED + '"If you win you can keep this island or go home."', Fore.BLACK + "Seeing no way else to leave the island except killing the general, you decide that you have to accept his challenge.")
#time.sleep(6)
#print (Fore.BLACK + ' You tell him that you accept his challenge.')
#time.sleep(3)
#print (' The general shows a wide smile' , Fore.RED + '"Great! Now let me explain the rules."')
#time.sleep(3)
#print (Fore.RED + ' "I will supply you with a few knives, hunting clothes, and a small amount of food."')
#time.sleep(4)
#print (Fore.RED + ' "However, I myself have a Colt Python gun and two hunting dogs by my side. I will alot you a couple of hours as a headstart. Remember, you goal is to kill me." ')
#time.sleep(5)
#print (Fore.BLACK + ' The general throws the supplies at your feet and you start picking them up.')
#time.sleep(4.5)
#print (Fore.RED + ' " and ......"')
#time.sleep(1.3)
#print (Fore.RED + ' "START! " ')
##Not mentioned to player but it takes 3 hits to kill general 

time.sleep(.5)
print(Fore.BLACK + " You start running East.")
time.sleep(5)
print(Fore.BLACK + " You stop to catch your breath. You can continue to run",Fore.MAGENTA + "East,",Fore.BLACK + "or go back", Fore.MAGENTA + "West.")
player_choice = input("")
while player_choice != "East" and player_choice != "West":
    print(Fore.BLACK + ' Choose either',Fore.MAGENTA +'"East"',Fore.BLACK+ "or",Fore.MAGENTA+'"West",',Fore.BLACK+ 'please.')
    print(Fore.BLACK+" You can continue to run", Fore.MAGENTA+"East,",Fore.BLACK+ "or go back",Fore.MAGENTA+"West.",Fore.MAGENTA)
    player_choice = input("")
if player_choice == "East":
    print(Fore.BLACK + " You continue running East.")
    time.sleep(2)
    print(Fore.BLACK + " You decide to look backwards, and off in the distance you see...")
    time.sleep(1)
    print(Fore.GREEN+ ' "The general' + "'s gaining on me!" + '"')
    time.sleep(1)
    print(Fore.BLACK + " You spot a large tree ahead of you. You can stay and",Fore.MAGENTA+ 'fight',Fore.BLACK + 'the general or',Fore.MAGENTA +'hide',Fore.BLACK+ 'in the tree.',Fore.MAGENTA)
    player_choice = input("")
    while player_choice != "Fight" and player_choice != "Hide":
        print(Fore.BLACK+' Choose either',Fore.MAGENTA+ '"Fight"',Fore.BLACK+ 'or',Fore.MAGENTA+ '"Hide",',Fore.BLACK+ 'please.')
        print(Fore.BLACK + " You can stay and",Fore.MAGENTA+ "fight",Fore.BLACK+ "the general, or",Fore.MAGENTA+ "hide in the tree.",Fore.MAGENTA)
        player_choice = input("")
    if player_choice == "Hide":
        print(Fore.BLACK+" You quickly climb the tree to hide from the general.")
        time.sleep(2)
        print(" The general arrives at the tree and stands under it.")
        time.sleep(1)
        print(Fore.BLACK + " He doesn't seem to notice you. You probably could",Fore.MAGENTA + "jump him",Fore.BLACK + "or you could", Fore.MAGENTA + "stay", Fore.BLACK + "in hiding.",Fore.MAGENTA)
        player_choice = input("")
        while player_choice != "Jump him" and player_choice != "Stay":
            print(Fore.BLACK+' Choose either',Fore.MAGENTA+ '"Jump him"',Fore.BLACK+ "or",Fore.MAGENTA+ '"Stay",',Fore.BLACK+ 'please.')
            print(Fore.BLACK+" You probably could",Fore.MAGENTA + "jump him",Fore.BLACK + "or you could", Fore.MAGENTA + "stay", Fore.BLACK + "in hiding.",Fore.MAGENTA)
            player_choice = input("")
        if player_choice == "Stay":
            print(Fore.BLACK + " The general moves away. You spend the night in the tree.")
            time.sleep(5)
            print(" The next day, the general is nowhere to be seen. You climb down the tree.")
            time.sleep(2)
            print(" You can either",Fore.MAGENTA + 'lay a trap',Fore.BLACK+ ' for the general, or start to',Fore.MAGENTA+'run.',Fore.MAGENTA)
            player_choice = input("")
            while player_choice != "Lay a trap" and player_choice != "Run":
                print(Fore.BLACK+' Choose either',Fore.MAGENTA+ '"Lay a trap"',Fore.BLACK+ "or",Fore.MAGENTA+ '"Run",',Fore.BLACK+ 'please.')
                print(Fore.BLACK+" You can either lay a trap for the general or start running.",Fore.MAGENTA)
                player_choice = input("")
            if player_choice == "Lay a trap":
                print(Fore.BLACK+" You tie a knife to a sapling, pull it back, and tie the twig down.")
            print(Fore.BLACK+" You start running North.")
            time.sleep(5)
            if player_choice == "Lay a trap":
                print(Fore.BLACK+' You hear the trap spring.')
                print(' The general yells in pain, and then mutters,',Fore.RED+ '"'+"You'" + 're a crafty one, I' + "'ll" + ' give you that."')
                general_health -= 1
                time.sleep(2)
            print(Fore.BLACK + " You arrive at a swamp. The area is muddy and has many broken tree branches scattered around.")
            time.sleep(1)
            print(" You can turn back and",Fore.MAGENTA +'fight',Fore.BLACK+ 'the general, or',Fore.MAGENTA+ 'set another trap',Fore.BLACK+ "in the swamp.",Fore.MAGENTA)
            player_choice = input("")
            while player_choice != "Fight" and player_choice != "Set another trap":
                print(Fore.BLACK+' Choose either',Fore.MAGENTA+ '"Fight"',Fore.BLACK+ 'or',Fore.MAGENTA+ '"Set another trap",',Fore.BLACK+ 'please.')
                print(" You can turn back and",Fore.MAGENTA +'fight',Fore.BLACK+ 'the general, or',Fore.MAGENTA+ 'set another trap',Fore.BLACK+ "in the swamp.",Fore.MAGENTA)
                player_choice = input("")
            if player_choice == "Set another trap":
                print (Fore.BLACK+' You look behind you and see that the general is not near.')
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
                print(" You can either start to",Fore.MAGENTA+'run West,',Fore.BLACK+ 'or stay and',Fore.MAGENTA+ "fight",Fore.BLACK+ "the general.",Fore.MAGENTA)
                player_choice = input("")
                while player_choice != "Run West" and player_choice != "Fight":
                    print(Fore.BLACK+' Chooes either',Fore.MAGENTA+ '"Run West"',Fore.BLACK+ 'or',Fore.MAGENTA+ '"Fight",',Fore.BLACK+ 'please.')
                    print(" You can either start to",Fore.MAGENTA+'run West,',Fore.BLACK+ 'or stay and',Fore.MAGENTA+ "fight",Fore.BLACK+ "the general.",Fore.MAGENTA)
                    player_choice = input("")
                if player_choice == "Run West":
                    print (Fore.BLACK+' You return into the forest area.')
                    time.sleep(1.5)
                    print (' While considering your options, you notice that the forest has many vines.')
                    time.sleep(3)
                    print(" You can either choose to",Fore.MAGENTA + 'fight',Fore.BLACK+ 'the general, or',Fore.MAGENTA +"set yet another trap.", Fore.MAGENTA)
                    player_choice = input("")
                    while player_choice != "Fight" and player_choice != "Set yet another trap":
                        print(Fore.BLACK+' Choose either', Fore.MAGENTA+ '"Fight"',Fore.BLACK+ 'or',Fore.MAGENTA+'"Set yet another trap",',Fore.BLACK+ 'please.')
                        print(" You can either choose to",Fore.MAGENTA + 'fight',Fore.BLACK+ 'the general, or',Fore.MAGENTA +"set yet another trap.", Fore.MAGENTA)
                        player_choice = input("")
                    if player_choice == "Set yet another trap":
                        print (Fore.BLACK+' An idea comes to your mind. You start getting the vines and start making a net.')
                        time.sleep(3)
                        print (' You cover the finished net in a bunch of leaves and branches, and hang the net high in a tree.')
                        time.sleep(3)
                        print (' You start leaving the area toward a cliff.')
                        time.sleep(2)
                        print (' While you are leaving, you hear another howl of a dog, but this time you do not look behind you since you know your trap worked.')
                        time.sleep(2)
                        print(' You would think that the general learned from the previous traps, but it seems he still falls for it each time.')
                        time.sleep(4)
                        print(" You arrive at a cliff. The general hot on your heels. You can either",Fore.MAGENTA+ 'jump',Fore.BLACK+ 'off, or',Fore.MAGENTA+"fight",Fore.BLACK+ "the general.",Fore.MAGENTA)
                        player_choice = input("")
                        while player_choice != "Jump" and player_choice != "Fight":
                            print(' Choose either',Fore.MAGENTA+ '"Jump"',Fore.BLACK+ 'or',Fore.MAGENTA+ '"Fight",',Fore.BLACK+ 'please.')
                            print(" You can either",Fore.MAGENTA+ 'jump',Fore.BLACK+ 'off, or',Fore.MAGENTA+"fight",Fore.BLACK+ "the general.",Fore.MAGENTA)
                            player_choice = input("")
                        if player_choice == "Jump":
                            print (Fore.BLACK+" You jump off the cliff and land in the water below.")
                            time.sleep(2)
                            print(" You start to swim toward the general's house.")
                            time.sleep(2)
                            print (' The general scoffs and says,',Fore.RED+ '"I wanted to land the killing blow, too bad he jumped." ')
                            time.sleep(3)
                            print (' "At least I won the hunt."')
                            time.sleep(2)
                            print (Fore.BLACK+' The general walks back home and puts his gun on his drawer. He then lays on his bed after the hunt to sleep.')
                            time.sleep(4)
                            print (' You finally made it to the back of the generals house. You climb up his house toward his window.')
                            time.sleep(3)
                            print (" You wait outside the general's window and decide you could use some rest.")
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
                            print (' His eyes dart to the gun in your hand.')
                            time.sleep(1.5)
                            print (Fore.RED+' "Well"')
                            time.sleep(1)
                            print ('.')
                            time.sleep(1)
                            print ('.')
                            time.sleep(1)
                            print ('.')
                            time.sleep(1)
                            print ( '"Looks like that was my last hunt."',Fore.BLACK+" General Health gives a wry smile",Fore.RED+'"At least you gave me the thrill I was seeking."')
                            time.sleep(3)
                            print (Fore.BLACK+' You load the gun and point it at him.')
                            time.sleep(1.5)
                            print (Fore.GREEN+' "I guess we both win then."') 
                            time.sleep(2)
                            print (Fore.BLACK+' You shoot the general in the head.')
                            time.sleep(2)
                            print (" You win.")
                    else:
                        print(Fore.BLACK+" The general catches up to you.")
                        fight_general_with_1_dog(general_health)
                else:
                    print(Fore.BLACK+" The general soon rushes to where you are, furious with the loss.")
                    fight_general_with_1_dog(general_health)
            else:
                print(Fore.BLACK+" The general catches up to you, fuming with anger.")
                fight_general_with_2_dogs(general_health)
        else:
            print(Fore.BLACK+" You drop from the tree, slashing the general on the way down.")
            general_health -= 1
            time.sleep(1)
            fight_general_with_2_dogs(general_health)
    else:
        print(Fore.BLACK+" The general catches up to you.")
        time.sleep(1)
        print(Fore.BLACK+' He says,',Fore.RED+ '"You shouldn'+"'"+'t have let me catch up to you."')
        fight_general_with_2_dogs(general_health)
else:
    print(Fore.BLACK+" You run back towards where you started.")
    time.sleep(3)
    print(Fore.BLACK+" You bump into the general.")
    time.sleep(.5)
    print(Fore.BLACK+' He says,' ,Fore.RED+ '"It was foolish of you to run towards me."')
    fight_general_with_2_dogs(general_health)