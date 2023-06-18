# Text adventure game using if..elif..else statements.
import ascii_art 
from clearscreen import clear

# Introduction
print(ascii_art.fairy_queen1)
print("Hello! I'm Estelle, the fairy queen. I am so happy to meet you. You've arrived just in time to help us overthrow the Beast King.")
print("But first, tell me your name Great Adventurer!")

player_name = input(">")

clear()

print(ascii_art.fairy_queen2)
print(f"{player_name}! A name worthy of a brave warrior such as yourself!")
print("Now, we do not have a lot of time. As we speak, the Beast King is plotting to destroy our village. We need your help to usurp his plans by sneaking into his stronghold, and stealing the blueprints.")
print(f"Do not worry, {player_name}! You will be greatly rewarded by my people. You must go now, before it's too late! Good luck!")

# Keeps prompting user for valid input until it is correct
while True:
	print("Enter 'Y' to be teleported to the next destination.")
	start = input(">").upper()
	if start == "Y": break

clear()

print("========== LOCATION: THE LAND OF FURDOR WHERE THE BEAST KING RULES ==========")
print(ascii_art.spider)
print("========== BEWARE THE LURKING CREATURES ==========")
print("You are out in the open, and immediately spot a group of beast folk carrying weapons. They are heading to your current position, luckily they haven't spotted you as yet.")
print("You look around and notice thick shrubbery to your left that can help mask your presence. On your right, there is a tall tree with low branches that you can climb.")
print("Where do you want to hide? Enter 'left' to go to the shrubbery or 'right' to climb the tree.")

choice_path = input(">").lower()

clear()

# Story line options based of if..elif..else statements
if choice_path == "left":
	print(ascii_art.lake)
	print("Woah! You fell right into the rabbit hole hidden in the shrubbery. After what felt like hours, you landed in a heap on the wet ground. You've got a cut on your leg from the fall, that makes it difficult to walk.")
	print("You're in luck though! There are two lakes in this underground cave. One looks ominous with dark, murky water that gives off a horrible stench. The other lake is crystal clear without an animal in sight.")
	print("You need to clean your wounds before finding an exit. Enter 'dark' to use the water from the dark lake or 'crystal' to use the water from the clear lake.")

	lake_choice = input(">").lower()

	clear()

	if lake_choice == "dark":
		print(ascii_art.tunnel)
		print("The blood from your wound purified the lake! A path suddenly opens to a tunnel that leads you out of the cave, directly into what seems as a barricaded room with weapons, armor and documents lying around.")
		print("You realize this is actually the war room used by the Beast King and his generals. On the table are different documents, showing the layout of the Fairy Queen's land. Before you can look around some more, you hear the sound of approaching footsteps!")
		print("Are you prepared to fight or run off with the papers? Enter 'fight' to grab a weapon or 'papers' to grab the documents.")

		fight_flight = input(">")

		clear()

		print("========== THE BEAST KING ENTERS ==========")

		if fight_flight == "fight":
			print(ascii_art.beast_king)
			print("You grab the nearest weapon - a sword! The Beast King is surprised to find you here. Before you could attack, restrain with strange magic.")
			print("The general notices your wounds and brought you to a healer with the approval of the Beast King. Once you're healed, you find out the true intentions of the Fairy Queen.")
			print("It seems Estelle uses life draining magic on the beast folk to keep her youth! You are now working with the Beast King to take down the Fairy Queen!")
			print("==== UNTIL NEXT TIME ====", ascii_art.hero)
		elif fight_flight == "papers":
			print(ascii_art.cat)
			print("Oh no! Nature magic was used to protect the documents. The spell changes you into a cat. At least you're a cute and cuddly kitten, and the Beast King dotes on you :)")
			print(ascii_art.game_over)

	elif lake_choice == "crystal":
		print(ascii_art.octopus)
		print("Ahh! The clear water was an illusion. Hiding in the water is a giant octopus that drags you down under to be it's first meal in a long time!")
		print(ascii_art.game_over)

elif choice_path == "right":
	print(ascii_art.new_world)
	print("The high branches on the tree lead you right into a portal that transports you into a different dimension. Looks like it's time for a bizarre adventure!")
	print(ascii_art.game_over)

else:
	print("You have entered the wrong value! A black hole appeared and destroyed the world.")
	print("==== UNTIL NEXT TIME ====", ascii_art.destroyer)
